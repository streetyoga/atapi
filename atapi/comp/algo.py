"""Computation Module"""
import os
from functools import cached_property
import numpy as np
import pandas as pd
import scipy.optimize as sco
import requests
from binance.spot import Spot as Client

MC_BASE = 'https://www.binance.com'
MC_EP = '/exchange-api/v2/public/asset-service/product/get-products'
MC_URL = MC_BASE + MC_EP  # For Circulating Supply Data
TR_BASE = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/'
TR_EP = 'v2/accounting/od/avg_interest_rates'
TR_URL = TR_BASE + TR_EP
TD = 365.25  # Trading days + 1/4 leap day.


def riskfree_return():
    """Riskfree Return"""
    response = requests.get(TR_URL+'?sort=-record_date&page[size]=1')
    data = response.json()['data'][0]['avg_interest_rate_amt']
    return float(data)/100


rfr = riskfree_return()  # T-Bill Average Interest Rate


# API key not used
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'))


class Algo:
    """Quantitative Analysis"""
    columns = ('Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
               'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
               'Taker buy quote asset volume', 'Ignore')

    @staticmethod
    def circulating_supply():
        """Circulating Supply"""
        response = requests.get(MC_URL)
        data = response.json()['data']
        return pd.Series({item['s']: item['cs'] for item in data if item['s'].endswith('USDT')}, name='Circulating Supply')
    symbols = circulating_supply().index.values.tolist()

    @staticmethod
    def servertime():
        """Returns the servertime.
If your systemtime is off, synchronize with timeserver."""
        # TODO exception when time is out of sync
        return pd.to_datetime(client.time()['serverTime'], unit='ms')

    @cached_property
    def assets(self):
        """Assets, all columns"""
        _assets = pd.concat((pd.DataFrame(client.klines(symbol, "1d"), columns=self.columns).set_index('Open time')
                            for symbol in self.symbols[:3]), axis=1, keys=self.symbols[:3])
        _assets = _assets.swaplevel(axis=1)  # Swapping levels for selection
        _assets.index = pd.to_datetime(_assets.index, unit='ms')
        _assets.index.name = 'Date'
        return _assets

    def assets_close(self):
        """Asset close prices"""
        _assets_close = self.assets["Close"].copy().astype(float)
        return _assets_close

    @property
    def asset_qty(self):
        """Asset Quantity"""
        _asset_qty = len(self.assets_close().columns)
        return _asset_qty

    def marketcap(self):
        """Simplified MarketCap"""
        _marketcap = self.assets_close().mul(
            self.circulating_supply()[:3])
        return _marketcap

    def marketcap_summary(self):
        """Daily marketcap summary of all assets."""
        _marketcap_summary = self.marketcap().sum(
            axis=1).rename('Total MarketCap')
        return _marketcap_summary

    def weights_cwi(self):
        # TODO use marketcap_summmary()
        """Capital Weights"""
        _weights_cwi = self.marketcap().div(
            self.marketcap().sum(axis=1), axis='index')
        return _weights_cwi

    @property
    def weights_pwi(self):
        """Price weighted index."""
        weights_pwi = self.assets_close().div(
            self.assets_close().sum(axis=1), axis='rows')
        return weights_pwi

    @property
    def weights_ewi(self):
        """Equal weighted index."""
        weights_ewi = self.assets_close().copy()
        weights_ewi.iloc[:] = 1 / self.asset_qty
        return weights_ewi

    @staticmethod
    def stats_index():
        """Annualized risk & return of all assets."""
        _stats_index = np.log(normalized / normalized.shift()
                              ).dropna().agg(['mean', 'std']).T
        _stats_index.columns = ['Return', 'Risk']
        _stats_index['Return'] = _stats_index['Return'] * TD
        _stats_index['Risk'] = _stats_index['Risk'] * np.sqrt(TD)
        return _stats_index

    @staticmethod
    def mean_returns():
        """Daily Mean Returns Of All Assets."""
        _mean_returns = returns.mean().rename('Mean Returns')
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
    def annualized_risk_return(ret):
        """Annualized Risk σ, Return"""
        stat = ret.agg(['mean', 'std']).T
        stat.columns = ['Return', 'Risk']
        stat.Return = stat.Return * TD
        # TODO Cap needed if annualized losses > 100% even with log returns
        # stats.loc[stats.Return < -1, 'Return'] = -1
        stat.Risk = stat.Risk * np.sqrt(TD)
        return stat


algo = Algo()
returns = np.log(algo.assets_close() /
                 algo.assets_close().shift()).dropna()

normalized = algo.assets_close().div(
    algo.assets_close().iloc[0]).mul(100)
normalized['PWI'] = algo.assets_close().sum(
    axis=1).div(algo.assets_close().sum(axis=1)[0]).mul(100)
returns_index = returns.copy()
returns_index['Mean'] = returns_index.mean(axis=1)
normalized['EWI'] = 100
normalized.iloc[1:, -1] = returns_index.Mean.add(1).cumprod().mul(100)
normalized['CWI'] = 100
normalized.iloc[1:, -1] = returns.mul(algo.weights_cwi().shift().dropna()
                                      ).sum(axis=1).add(1).cumprod().mul(100)


def portfolio_return(weights):
    """Annualized Portfolio Return"""
    return returns.dot(weights.T).mean() * TD


def portfolio_risk(weights):
    """Annualized Portfolio Risk"""
    return returns.dot(weights.T).std() * np.sqrt(TD)


def minimized_sharpe(weights):
    """Sharpe Ratio * (-1)"""
    return (rfr - portfolio_return(weights)) / portfolio_risk(weights)


# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
equal_weights = np.full(algo.asset_qty, 1 / algo.asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(algo.asset_qty))
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
optimal_weights = optimum['x']
optimal_weights = pd.Series(
    index=algo.assets_close().columns, data=optimal_weights, name='Optimal Weights')
returns['TP'] = returns.dot(
    optimal_weights)

# Annualized Statistics
stats = algo.annualized_risk_return(returns)
stats['Sharpe'] = stats['Return'].sub(
    rfr) / stats['Risk']
stats['Var'] = np.power(stats.Risk, 2)
stats['SysVar'] = algo.covar.iloc[:, -1]
stats['UnsysVar'] = stats['Var'].sub(stats['SysVar'])
stats['beta'] = stats['SysVar'] / \
    stats.loc['TP', 'SysVar']  # Normalize == beta
# Expected Return
stats['CAPM'] = rfr + \
    (stats.loc["TP", "Return"] - rfr) * stats.beta
# Alpha, asset below or above Security market line
stats['alpha'] = stats.Return - stats.CAPM

# Marketcap Portfolio
returns_mcap = returns.drop(columns=['TP'])
returns_mcap['MCAP'] = returns_mcap.mul(
    algo.weights_cwi().shift().dropna()).sum(axis=1)
stats_mcap = algo.annualized_risk_return(returns_mcap)
covar_mcap = returns_mcap.cov() * TD
stats_mcap['SysVar'] = covar_mcap.iloc[:, -1]
stats_mcap['beta'] = stats_mcap['SysVar'] / \
    stats_mcap.loc['MCAP', 'SysVar']