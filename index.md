### Implementation

The project will start out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) which can be exported to a flat [Python](https://github.com/python/cpython) file, ready to be deployed on AWS or other cloud computing platforms.


### Milestones

Project is planed to be production ready in 2 years and shall remain written purly in Python:


- Consideration between [python-binance](https://github.com/sammchardy/python-binance), the official lightweight library [binance-connector-python](https://github.com/binance/binance-connector-python) and [CCXT](https://github.com/ccxt/ccxt) library. CCXT has the advantage to support hundreds of exchanges out of the box which should faciliate the implementation of arbitrage among different exchanges, but python-binance might have better api support for binance, i.e. implement NFT trading of the official binance API earlier, once it will be supported. The binance public API connector has the disadvantage of being simple, but this could also be an advantage.

- decision which algorithm to implement first, probably simple moving average with fixed values.
- a rudementary implementation in a Jupyter notebook, with api keys stored in it, which can be exported to a python script. Binance futures market only.
- Securing and encrypting API keys in external file.
- Reflection on different deployment possibilities beyond running it in a terminal window, like cron jobs, Windows Task Scheduler, Power Automate...
- Considerations how to evolve the interface from a Jupyter notebook, options are [Python Fire](https://github.com/google/python-firegoogle) for a CLI interface, and [rich](https://github.com/Textualize/rich) for a textual interface. A pure implementation in the Python REPL or as [Python IDLE](https://github.com/python/cpython/tree/main/Lib/idlelib) plugin is also considered.
- Adding a second algorithm. 
- Switching between implemented algorithms, including backtest, forward test and going from test network to main, no leverage.
- slowly implementing leverage starting with 2x only.
- Switching between Hedge-mode and One-way mode on binance.
- Expanding to binance spot market, nft market. 
- Implementing arbitrage trading with other exchanges.
- Implementation of GUI, hot candidates are [tkinter](https://github.com/python/cpython/tree/main/Lib/tkinter) with heavy skinning to give it a modern look and [voila](https://github.com/voila-dashboards/voila).

This project is meant to sharpen my Python programming skills, no guaranties or responsibilites from outcomes by using my software will be covered by me.

### Support or Contact

You can contact me on [Linkedin](https://www.linkedin.com/in/streetyogi/) to give feedback and share ideas, or right here on github.
