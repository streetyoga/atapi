### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a line-oriented command interpreter shell, which is also importable as an [Python](https://github.com/python/cpython) modlule, ready to be deployed on AWS or other cloud computing platforms.

Some example output:
```sh
python -m atapi
```
```sh
atf🖖 marketcap
                BNBUSDT       BTCUSDT       ETHUSDT     LTCUSDT     TRXUSDT      XRPUSDT
Date
2021-01-22   6676983304  627856464805  149200108943  9695518519  2663398041  13157541852
2021-01-23   6679807996  611330270204  149318731152  9696222829  2726790084  13133370302
2021-01-24   6829271739  614796850918  168553685405  9931462055  2795775542  13216520436
2021-01-25   6830643266  614688222495  159520241091  9653964285  2749163746  12935163587
2021-01-26   6831443323  618758357971  165341202327  9484930111  2749163746  12972387775
...                 ...           ...           ...         ...         ...          ...
2022-06-01  49048403290  568028122312  220050249106  4416017806  7789763399  19240554276
2022-06-02  50338291392  580354399059  222002673825  4542793437  7860613329  19603127535
2022-06-03  48754504735  566015256699  214865974418  4408974715  7560433361  18873146707
2022-06-04  49195352567  569137466256  218431903260  4486448712  7497973554  18974667219
2022-06-05  49113714080  569394172371  219077062823  4486448712  7502634733  19052016181

[500 rows x 6 columns]
```

### Milestones

Project is planed to be production ready in 2 years and shall remain written purly in Python:

- It uses the official lightweight [binance-connector-python](https://github.com/binance/binance-connector-python) and [requests](https://pypi.org/project/requests/) for Market Capitalisation data.
- [binance-futures-connector-python](https://github.com/binance/binance-futures-connector-python) will be implemented next.
- Consideration of [python-binance](https://github.com/sammchardy/python-binance) and [CCXT](https://github.com/ccxt/ccxt) library. CCXT supports hundreds of exchanges out of the box which should faciliate the implementation of arbitrage among different exchanges, but python-binance (which won a contest sponsored by binance) might have better api support for binance, i.e. implement NFT trading of the official binance API earlier, once it will be supported. The binance public API connector is very basic and a lot of work needs to be implemented in requests
- decision which algorithm to implement first, probably simple moving average with fixed values.
- Python script with API keys stored as environment variables. Binance spot testnet for balance, public api for statistics.
- Securing and encrypting API keys in external file.
- Reflection on different deployment possibilities beyond running it in a terminal window, like cron jobs, schtasks.exe, Power Automate...
- Implemented in [cmd](https://docs.python.org/3/library/cmd.html) from the Python Standard Library, partial support as Python module/REPL.  
  Other considerations:   
  [Python IDLE](https://github.com/python/cpython/tree/main/Lib/idlelib) plugin    
  [Python Fire](https://github.com/google/python-firegoogle) CLI interface   
  [rich](https://github.com/Textualize/rich) textual interface.  
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
