#!/usr/bin/env python
# coding: utf-8

# %% Algorithmic Trading Framework
import os
import pandas as pd
import numpy as np
import scipy.optimize as sco
from binance.spot import Spot as Client
pd.set_option('display.max_rows', 80)
# pd.reset_option('display.float_format')

# Synchronize with timeserver if time is off, ommit base_url to default to api.binance.com
client = Client(os.getenv('BINANCE_API_KEY'), os.getenv(
    'BINANCE_API_SECRET'), base_url='https://testnet.binance.vision')
print(pd.to_datetime(client.time()['serverTime'], unit='ms'))

# %%
balance = pd.json_normalize(client.account()['balances'])
print(balance)

# %% All kline fields for selected assets
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LTCUSDT', 'TRXUSDT', 'XRPUSDT']
columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
           'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
# assets= [pd.DataFrame((c[4] for c in client.klines(symbol, "1d")),columns=[symbol]) for symbol in symbols]
assets = pd.concat(([pd.DataFrame(client.klines(symbol, "1d"), columns=columns)
                   for symbol in symbols]), axis=1, keys=symbols)

# %% Close Price Data for Assets
assets = assets.swaplevel(axis=1)  # Swapping levels for easier selection
assets = assets.set_index(pd.to_datetime(assets['Close time', 'BTCUSDT'], unit='ms').dt.strftime(
    '%Y-%m-%d'))  # Set close time as index, needs improvement
assets.index.name = 'Close time'
assets_close = assets["Close"].copy().astype(float)  # Daily close prices
print(assets_close)


# %% Daily Returns
returns = assets_close.pct_change().dropna()
# Maybe better to use logarithimc returns np.log(assets_close / assets_close.shift(1)).dropna().mean()
print(returns.mean(axis=0))

# %%
print(returns)

# %% Test
lreturns = np.log(assets_close / assets_close.shift(1)).dropna()
lreturns.mean()

# %% Test
lreturns

# %% Correlation Coefficient
print(returns.corr())

# %% Test
lreturns.corr()

# %%
riskfree_return = 0.031  # 5 Year Treasury Rate, but testnet resets every month
# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
asset_qty = len(assets_close.columns)


def portfolio_return(weights):
    return returns.dot(weights.T).mean() * 365.25


def portfolio_risk(weights):
    return returns.dot(weights.T).std() * 365.25


def minimized_sharpe(weights):
    return (riskfree_return - portfolio_return(weights)) / portfolio_risk(weights)


equal_weights = np.full(asset_qty, 1 / asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for x in range(asset_qty))

# Sequential Least Squares Programming
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
np.set_printoptions(suppress=True)
print(optimum)  # No surprise with that 157.07$ BNB outlier

# %% Test
riskfree_return = 0.031  # 5 Year Treasury Rate, but testnet resets every month
# Optimal Sharpe Ratio Portfolio (Tangency Portfolio)
asset_qty = len(assets_close.columns)


def portfolio_return(weights):
    return lreturns.dot(weights.T).mean() * 365.25


def portfolio_risk(weights):
    return lreturns.dot(weights.T).std() * 365.25


def minimized_sharpe(weights):
    return (riskfree_return - portfolio_return(weights)) / portfolio_risk(weights)


equal_weights = np.full(asset_qty, 1 / asset_qty)
constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for x in range(asset_qty))

# Sequential Least Squares Programming
optimum = sco.minimize(minimized_sharpe, equal_weights,
                       method='SLSQP', bounds=bounds, constraints=constraint)
np.set_printoptions(suppress=True)
optimum  # No surprise with that 157.07$ BNB outlier

# %% Optimal Weights
pd.options.display.float_format = '{:.4f}'.format
optimal_weights = optimum['x']
optimal_weights = pd.Series(index=assets_close.columns, data=optimal_weights)
print(optimal_weights)

# %%
print(portfolio_return(optimal_weights))

# %%
print(portfolio_risk(optimal_weights))

# %%
print(-minimized_sharpe(optimal_weights))

# %% Tangency Portfolio
returns['TP'] = returns.dot(optimal_weights)
print(returns)

# %% Test
# Tangency Portfolio
lreturns['TP'] = lreturns.dot(optimal_weights)
lreturns

# %% Covariance
COV = returns.cov() * 365.25
print(COV)

# %% Test
# Covariance
COV = lreturns.cov() * 365.25
COV

# %%
COV.iloc[:-1, -1].dot(optimal_weights)

# %%
COV.iloc[-1, -1]

# %% Annualised Risk σ, Return, Sharpe & Variance


def annualised_risk_return(returns):
    stats = returns.agg(['mean', 'std']).T
    stats.columns = ['Return', 'Risk']
    # Crypto exchanges trade every day, including leap days.
    stats.Return = stats.Return * 365.25
    stats.loc[stats.Return < -1, 'Return'] = -1  # Set losses > 100% to -100%
    stats.Risk = stats.Risk * np.sqrt(365.25)  # maybe switch to log returns
    return stats


# Risk may not be accurate for mean daily losses > 0.274% ()
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
print(stats)

# %% Test
# Annualised Risk σ, Return, Sharpe & Variance


def annualised_risk_return(lreturns):
    stats = lreturns.agg(['mean', 'std']).T
    stats.columns = ['Return', 'Risk']
    # Crypto exchanges trade every day, including leap days.
    stats.Return = stats.Return * 365.25
    # stats.loc[stats.Return < -1, 'Return'] = -1 # Set losses > 100% to -100%
    stats.Risk = stats.Risk * np.sqrt(365.25)  # maybe switch to log returns
    return stats


# Risk may not be accurate for mean daily losses > 0.274% ()
stats = annualised_risk_return(lreturns)
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
stats
