from flask import Flask, jsonify
from alpaca_trade_api import REST
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
#API Keys
API_KEY_ID = os.environ.get('ALPACA_API_KEY_ID')
API_KEY_SECRET = os.environ.get('ALPACA_API_KEY_SECRET')

# Initialize Alpaca API
api = REST('ALPACA_API_KEY_ID', 'ALPACA_API_KEY_SECRET', base_url='https://paper-api.alpaca.markets')  # Use paper trading endpoint for testing

@app.route('/')
def index():
    return "Welcome to the Automated Stock Trading Platform!"

@app.route('/account')
def account_info():
    return jsonify(api.get_account()._raw)

if __name__ == '__main__':
    app.run(debug=True)