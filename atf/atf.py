#!/usr/bin/env python
# coding: utf-8

# %% Algorithmic Trading Framework
import os
import pandas as pd
import numpy as np
import scipy.optimize as sco
from binance.spot import Spot as Client
import requests

mc_base = 'https://www.binance.com'
mc_path = '/exchange-api/v2/public/asset-service/product/get-products'
mc_url = mc_base + mc_path  # Only for Circulating Supply Data
pd.set_option('display.max_rows', 80)
pd.options.display.float_format = '{:.4f}'.format
# pd.reset_option('display.float_format')

# Synchronize with timeserver if time is off, ommit base_url to default to api.binance.com
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'), base_url='https://testnet.binance.vision')
print('Server Time')
print(pd.to_datetime(client.time()['serverTime'], unit='ms'), '\n')

# %%
balance = pd.json_normalize(client.account()['balances'])
print(f'Balance\n{balance}\n')

# %% All kline fields for selected assets
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LTCUSDT', 'TRXUSDT', 'XRPUSDT']
columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
           'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
# assets= [pd.DataFrame((c[4] for c in client.klines(symbol, "1d")),columns=[symbol]) for symbol in symbols]
assets = pd.concat(([pd.DataFrame(client.klines(symbol, "1d"), columns=columns)
                   for symbol in symbols]), axis=1, keys=symbols)
# Circulating Supply
response = requests.get(mc_url)
data = response.json()
circulating_supply = [item['cs'] for item in data['data']
                      for symbol in symbols if item['s'] == symbol]

# %% Close Price Data for Assets
assets = assets.swaplevel(axis=1)  # Swapping levels for easier selection
assets = assets.set_index(pd.to_datetime(assets['Close time', 'BTCUSDT'], unit='ms').dt.strftime(
    '%Y-%m-%d'))  # Set close time as index, needs improvement
assets.index.name = 'Date'
assets_close = assets["Close"].copy().astype(float)  # Daily close prices
print(f'Close Price\n{assets_close}\n')
# Simplified MarketCap, only last Circulating Supply taken into account.
marketcap = assets_close.mul(circulating_supply)
print(f'Market Capitalisation\n{marketcap}\n')
# %% Daily Returns
# Risk not accurate with arithmetic returns for mean daily losses > 0.274%
# returns = assets_close.pct_change().dropna()
returns = np.log(assets_close / assets_close.shift(1)).dropna()
print(f'Daily Mean Returns\n{returns.mean(axis=0)}\n')

# %% Correlation Coefficient
print(f'Correlation Coefficient\n{returns.corr()}\n')

# %%
riskfree_return = 0.031  # 5 Year Treasury Rate, but testnet resets every month
# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
asset_qty = len(assets_close.columns)


def portfolio_return(weights):
    return returns.dot(weights.T).mean() * 365.25


def portfolio_risk(weights):
    return returns.dot(weights.T).std() * np.sqrt(365.25)


def minimized_sharpe(weights):
    return (riskfree_return - portfolio_return(weights)) / portfolio_risk(weights)


equal_weights = np.full(asset_qty, 1 / asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for x in range(asset_qty))

# Sequential Least Squares Programming
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
np.set_printoptions(suppress=True)
optimum

# %% Optimal Weights
optimal_weights = optimum['x']
optimal_weights = pd.Series(index=assets_close.columns, data=optimal_weights)
print(f'Optimal Weights\n{optimal_weights}\n')

# %%
portfolio_return(optimal_weights)

# %%
portfolio_risk(optimal_weights)

# %%
-minimized_sharpe(optimal_weights)

# %% Tangency Portfolio
returns['TP'] = returns.dot(optimal_weights)
print(f'Daily Returns, including Tangency Portfolio\n{returns}\n')

# %% Covariance
COV = returns.cov() * 365.25
print(f'Covariance\n{COV}\n')

# %%
COV.iloc[:-1, -1].dot(optimal_weights)

# %%
COV.iloc[-1, -1]

# %% Annualised Risk σ, Return, Sharpe & Variance


def annualised_risk_return(returns):
    stats = returns.agg(['mean', 'std']).T
    stats.columns = ['Return', 'Risk']
    stats.Return = stats.Return * 365.25  # Trading days + 1/4 leap day.
    # stats.loc[stats.Return < -1, 'Return'] = -1  # Set losses > 100% to -100%
    stats.Risk = stats.Risk * np.sqrt(365.25)
    return stats


stats = annualised_risk_return(returns)
stats['Sharpe'] = stats['Return'].sub(riskfree_return) / stats['Risk']
stats['Variance'] = np.power(stats.Risk, 2)
# Systematic & Unsystematic Risk in Variance
stats['Sys. Var.'] = COV.iloc[:, -1]
stats['Unsys. Var.'] = stats['Variance'].sub(stats['Sys. Var.'])
# Normalize == beta
stats['beta'] = stats['Sys. Var.'] / stats.loc['TP', 'Sys. Var.']
# Expected Return
stats["CAPM"] = riskfree_return + \
    (stats.loc["TP", "Return"] - riskfree_return) * stats.beta
# Alpha, asset below or above Security market line
stats['alpha'] = stats.Return - stats.CAPM
print(f'Key Measurements\n{stats}')
