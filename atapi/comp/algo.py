"""Computation Module"""
import os
from functools import cached_property
import numpy as np
import pandas as pd
import scipy.optimize as sco
import requests
from binance.spot import Spot as Client

MC_BASE = 'https://www.binance.com'
MC_PATH = '/exchange-api/v2/public/asset-service/product/get-products'
MC_URL = MC_BASE + MC_PATH  # For Circulating Supply Data
RISKFREE_RETURN = 0.031  # 5 Year Treasury Rate
TD = 365.25  # Trading days + 1/4 leap day.

# API key not used
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'))


# Testnet API for balance
client_test = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'), base_url='https://testnet.binance.vision')


class Algo:
    """Quantitative Analysis"""
    symbols = ('BTCUSDT', 'ETHUSDT', 'BNBUSDT',
               'XRPUSDT', 'TRXUSDT', 'LTCUSDT')
    columns = ('Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
               'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
               'Taker buy quote asset volume', 'Ignore')

    @cached_property
    def circulating_supply(self):
        """Circulating Supply"""
        response = requests.get(MC_URL)
        data = response.json()['data']
        return pd.Series({item['s']: item['cs'] for item in data
                          if item['s'] in self.symbols}, name='Circulating Supply')

    @staticmethod
    def balance():
        """Balance and kline fields for selected assets."""
        return pd.json_normalize(client_test.account()['balances'])

    @staticmethod
    def servertime():
        """Returns the servertime.
If your systemtime is off, synchronize with timeserver."""
        # TODO exception when time is out of sync
        return pd.to_datetime(client.time()['serverTime'], unit='ms')

    @cached_property
    def assets(self):
        """Assets, all columns"""
        _assets = pd.concat((pd.DataFrame(client.klines(symbol, "1d"), columns=self.columns)
                            for symbol in self.symbols), axis=1, keys=self.symbols)
        _assets = _assets.swaplevel(axis=1)  # Swapping levels for selection
        _assets = _assets.set_index(pd.to_datetime(
            _assets.iloc[:, 6], unit='ms').dt.date)
        _assets.index.name = 'Date'
        return _assets

    @property
    def assets_close(self):
        """Asset close prices"""
        _assets_close = self.assets["Close"].copy().astype(float)
        return _assets_close

    @property
    def asset_qty(self):
        """Asset Quantity"""
        _asset_qty = len(self.assets_close.columns)
        return _asset_qty

    @property
    def marketcap(self):
        """Simplified MarketCap"""
        marketcap = self.assets_close.mul(
            self.circulating_supply)
        return marketcap

    @property
    def marketcap_summary(self):
        """Daily marketcap summary of all assets."""
        marketcap_summary = self.marketcap.sum(
            axis=1).rename('Total MarketCap')
        return marketcap_summary

    @property
    def weights_cwi(self):
        # TODO use marketcap_summmary()
        """Capital Weights"""
        _weights_cwi = self.marketcap.div(
            self.marketcap.sum(axis=1), axis='index')
        return _weights_cwi

    @property
    def weights_pwi(self):
        """Price weighted index."""
        weights_pwi = self.assets_close.div(
            self.assets_close.sum(axis=1), axis='rows')
        return weights_pwi

    @property
    def weights_ewi(self):
        """Equal weighted index."""
        weights_ewi = self.assets_close.copy()
        weights_ewi.iloc[:] = 1 / self.asset_qty
        return weights_ewi

    @staticmethod
    def stats_index():
        """Anualized risk / return of all assets."""
        _stats_index = np.log(normalized / normalized.shift()
                              ).dropna().agg(['mean', 'std']).T
        _stats_index.columns = ['Return', 'Risk']
        _stats_index['Return'] = _stats_index['Return'] * TD
        _stats_index['Risk'] = _stats_index['Risk'] * np.sqrt(TD)
        return _stats_index

    @staticmethod
    def mean_returns():
        """Daily Mean Returns Of All Assets."""
        _mean_returns = returns.mean(axis=0).rename('Mean Returns')
        return _mean_returns

    @staticmethod
    def correlation():
        """Correlation Coefficient"""
        _correlation = returns.corr()
        return _correlation

    @property
    def covar(self):
        """Covariance"""
        _covar = returns.cov() * TD
        return _covar

    @staticmethod
    def annualised_risk_return(ret):
        """Annualized Risk σ, Return"""
        stat = ret.agg(['mean', 'std']).T
        stat.columns = ['Return', 'Risk']
        stat.Return = stat.Return * TD
        # TODO Cap might be needed if annualized losses > 100% with log returns
        # stats.loc[stats.Return < -1, 'Return'] = -1
        stat.Risk = stat.Risk * np.sqrt(TD)
        return stat


algo = Algo()
returns = np.log(algo.assets_close /
                 algo.assets_close.shift()).dropna()

normalized = algo.assets_close.div(
    algo.assets_close.iloc[0]).mul(100)
normalized['PWI'] = algo.assets_close.sum(
    axis=1).div(algo.assets_close.sum(axis=1)[0]).mul(100)
returns_index = returns.copy()
returns_index['Mean'] = returns_index.mean(axis=1)
normalized['EWI'] = 100
normalized.iloc[1:, -1] = returns_index.Mean.add(1).cumprod().mul(100)
normalized['CWI'] = 100
normalized.iloc[1:, -1] = returns.mul(algo.weights_cwi.shift().dropna()
                                      ).sum(axis=1).add(1).cumprod().mul(100)


def portfolio_return(weights):
    """Annualized Portfolio Return"""
    return returns.dot(weights.T).mean() * TD


def portfolio_risk(weights):
    """Annualized Portfolio Risk"""
    return returns.dot(weights.T).std() * np.sqrt(TD)


def minimized_sharpe(weights):
    """Sharpe Ratio * (-1)"""
    return (RISKFREE_RETURN - portfolio_return(weights)) / portfolio_risk(weights)


# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
equal_weights = np.full(algo.asset_qty, 1 / algo.asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(algo.asset_qty))
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
optimal_weights = optimum['x']
optimal_weights = pd.Series(
    index=algo.assets_close.columns, data=optimal_weights, name='Optimal Weights')
returns['TP'] = returns.dot(
    optimal_weights)

# Annualised Statistics
stats = algo.annualised_risk_return(returns)
stats['Sharpe'] = stats['Return'].sub(
    RISKFREE_RETURN) / stats['Risk']
stats['Variance'] = np.power(stats.Risk, 2)
stats['Sys. Var.'] = algo.covar.iloc[:, -1]
stats['Unsys. Var.'] = stats['Variance'].sub(stats['Sys. Var.'])
stats['beta'] = stats['Sys. Var.'] / \
    stats.loc['TP', 'Sys. Var.']  # Normalize == beta
# Expected Return
stats['CAPM'] = RISKFREE_RETURN + \
    (stats.loc["TP", "Return"] - RISKFREE_RETURN) * stats.beta
# Alpha, asset below or above Security market line
stats['alpha'] = stats.Return - stats.CAPM

# Marketcap Portfolio
returns_mcap = returns.drop(columns=['TP'])
returns_mcap['MCAP'] = returns_mcap.mul(
    algo.weights_cwi.shift().dropna()).sum(axis=1)
stats_mcap = algo.annualised_risk_return(returns_mcap)
covar_mcap = returns_mcap.cov() * TD
stats_mcap['Sys. Var.'] = covar_mcap.iloc[:, -1]
stats_mcap['beta'] = stats_mcap['Sys. Var.'] / \
    stats_mcap.loc['MCAP', 'Sys. Var.']
