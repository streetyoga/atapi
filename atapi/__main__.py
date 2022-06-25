""" streetyoga.capital -
    A Quantitative Trading Software Company, presents:
    Algorithmic Trading API
"""
import sys
import cmd
from .comp import algo
from rich.console import Console
from rich.table import Table


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
    prompt = 'atf🖖  '

    @staticmethod
    def do_algorithmic_factory(arg):
        """Enters Factory"""
        AF.menu()

    @staticmethod
    def do_bye(arg):
        'Exits the API.'
        print('Thank you for using 𝔞𝔱𝔞𝔭𝔦')
        sys.exit()

    @staticmethod
    def do_servertime(arg):
        """Print Servertime."""
        table = Table('Server Time')
        table.add_row(str(algo_class.servertime()))
        console.print(table)

    @staticmethod
    def do_balance(arg):
        """Balance and kline fields for selected assets."""
        table = Table('Assets Balance')
        table.add_row(algo_class.balance().astype({'free': 'float', 'locked': 'float'}).to_string(
            float_format=lambda _: '{:.2f}'.format(_), index=False))
        console.print(table)

    @staticmethod
    def do_circulating_supply(arg):
        """Returns the circulating supply."""
        table = Table('Circulating Supply')
        table.add_row(algo_class.circulating_supply.to_string())
        console.print(table)

    @staticmethod
    def do_assets_close(arg):
        """Daily close price data for assets."""
        table = Table('Assets Close Prices')
        table.add_row(algo_class.assets_close.to_string())
        console.print(table)

    @staticmethod
    def do_marketcap(arg):
        """Simplified marketcap, only with last circulating supply."""
        table = Table('Market Cap')
        table.add_row(algo_class.marketcap.astype({symbol: 'float' for symbol in algo_class.symbols}).to_string(
                      float_format=lambda _: '{:.0f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_marketcap_summary(arg):
        """Daily marketcap summary of all assets."""
        table = Table('Crypto Market Cap')
        table.add_row(algo_class.marketcap_summary.to_string(
            float_format=lambda _: '{:.0f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_optimal_weights(arg):
        """Optimal weights calculated with sequential least squares programming."""
        table = Table('Optimal Weights')
        table.add_row(algo.optimal_weights.to_string(
            float_format=lambda _: '{:.0f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_returns(arg):
        """Daily logarithmic returns."""
        table = Table('Log Returns')
        table.add_row(algo.returns.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_normalized(arg):
        """Normalized Asset Returns Base 100."""
        table = Table(
            'Normalized Returns, Price Weighed, Equal Weighted, Capitalization Weighted')
        table.add_row(algo.normalized.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_weights_cwi(arg):
        """Capital weighted index."""
        table = Table('Capital Weighted Index')
        table.add_row(algo_class.weights_cwi.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_weights_pwi(arg):
        """Price weighted index."""
        table = Table('Price Weighted Index')
        table.add_row(algo_class.weights_pwi.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_weights_ewi(arg):
        """Equal weighted index."""
        table = Table('Equal Weighted Index')
        table.add_row(algo_class.weights_ewi.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_stats_index(arg):
        """Anualized risk / return of all assets."""
        table = Table('Anualized Risk & Return')
        table.add_row(algo_class.stats_index().to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_mean_returns(arg):
        """Daily Mean Returns Of All Assets."""
        table = Table('Daily Mean Returns')
        table.add_row(algo_class.mean_returns().to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_correlation(arg):
        """Correlation Coefficient"""
        table = Table('Correlation Coefficient')
        table.add_row(algo_class.correlation().to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_covariance(arg):
        """Covariance."""
        table = Table('Annualized Covariance')
        table.add_row(algo_class.covar.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_stats(arg):
        """Return, risk, sharpe, variance, systematic variance,
unsystematic variance, beta, CAPM, alpha."""
        table = Table('Anualized Modern Portfolio Theory Metrics')
        table.add_row(algo.stats.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)

    @staticmethod
    def do_stats_mcap(arg):
        """Marketcap portfolio."""
        table = Table('Market Cap Portfolio')
        table.add_row(algo.stats_mcap.to_string(
            float_format=lambda _: '{:.4f}'.format(_)))
        console.print(table)


if __name__ == '__main__':

    algo_class = algo.Algo()
    console = Console()
    shell = ATFShell()
    shell.cmdloop()
