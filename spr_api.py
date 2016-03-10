from flask import Flask, jsonify
from datautils.yahoo_finance import get_current_price
from flask.ext.api import FlaskAPI
app = FlaskAPI(__name__)

@app.route('/<symbol>', methods=['GET'])
def get_price(symbol):
    return {'symbol': symbol, 'price': get_current_price(symbol)}

if __name__ == '__main__':
    app.run(debug=True)