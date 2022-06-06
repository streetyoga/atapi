"""Algorithmic Trading Framework"""
__version__ = "0.1.1"
import os
import sys
import cmd
from functools import cached_property
import pandas as pd
import numpy as np
import scipy.optimize as sco
from binance.spot import Spot as Client
import requests

MC_BASE = 'https://www.binance.com'
MC_PATH = '/exchange-api/v2/public/asset-service/product/get-products'
MC_URL = MC_BASE + MC_PATH  # For Circulating Supply Data
RISKFREE_RETURN = 0.031  # 5 Year Treasury Rate
pd.options.display.float_format = '{:.4f}'.format


class AF:
    """Algorithmic Factory"""

    def __init__(self, biofuel, o_2):
        self.biofuel = biofuel
        self.o_2 = o_2

    @staticmethod
    def create():
        """Create Algorithms"""
        raise NotImplementedError('Grand Opening Soon...')

    @staticmethod
    def menu():
        """Factory Menu"""
        menu = """Enter:
- 'a' algorithm
- 's' strategy
- 'c' create
- '⏎' back
Choose: """
        while user_input := input(menu):
            {'a': lambda: None,
             's': lambda: None,
             'c': AF.create
             }.get(user_input, lambda: print('Invalid Input'))()


# API key not used
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'))


# Testnet API for balance
client_test = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'), base_url='https://testnet.binance.vision')


class ATFShell(cmd.Cmd):
    """Line-oriented command interpreter"""
    intro = 'Welcome to the Algorithmic Trading Framework. Type help or ? for commands.\n'
    prompt = 'atf🖖  '
    symbols = ('BTCUSDT', 'ETHUSDT', 'BNBUSDT',
               'XRPUSDT', 'TRXUSDT', 'LTCUSDT')
    columns = ('Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
               'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
               'Taker buy quote asset volume', 'Ignore')

    @cached_property
    def assets(self):
        """Assets, all columns"""
        _assets = pd.concat((pd.DataFrame(client.klines(symbol, "1d"), columns=self.columns)
                            for symbol in self.symbols), axis=1, keys=self.symbols)
        _assets = _assets.swaplevel(axis=1)  # Swapping levels for selection
        # TODO all assets have same close time, change to selection without asset name
        _assets.set_index(pd.to_datetime(
            _assets['Close time', 'BTCUSDT'], unit='ms').dt.date, inplace=True)
        _assets.index.name = 'Date'
        return _assets

    @staticmethod
    def do_algorithmic_factory(arg):
        """Enters Factory"""
        AF.menu()

    @staticmethod
    def do_bye(arg):
        'Exits the framework.'
        print('Thank you for using ATF')
        sys.exit()

    @staticmethod
    def do_servertime(arg):
        """Returns the servertime.
If your systemtime is off, synchronize with timeserver."""
        print(pd.to_datetime(client.time()['serverTime'], unit='ms'))

    @staticmethod
    def do_balance(arg):
        """Balance and kline fields for selected assets."""
        print(pd.json_normalize(client_test.account()['balances']))

    @cached_property
    def circulating_supply(self):
        """Circulating Supply"""
        response = requests.get(MC_URL)
        data = response.json()['data']
        return pd.Series({symbol: item['cs'] for item in data
                          for symbol in self.symbols if
                          item['s'] == symbol}).to_frame('Circ. Supp.')

    def do_circulating_supply(self, arg):
        """Returns the circulating supply."""
        print(self.circulating_supply)

    @property
    def assets_close(self):
        """Asset close prices"""
        _assets_close = self.assets["Close"].copy().astype(float)
        return _assets_close

    def do_assets_close(self, arg):
        """Daily close price data for assets."""
        print(self.assets_close)

    @property
    def asset_qty(self):
        """Asset Quantity"""
        _asset_qty = len(self.assets_close.columns)
        return _asset_qty

    @property
    def marketcap(self):
        """Simplified MarketCap"""
        # Windows astype(int) defautls to int32 contrary to linux
        marketcap = self.assets_close.mul(
            self.circulating_supply.squeeze()).astype('int64')
        return marketcap

    def do_marketcap(self, arg):
        """Simplified marketcap, only with last circulating supply."""
        print(self.marketcap)

    def do_marketcap_summary(self, arg):
        """Daily marketcap summary of all assets."""
        marketcap_summary = self.marketcap.sum(
            axis=1).to_frame('Marketcap Sum.')
        print(marketcap_summary)

    @staticmethod
    def do_optimal_weights(arg):
        """Optimal weights calculated with sequential least squares programming."""
        print(optimal_weights)

    @staticmethod
    def do_returns(arg):
        """Daily logarithmic returns."""
        return print(returns)

    @staticmethod
    def do_normalized(arg):
        """Normalized assets."""
        print(normalized)

    @property
    def weights_cwi(self):
        """Capital Weights"""
        _weights_cwi = self.marketcap.div(
            self.marketcap.sum(axis=1), axis='index')
        return _weights_cwi

    def do_weights_cwi(self, arg):
        """Capital weighted index."""
        print(self.weights_cwi)

    def do_weights_pwi(self, arg):
        """Price weighted index."""
        weights_pwi = self.assets_close.div(
            self.assets_close.sum(axis=1), axis='rows')
        print(weights_pwi)

    def do_weights_ewi(self, arg):
        """Equal weighted index."""
        weights_ewi = self.assets_close.copy()
        weights_ewi.iloc[:] = 1 / self.asset_qty
        print(weights_ewi)

    def do_stats_index(self, arg):
        """Anualized risk / return of all assets."""
        stats_index = np.log(normalized / normalized.shift()
                             ).dropna().agg(['mean', 'std']).T
        stats_index.columns = ['Return', 'Risk']
        stats_index['Return'] = stats_index['Return'] * 365.25
        stats_index['Risk'] = stats_index['Risk'] * np.sqrt(365.25)
        print(stats_index)

    @staticmethod
    def do_mean_returns(arg):
        """Daily Mean Returns Of All Assets."""
        mean_returns = returns.mean(axis=0).to_frame('Mean Returns')
        print(mean_returns)

    @staticmethod
    def do_correlation(arg):
        """Correlation Coefficient"""
        correlation = returns.corr()
        print(correlation)

    @property
    def covar(self):
        """Covariance"""
        _covar = returns.cov() * 365.25
        return _covar

    def do_covariance(self, arg):
        """Covariance."""
        print(self.covar)

    @staticmethod
    def annualised_risk_return(ret):
        """Annualized Risk σ, Return"""
        stat = ret.agg(['mean', 'std']).T
        stat.columns = ['Return', 'Risk']
        stat.Return = stat.Return * 365.25  # Trading days + 1/4 leap day.
        # TODO Cap might be needed if annualized losses > 100% with log returns
        # stats.loc[stats.Return < -1, 'Return'] = -1
        stat.Risk = stat.Risk * np.sqrt(365.25)
        return stat

    @staticmethod
    def do_stats(arg):
        """Return, risk, sharpe, variance, systematic variance,
unsystematic variance, beta, CAPM, alpha."""
        print(stats)

    @staticmethod
    def do_stats_mcap(arg):
        """Marketcap portfolio."""
        print(stats_mcap)


