### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a line-oriented command interpreter shell, which is also importable as an [Python](https://github.com/python/cpython) modlule, ready to be deployed on AWS or other cloud computing platforms.

Some example output:
```sh
python -m atapi
```
```sh
atf🖖 marketcap
==========  ============  =============  ============  ===========  ===========  ===========
Date             BNBUSDT        BTCUSDT       ETHUSDT      LTCUSDT      TRXUSDT      XRPUSDT
==========  ============  =============  ============  ===========  ===========  ===========
2021-02-04    9136963193   704366408120  193398455975  10230271989   3062563654  21534434428
2021-02-05   11053932846   730178603448  208369331709  10934057158   3353090840  21860266930
2021-02-06   11892376440   747278291350  203177036401  10970727327   3244837080  21419377847
2021-02-07   11160667005   739817320132  195331628482  10631528263   3328109203  20231104420
2021-02-08   13035609164   884349061580  212121746806  11796511328   3739843592  21802255209
...                 ...           ...           ...         ...         ...          ...
2022-06-14   36410765425   422131930726  146521143738   3254477509   5143441496  15537472725
2022-06-15   38141501360   430661942319  149989946066   3571815511   5830899138  16610689571
2022-06-16   34320820145   389044311143  129504377603   3157865718   5480230973  15141059295
2022-06-17   35235171205   390331507456  131739343184   3356730866   5541297197  15518135484
2022-06-18   34794323372   390064533406  130932137611   3364488017   5557951622  15484295313
==========  ============  =============  ============  ===========  ===========  ===========
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
