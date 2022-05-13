### Implementation

The project started out as a [JupyterLab Notebook](https://github.com/jupyterlab/jupyterlab) and turned into a [Python](https://github.com/python/cpython) file, ready to be deployed on AWS or other cloud computing platforms.

Some example output:
```python
>>> import atf as at
>>> at.marketcap
                BNBUSDT       BTCUSDT       ETHUSDT     LTCUSDT     TRXUSDT      XRPUSDT
Date
2022-05-04  65735310135  755714468999  355066761678  7476376241  8473727537  31234477683
2022-05-05  61800335037  695845650798  331794661223  6808842648  7319022602  28923677446
2022-05-06  25645914463  682395556019  320613813957  6717495946  8019111564  28101844725
2022-05-07  59677734362  675310697176  318440431119  6640202583  8197815899  28126016276
2022-05-08  58126603100  647946179505  304214433009  6605069236  8635739709  27371863897
2022-05-09  48395295390  572888939342  268925940329  5340268744  7141300159  23518918732
2022-05-10  52118010420  590492476695  336472264064  5529988817  7165847458  23514084422
2022-05-11  44346026410  553962856930  241486982000  6478589186  7165847458  23591433384
2022-05-12  43954161670  542404151983  235470333843  6458914512  7187449081  18979501529
```

### Milestones

Project is planed to be production ready in 2 years and shall remain written purly in Python:

- It uses the official lightweight [binance-connector-python](https://github.com/binance/binance-connector-python) and requests for Market Capitalisation data.
- Consideration of [python-binance](https://github.com/sammchardy/python-binance) and [CCXT](https://github.com/ccxt/ccxt) library. CCXT supports hundreds of exchanges out of the box which should faciliate the implementation of arbitrage among different exchanges, but python-binance (which won a contest sponsored by binance) might have better api support for binance, i.e. implement NFT trading of the official binance API earlier, once it will be supported. The binance public API connector is very basic and a lot of work needs to be implemented in requests
- decision which algorithm to implement first, probably simple moving average with fixed values.
- Python script with API keys stored as environment variables. Binance spot testnet only.
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
