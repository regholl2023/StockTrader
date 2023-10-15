from flask import Flask, jsonify
import alpaca_trade_api
from dotenv import load_dotenv
import os

app = Flask(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
#API Key
API_KEY_ID = os.environ.get('ALPACA_API_KEY_ID')
API_KEY_SECRET = os.environ.get('ALPACA_API_KEY_SECRET')

# Init Alpaca API. Use paper trading endpoint for testing.
# api = alpaca_trade_api.REST('ALPACA_API_KEY_ID', 'ALPACA_API_KEY_SECRET', base_url='https://paper-api.alpaca.markets')  


@app.route('/')
def index():
    # Get account information
    account_data = api.get_account()._raw
    # Get cash balance
    cash_balance = float(account_data['cash'])
    
    # Create a welcome message
    welcome_message = "Welcome to the Automated Stock Trading Platform!"
    
    # Combine the welcome message and cash balance as HTML
    page_content = f"<h1>{welcome_message}</h1><p>Cash Balance: ${cash_balance:.2f}</p>"
    return page_content

# @app.route('/account')
# def account_info():
#     return jsonify(api.get_account()._raw)

if __name__ == '__main__':
    app.run(debug=True)