### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a [Python](https://github.com/python/cpython) file, ready to be deployed on AWS or other cloud computing platforms.

Some example output:
```python
>>> import atf
>>> atf.marketcap
                BNBUSDT       BTCUSDT       ETHUSDT      LTCUSDT     TRXUSDT      XRPUSDT
Date
2021-01-07   7114434976  751003782105  148041159042  11910426821  3006676303  15657847046
2021-01-08   6915759553  772916093070  147081508791  12110164714  2953245868  15485262175
2021-01-09   7159352472  763496425717  154220871552  12466739051  3285486028  15672349977
2021-01-10   6923449898  726582619808  151592106696  11961064597  3181539545  15223725997
2021-01-11   6231857615  674292505364  131379020051   9766760984  2814326736  13895257577
...                 ...           ...           ...          ...         ...          ...
2022-05-17  49995409745  579836052491  252690172861   5148173860  7018816249  21174278324
2022-05-18  46974785707  546894927819  231465464982   4641796104  6897383442  19607961845
2022-05-19  50142359022  577442044957  244088370801   5070810592  7147049293  20328274053
2022-05-20  49342301845  556145091060  236779800188   4824654738  6920698541  19825505800
2022-05-21  51171003965  564117688465  239869052129   4944216153  7276253800  20134901648

[500 rows x 6 columns]
```

### Milestones

Project is planed to be production ready in 2 years and shall remain written purly in Python:

- It uses the official lightweight [binance-connector-python](https://github.com/binance/binance-connector-python) and requests for Market Capitalisation data.
- Consideration of [python-binance](https://github.com/sammchardy/python-binance) and [CCXT](https://github.com/ccxt/ccxt) library. CCXT supports hundreds of exchanges out of the box which should faciliate the implementation of arbitrage among different exchanges, but python-binance (which won a contest sponsored by binance) might have better api support for binance, i.e. implement NFT trading of the official binance API earlier, once it will be supported. The binance public API connector is very basic and a lot of work needs to be implemented in requests
- decision which algorithm to implement first, probably simple moving average with fixed values.
- Python script with API keys stored as environment variables. Binance spot testnet for balance, public api for statistics.
- Securing and encrypting API keys in external file.
- Reflection on different deployment possibilities beyond running it in a terminal window, like cron jobs, schtasks.exe, Power Automate...
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
