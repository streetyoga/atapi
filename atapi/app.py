from comp.algo import Algo
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def api():
    return jsonify(Servertime=algo.servertime())


@app.route('/api')
def circulating_supply():
    parsed = json.loads(algo.circulating_supply().to_json(orient='index'))
    return jsonify(Symbols=parsed)


@app.route('/api/rfr')
def risk_free_return():
    return jsonify({"Risk Free Return": algo.rfr})


algo = Algo()
if __name__ == "__main__":
    app.run(port=47491)
