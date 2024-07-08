import requests
import json

portfolio_value = 0
username = ""
portfolio = []
with open('Python\Stocks\Stock Trading Game\save.json', 'r') as f:
    pf = json.load(f)
    portfolio_value = pf['portfolio_value']
    username = pf['username']
    portfolio = pf['portfolio']

if username == "":
    print("Please enter a username")
    while username == "":
        username = input("> ")
    portfolio = []
    portfolio_value = 0
else:
    print(f"Welcome back {username}")

api_key = 'ENTER_YOUR_API_KEY_HERE'
api_key = 'Q38KXAMESHWB6PGC'

def get_current_stock_price(symbol):
    function = 'GLOBAL_QUOTE'
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        # Check for error message from the API
        if 'Error Message' in data:
            return None

        # Extract the current stock price
        price = data['Global Quote']['05. price']
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving stock price: {e}")
        return None

def get_symbol(company):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    data = data['bestMatches'][0]
    return data['1. symbol'], data['2. name']


#? END OF SESSION SAVE
with open('Python\Stocks\Stock Trading Game\save.json', 'w') as f:
    json.dump({'username': username, 'portfolio_value': portfolio_value, 'portfolio': portfolio}, f)