"""Computation Module"""
from functools import cached_property
import numpy as np
import pandas as pd
import scipy.optimize as sco
from atapi.eps import Data


class Algo(Data):

    """Quantitative Analysis"""

    TD = 365.25  # Trading days + 1/4 leap day.

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
            self.circulating_supply[:3])
        return _marketcap

    @property
    def marketcap_summary(self):
        """Daily marketcap summary of all assets."""
        _marketcap_summary = self.marketcap().sum(
            axis=1).rename('Total MarketCap')
        return _marketcap_summary

    def weights_cwi(self):
        """Capital Weights"""
        _weights_cwi = self.marketcap().div(
            self.marketcap_summary, axis='index')
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

    def stats_index(self):
        """Annual risk & return of all assets."""
        _stats_index = np.log(self.normalized / self.normalized.shift()
                              ).dropna().agg(['mean', 'std']).T
        _stats_index.columns = ['Return', 'Risk']
        _stats_index['Return'] = _stats_index['Return'] * self.TD
        _stats_index['Risk'] = _stats_index['Risk'] * np.sqrt(self.TD)
        return _stats_index

    def mean_returns(self):
        """Daily Mean Returns Of All Assets."""
        _mean_returns = self.returns_with_tp.mean().rename('Mean Returns')
        return _mean_returns

    def correlation(self):
        """Correlation Coefficient"""
        _correlation = self.returns_with_tp.corr()
        return _correlation

    @property
    def covar(self):
        """Covariance"""
        _covar = self.returns_with_tp.cov() * self.TD
        return _covar

    def annual_risk_return(self, ret):
        """Annual Risk σ, Return"""
        stat = ret.agg(['mean', 'std']).T
        stat.columns = ['Return', 'Risk']
        stat.Return = stat.Return * self.TD
        # TODO Cap needed if annual losses > 100% even with log returns
        # stats.loc[stats.Return < -1, 'Return'] = -1
        stat.Risk = stat.Risk * np.sqrt(self.TD)
        return stat

    @property
    def returns(self):
        """ Daily Returns"""
        _returns = np.log(self.assets_close() /
                          self.assets_close().shift()).dropna()
        return _returns

    @property
    def normalized(self):
        """ Normalized Daily Returns"""
        _normalized = self.assets_close().div(
            self.assets_close().iloc[0]).mul(100)
        _normalized['PWI'] = self.assets_close().sum(
            axis=1).div(self.assets_close().sum(axis=1)[0]).mul(100)
        _normalized['EWI'] = 100
        _normalized.iloc[1:, -
                         1] = self.returns_index.Mean.add(1).cumprod().mul(100)
        _normalized['CWI'] = 100
        _normalized.iloc[1:, -1] = self.returns.mul(self.weights_cwi().shift().dropna()
                                                    ).sum(axis=1).add(1).cumprod().mul(100)
        return _normalized

    @property
    def returns_index(self):
        _returns_index = self.returns.copy()
        _returns_index['Mean'] = _returns_index.mean(axis=1)
        return _returns_index

    def portfolio_return(self, weights):
        """Annual Portfolio Return"""
        return self.returns.dot(weights.T).mean() * self.TD

    def portfolio_risk(self, weights):
        """Annual Portfolio Risk"""
        return self.returns.dot(weights.T).std() * np.sqrt(self.TD)

    def minimized_sharpe(self, weights):
        """Sharpe Ratio * (-1)"""
        return (self.rfr - self.portfolio_return(weights)) / self.portfolio_risk(weights)

    @cached_property
    def optimal_weights(self):
        """ Optimal Sharpe Ratio Portfolio (Tangency Portfolio) """
        equal_weights = np.full(self.asset_qty, 1 / self.asset_qty)
        constraint = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(self.asset_qty))
        optimum = sco.minimize(self.minimized_sharpe, equal_weights,
                               method='SLSQP', bounds=bounds, constraints=constraint)
        _optimal_weights = optimum['x']
        _optimal_weights = pd.Series(
            index=self.assets_close().columns, data=_optimal_weights, name='Optimal Weights')
        return _optimal_weights

    @property
    def returns_with_tp(self):
        """Returns including Tangency Portfolio"""
        _returns_with_tp = self.returns.copy()
        _returns_with_tp['TP'] = _returns_with_tp.dot(self.optimal_weights)
        return _returns_with_tp

    @property
    def stats(self):
        """ Annual Statistics """

        _stats = self.annual_risk_return(self.returns_with_tp)
        _stats['Sharpe'] = _stats['Return'].sub(
            self.rfr) / _stats['Risk']
        _stats['Var'] = np.power(_stats.Risk, 2)
        _stats['SysVar'] = self.covar.iloc[:, -1]
        _stats['UnsysVar'] = _stats['Var'].sub(_stats['SysVar'])
        _stats['beta'] = _stats['SysVar'] / \
            _stats.loc['TP', 'SysVar']  # Normalize == beta
        # Expected Return
        _stats['CAPM'] = self.rfr + \
            (_stats.loc["TP", "Return"] - self.rfr) * _stats.beta
        # Alpha, asset below or above Security market line
        _stats['alpha'] = _stats.Return - _stats.CAPM
        return _stats

    @property
    def returns_mcap(self):
        """ Marketcap Portfolio Returns"""
        _returns_mcap = self.returns.copy()
        _returns_mcap['MCAP'] = _returns_mcap.mul(
            self.weights_cwi().shift().dropna()).sum(axis=1)
        return _returns_mcap

    @property
    def stats_mcap(self):
        """ Marketcap Portfolio Statistics"""
        _stats_mcap = self.annual_risk_return(self.returns_mcap)
        covar_mcap = self.returns_mcap.cov() * self.TD
        _stats_mcap['SysVar'] = covar_mcap.iloc[:, -1]
        _stats_mcap['beta'] = _stats_mcap['SysVar'] / \
            _stats_mcap.loc['MCAP', 'SysVar']
        return _stats_mcap
