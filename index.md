### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a [Python](https://github.com/python/cpython) file, ready to be deployed on AWS or other cloud computing platforms.


### Milestones

Project is planed to be production ready in 2 years and shall remain written purly in Python:

- It uses the official lightweight [binance-connector-python](https://github.com/binance/binance-connector-python) and requests for Market Capitalisation data.
- Consideration of [python-binance](https://github.com/sammchardy/python-binance) and [CCXT](https://github.com/ccxt/ccxt) library. CCXT supports hundreds of exchanges out of the box which should faciliate the implementation of arbitrage among different exchanges, but python-binance (which won a contest sponsored by binance) might have better api support for binance, i.e. implement NFT trading of the official binance API earlier, once it will be supported. The binance public API connector is very basic and a lot of work needs to be implemented in requests
- decision which algorithm to implement first, probably simple moving average with fixed values.
- Python script with API keys stored as environment variables. Binance spot testnet only.
- Securing and encrypting API keys in external file.
- Reflection on different deployment possibilities beyond running it in a terminal window, like cron jobs, Windows Task Scheduler, Power Automate...
- Implementation as Python REPL, considerations to implement as [Python IDLE](https://github.com/python/cpython/tree/main/Lib/idlelib) plugin, [Python Fire](https://github.com/google/python-firegoogle) CLI interface, or [rich](https://github.com/Textualize/rich) textual interface.
- Adding a second algorithm, first draft on how to create own algorithms and trading strategies in the framework, either domain specific or in pure Python.
- Switching between implemented algorithms, including backtest, forward test and going from test network to main, no leverage.
- slowly implementing leverage starting with 2x only.
- Switching between Hedge-mode and One-way mode on binance.
- Expanding to binance future market, nft market. 
- Implementing arbitrage trading with other exchanges.
- If neccessary implementation of GUI  
   [tkinter](https://github.com/python/cpython/tree/main/Lib/tkinter) with skinning for modern look  
   [Dash](https://github.com/plotly/dash)  
   [Streamlit](https://github.com/streamlit/streamlit)  
   [Flask](https://github.com/pallets/flask/)   
   [Django](https://github.com/django/django)  
   
This project is meant to sharpen my Python programming skills.

### Support or Contact

You can contact me on [Linkedin](https://www.linkedin.com/in/streetyogi/) to give feedback and share ideas, or right here on github.
