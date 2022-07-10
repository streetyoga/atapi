from comp.algo import Algo
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def api():
    return jsonify(Servertime=algo.servertime())


@app.route('/api')
def circulating_supply():
    parsed = json.loads(algo.circulating_supply.to_json(orient='index'))
    return jsonify(Symbols=parsed)


@app.route('/api/symbols/<string:symbol>')
def get_cs_by_symbol(symbol):
    df = algo.circulating_supply
    if symbol in df.index:
        return jsonify({symbol: df.loc[symbol]})
    return jsonify({'message': f'Symbol {symbol!r} does not exist.'})


@app.route('/api/rfr')
def risk_free_return():
    return jsonify({"Risk Free Return": algo.rfr})


algo = Algo()
if __name__ == "__main__":
    app.run(port=47491)
