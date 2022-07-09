from comp.algo import Algo
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def api():
    return jsonify(Servertime=Algo.servertime())


@app.route('/api')
def circulating_supply():
    parsed = json.loads(Algo.circulating_supply().to_json(orient='index'))
    return jsonify(Symbols=parsed)


if __name__ == "__main__":
    app.run(port=47491)
