### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a line-oriented command interpreter shell in [Python](https://github.com/python/cpython).   
Future Implementations will be ready to be deployed on AWS or other cloud computing platforms.

Some example output:
```sh
python -m atapi
```
```sh
atf🖖 marketcap
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Market Cap                                                                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                 BNBUSDT       BTCUSDT      ETHUSDT     LTCUSDT     TRXUSDT     XRPUSDT │
│ Date                                                                                   │
│ 2021-02-05  11053932846  730206095840 208390333334 10935301434  3353031782 21860266930 │
│ 2021-02-06  11892376440  747306427573 203197514693 10971975776  3244779928 21419377847 │
│ 2021-02-07  11160667005  739845175437 195351316031 10632738112  3328050585 20231104420 │
│ 2021-02-08  13035609164  884382358737 212143126638 11797853750  3739777721 21802255209 │
│ 2021-02-09  17527277108  885251010583 214443773179 12800050676  4263457630 23028719686 │
    ...           ...           ...           ...         ...         ...          ...
│ 2022-06-15  38141501360  430678157430 150005063610  3572221978  5830796437 16610689571 │
│ 2022-06-16  34320820145  389058959284 129517430399  3158225077  5480134449 15141059295 │
│ 2022-06-17  35235171205  390346204061 131752621243  3357112856  5541199597 15518135484 │
│ 2022-06-18  32165564075  361778523741 120623940583  3327491272  5633722549 14865503618 │
│ 2022-06-19  31218557620  346166056268 114897779224  3219584073  5568956483 14556107770 │
└────────────────────────────────────────────────────────────────────────────────────────┘
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
- Implemented in [cmd](https://docs.python.org/3/library/cmd.html) from the Python Standard Library and the [rich](https://github.com/Textualize/rich) textual interface.   
  Other considerations:   
  [Python IDLE](https://github.com/python/cpython/tree/main/Lib/idlelib) plugin    
  [Python Fire](https://github.com/google/python-firegoogle) CLI interface   

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
