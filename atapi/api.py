from comp.algo import Algo
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def api():
    return jsonify({'Servertime': Algo.servertime()})


app.run(port=47491)