shell = ATFShell()

returns = np.log(shell.assets_close /
                 shell.assets_close.shift()).dropna()

normalized = shell.assets_close.div(
    shell.assets_close.iloc[0]).mul(100)
normalized['PWI'] = shell.assets_close.sum(
    axis=1).div(shell.assets_close.sum(axis=1)[0]).mul(100)
returns_index = returns.copy()
returns_index['Mean'] = returns_index.mean(axis=1)
normalized['EWI'] = 100
normalized.iloc[1:, -1] = returns_index.Mean.add(1).cumprod().mul(100)
normalized['CWI'] = 100
normalized.iloc[1:, -1] = returns.mul(shell.weights_cwi.shift().dropna()
                                      ).sum(axis=1).add(1).cumprod().mul(100)


def portfolio_return(weights):
    """Annualized Portfolio Return"""
    return returns.dot(weights.T).mean() * 365.25


def portfolio_risk(weights):
    """Annualized Portfolio Risk"""
    return returns.dot(weights.T).std() * np.sqrt(365.25)


def minimized_sharpe(weights):
    """Sharpe Ratio * (-1)"""
    return (RISKFREE_RETURN - portfolio_return(weights)) / portfolio_risk(weights)


# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
equal_weights = np.full(shell.asset_qty, 1 / shell.asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(shell.asset_qty))
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
np.set_printoptions(suppress=True)
optimal_weights = optimum['x']
optimal_weights = pd.Series(
    index=shell.assets_close.columns, data=optimal_weights).to_frame('Opt. Weights')
returns['TP'] = returns.dot(
    optimal_weights.squeeze())

# Annualised Statistics
stats = shell.annualised_risk_return(returns)
stats['Sharpe'] = stats['Return'].sub(
    RISKFREE_RETURN) / stats['Risk']
stats['Variance'] = np.power(stats.Risk, 2)
stats['Sys. Var.'] = shell.covar.iloc[:, -1]
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
    shell.weights_cwi.shift().dropna()).sum(axis=1)
stats_mcap = shell.annualised_risk_return(returns_mcap)
covar_mcap = returns_mcap.cov() * 365.25
stats_mcap['Sys. Var.'] = covar_mcap.iloc[:, -1]
stats_mcap['beta'] = stats_mcap['Sys. Var.'] / \
    stats_mcap.loc['MCAP', 'Sys. Var.']

if __name__ == '__main__':
    ATFShell().cmdloop()
