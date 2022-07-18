""" streetyoga.capital -
    A Quantitative Trading Software Company, presents:
    Algorithmic Trading API
"""
import sys
import cmd
from rich.console import Console
from rich.table import Table
from atapi.cmp import Algo


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
: a : algorithm
: s : strategy
: c : create
: ↩ : back
Choose: """
        while user_input := input(menu):
            {'a': lambda: None,
             's': lambda: None,
             'c': AF.create
             }.get(user_input, lambda: print('Invalid Input'))()


class ATFShell(cmd.Cmd):
    """Line-oriented command interpreter"""
    intro = 'Welcome to the Algorithmic Trading API. Type help/? for commands.\n'
    prompt = '𝔞𝔱𝔞𝔭𝔦     \r'

    @staticmethod
    def do_algorithmic_factory(arg):
        """Enters Factory"""
        AF.menu()

    @staticmethod
    def do_quit(arg):
        'Exits the API.'
        print('Thank you for using 𝔞𝔱𝔞𝔭𝔦')
        sys.exit()

    @staticmethod
    def format_table(name, data):
        """Format Tables"""
        table = Table(name)
        table.add_row(data)
        console.print(table)

    def do_servertime(self, arg):
        """Print Servertime."""
        self.format_table('Server Time', str(algo.servertime()))

    def do_circulating_supply(self, arg):
        """Returns the circulating supply."""
        self.format_table('Circulating Supply', algo.circulating_supply.to_string(
            float_format=lambda _: f'{_:,.0f}'))

    def do_assets_close(self, arg):
        """Daily close price data for assets."""
        self.format_table('Assets Close Prices',
                          algo.assets_close().to_string())

    def do_marketcap(self, arg):
        """Simplified marketcap, only with last circulating supply."""
        self.format_table('Market Cap', algo.marketcap().to_string(
            float_format=lambda _: f'{_:,.0f}'))

    def do_marketcap_summary(self, arg):
        """Daily marketcap summary of all assets."""
        self.format_table('Crypto Market Cap', algo.marketcap_summary.to_string(
            float_format=lambda _: f'{_:,.0f}'))

    def do_optimal_weights(self, arg):
        """Optimal weights calculated with sequential least squares programming."""
        self.format_table('Optimal Weights', algo.optimal_weights.to_string(
            float_format=lambda _: f'{_:.0f}'))

    def do_returns(self, arg):
        """Daily logarithmic returns."""
        self.format_table('Log Returns', algo.returns_with_tp.to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_normalized(self, arg):
        """Normalized Asset Returns Base 100."""
        self.format_table(
            'Normalized Returns, Price Weighed, Equal Weighted, Capitalization Weighted',
            algo.normalized.to_string(
                float_format=lambda _: f'{_:.4f}'))

    def do_weights_cwi(self, arg):
        """Capital weighted index."""
        self.format_table('Capital Weighted Index', algo.weights_cwi().to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_weights_pwi(self, arg):
        """Price weighted index."""
        self.format_table('Price Weighted Index', algo.weights_pwi.to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_weights_ewi(self, arg):
        """Equal weighted index."""
        self.format_table('Equal Weighted Index', algo.weights_ewi.to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_stats_index(self, arg):
        """Anualized risk / return of all assets."""
        self.format_table('Anualized Risk & Return', algo.stats_index().to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_mean_returns(self, arg):
        """Daily Mean Returns Of All Assets."""
        self.format_table('Daily Mean Returns', algo.mean_returns().to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_correlation(self, arg):
        """Correlation Coefficient"""
        self.format_table('Correlation Coefficient', algo.correlation().to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_covariance(self, arg):
        """Covariance."""
        self.format_table('Annualized Covariance', algo.covar.to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_stats(self, arg):
        """Return, risk, sharpe, variance, systematic variance,
unsystematic variance, beta, CAPM, alpha."""
        self.format_table('Anualized Modern Portfolio Theory Metrics', algo.stats.to_string(
            float_format=lambda _: f'{_:.4f}'))

    def do_stats_mcap(self, arg):
        """Marketcap portfolio."""
        self.format_table('Market Cap Portfolio', algo.stats_mcap.to_string(
            float_format=lambda _: f'{_:.4f}'))


if __name__ == '__main__':
    algo = Algo()
    console = Console()
    shell = ATFShell()
    shell.cmdloop()
