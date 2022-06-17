""" streetyoga.capital -
    A Quantitative Trading Software Company, presents:
    Algorithmic Trading API
"""
import sys
import cmd
from .comp import algo


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
        print('Thank you for using ATF')
        sys.exit()

    @staticmethod
    def do_servertime(arg):
        """Print Servertime."""
        print(algo_class.servertime())

    @staticmethod
    def do_balance(arg):
        """Balance and kline fields for selected assets."""
        print(algo_class.balance())

    @staticmethod
    def do_circulating_supply(arg):
        """Returns the circulating supply."""
        print(algo_class.circulating_supply)

    @staticmethod
    def do_assets_close(arg):
        """Daily close price data for assets."""
        print(algo_class.assets_close)

    @staticmethod
    def do_marketcap(arg):
        """Simplified marketcap, only with last circulating supply."""
        print(algo_class.marketcap)

    @staticmethod
    def do_marketcap_summary(arg):
        """Daily marketcap summary of all assets."""
        print(algo_class.marketcap_summary())

    @staticmethod
    def do_optimal_weights(arg):
        """Optimal weights calculated with sequential least squares programming."""
        print(algo.optimal_weights)

    @staticmethod
    def do_returns(arg):
        """Daily logarithmic returns."""
        return print(algo.returns)

    @staticmethod
    def do_normalized(arg):
        """Normalized assets."""
        print(algo.normalized)

    @staticmethod
    def do_weights_cwi(arg):
        """Capital weighted index."""
        print(algo_class.weights_cwi)

    @staticmethod
    def do_weights_pwi(arg):
        """Price weighted index."""
        print(algo_class.weights_pwi())

    @staticmethod
    def do_weights_ewi(arg):
        """Equal weighted index."""
        print(algo_class.weights_ewi())

    @staticmethod
    def do_stats_index(arg):
        """Anualized risk / return of all assets."""
        print(algo_class.stats_index())

    @staticmethod
    def do_mean_returns(arg):
        """Daily Mean Returns Of All Assets."""
        print(algo_class.mean_returns())

    @staticmethod
    def do_correlation(arg):
        """Correlation Coefficient"""
        print(algo_class.correlation())

    @staticmethod
    def do_covariance(arg):
        """Covariance."""
        print(algo_class.covar)

    @staticmethod
    def do_stats(arg):
        """Return, risk, sharpe, variance, systematic variance,
unsystematic variance, beta, CAPM, alpha."""
        print(algo.stats)

    @staticmethod
    def do_stats_mcap(arg):
        """Marketcap portfolio."""
        print(algo.stats_mcap)


if __name__ == '__main__':
    algo_class = algo.Algo()
    shell = ATFShell()
    shell.cmdloop()
