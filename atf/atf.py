#!/usr/bin/env python
# coding: utf-8
"""Algorithmic Trading Framework"""
# %%
import os
import pandas as pd
import numpy as np
import scipy.optimize as sco
from binance.spot import Spot as Client
import requests

MC_BASE = 'https://www.binance.com'
MC_PATH = '/exchange-api/v2/public/asset-service/product/get-products'
MC_URL = MC_BASE + MC_PATH  # For Circulating Supply Data
pd.set_option('display.max_rows', 80)
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
- 'q' quit
Choose: """
        while True:
            user_input = input(menu)
            choice = {'a': lambda: None,
                      's': lambda: None,
                      'c': AF.create
                      }.get(user_input)
<<<<<<< HEAD
            if user_input == 'q':
                break
            if not choice:
                print('Invalid Input')
            else:
                choice()

=======
            if user_input == 'q': break
            elif choice: choice()
            else: print('Invalid Input')
           
>>>>>>> f2fca29b6fe45337947d12db9c93637b3180dce6

# API key not used
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'))


# Testnet API for balance
client_test = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'), base_url='https://testnet.binance.vision')


# Synchronize with timeserver if time is off
def servertime():
    """return the servertime"""
    return pd.to_datetime(client.time()['serverTime'], unit='ms')


# %% Balance and kline fields for selected assets
balance = pd.json_normalize(client_test.account()['balances'])
symbols = ('BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'TRXUSDT', 'LTCUSDT')
columns = ('Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
           'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
           'Taker buy quote asset volume', 'Ignore')
assets = pd.concat((pd.DataFrame(client.klines(symbol, "1d"), columns=columns)
                    for symbol in symbols), axis=1, keys=symbols)
# Circulating Supply
response = requests.get(MC_URL)
data = response.json()['data']
circulating_supply = pd.Series({symbol: item['cs'] for item in data
                                for symbol in symbols if
                                item['s'] == symbol}).to_frame('Circ. Supp.')
# %% Close Price Data for Assets
assets = assets.swaplevel(axis=1)  # Swapping levels for selection
# Set close time as index
# TODO all assets have same close time, change to selection without asset name
assets.set_index(pd.to_datetime(
    assets['Close time', 'BTCUSDT'], unit='ms').dt.date, inplace=True)
assets.index.name = 'Date'
assets_close = assets["Close"].copy().astype(float)  # Daily close prices
asset_qty = len(assets_close.columns)
# Simplified MarketCap, only last Circulating Supply taken into account.
# Windows astype(int) defautls to int32 contrary to linux
marketcap = assets_close.mul(circulating_supply.squeeze()).astype('int64')
marketcap_summary = marketcap.sum(axis=1).to_frame('Marketcap Sum.')

# %% Daily Logarithmic Returns
returns = np.log(assets_close / assets_close.shift()).dropna()
# Normalized Assets
normalized = assets_close.div(assets_close.iloc[0]).mul(100)
# Price Weighted Index
normalized['PWI'] = assets_close.sum(
    axis=1).div(assets_close.sum(axis=1)[0]).mul(100)
returns_index = returns.copy()
returns_index['Mean'] = returns_index.mean(axis=1)
normalized['EWI'] = 100
normalized.iloc[1:, -1] = returns_index.Mean.add(1).cumprod().mul(100)
normalized['CWI'] = 100
weights_cwi = marketcap.div(marketcap.sum(axis=1), axis='index')
normalized.iloc[1:, -1] = returns.mul(weights_cwi.shift().dropna()
                                      ).sum(axis=1).add(1).cumprod().mul(100)

weights_pwi = assets_close.div(assets_close.sum(axis=1), axis='rows')
weights_ewi = assets_close.copy()
weights_ewi.iloc[:] = 1 / asset_qty
stats_index = np.log(normalized / normalized.shift()
                     ).dropna().agg(['mean', 'std']).T
stats_index.columns = ['Return', 'Risk']
stats_index['Return'] = stats_index['Return'] * 365.25
stats_index['Risk'] = stats_index['Risk'] * np.sqrt(365.25)
mean_returns = returns.mean(axis=0).to_frame('Mean Returns')

# %% Correlation Coefficient
correlation = returns.corr()

# %% Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
RISKFREE_RETURN = 0.031  # 5 Year Treasury Rate


def portfolio_return(weights):
    """annualized portfolio return"""
    return returns.dot(weights.T).mean() * 365.25


def portfolio_risk(weights):
    """annualized portfolio risk"""
    return returns.dot(weights.T).std() * np.sqrt(365.25)


def minimized_sharpe(weights):
    """sharpe ratio * (-1)"""
    return (RISKFREE_RETURN - portfolio_return(weights)) / portfolio_risk(weights)


equal_weights = np.full(asset_qty, 1 / asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(asset_qty))

# Sequential Least Squares Programming
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
np.set_printoptions(suppress=True)

# %% Optimal Weights
optimal_weights = optimum['x']
optimal_weights = pd.Series(
    index=assets_close.columns, data=optimal_weights).to_frame('Opt. Weights')

# %% Tangency Portfolio
returns['TP'] = returns.dot(optimal_weights.squeeze())

# %% Covariance
covar = returns.cov() * 365.25


# %% Annualised Risk σ, Return, Sharpe & Variance


def annualised_risk_return(ret):
    """annualized risk and return"""
    stat = ret.agg(['mean', 'std']).T
    stat.columns = ['Return', 'Risk']
    stat.Return = stat.Return * 365.25  # Trading days + 1/4 leap day.
    # TODO Cap might be needed if annualized losses > 100% with log returns
    # stats.loc[stats.Return < -1, 'Return'] = -1
    stat.Risk = stat.Risk * np.sqrt(365.25)
    return stat


stats = annualised_risk_return(returns)
stats['Sharpe'] = stats['Return'].sub(RISKFREE_RETURN) / stats['Risk']
stats['Variance'] = np.power(stats.Risk, 2)
# Systematic & Unsystematic Risk in Variance
stats['Sys. Var.'] = covar.iloc[:, -1]
stats['Unsys. Var.'] = stats['Variance'].sub(stats['Sys. Var.'])
# Normalize == beta
stats['beta'] = stats['Sys. Var.'] / stats.loc['TP', 'Sys. Var.']
# Expected Return
stats['CAPM'] = RISKFREE_RETURN + \
    (stats.loc["TP", "Return"] - RISKFREE_RETURN) * stats.beta
# Alpha, asset below or above Security market line
stats['alpha'] = stats.Return - stats.CAPM

# %% MarketCap Portfolio
returns_mcap = returns.drop(columns=['TP'])
returns_mcap['MCAP'] = returns_mcap.mul(
    weights_cwi.shift().dropna()).sum(axis=1)
stats_mcap = annualised_risk_return(returns_mcap)
covar_mcap = returns_mcap.cov() * 365.25
stats_mcap['Sys. Var.'] = covar_mcap.iloc[:, -1]
stats_mcap['beta'] = stats_mcap['Sys. Var.'] / \
    stats_mcap.loc['MCAP', 'Sys. Var.']
