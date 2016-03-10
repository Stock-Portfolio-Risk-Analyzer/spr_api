import datautils.yahoo_finance as yf
from flask import request, url_for
from flask.ext.api import FlaskAPI
from werkzeug.exceptions import BadRequestKeyError
app = FlaskAPI(__name__)


@app.route('/stock/<symbol>/current_price', methods=['GET'])
def current_price(symbol):
    return {'symbol': symbol, 'current_price': yf.get_current_price(symbol)}

@app.route('/stock/<symbol>/historical_prices', methods=['GET'])
def historical_prices(symbol):
    try:
        start_date = request.args['start_date']
        end_date = request.args['end_date']
    except BadRequestKeyError:
        pass
    print dict(yf.get_stock_data(symbol))
    return dict(yf.get_stock_data(symbol))

@app.route('/portfolio/', methods=['GET', 'POST'])
def portfolio(symbol):
    return "FOO"

if __name__ == '__main__':
    app.run(debug=True)