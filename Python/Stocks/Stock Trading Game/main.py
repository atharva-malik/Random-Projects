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

        # Extract the current stock price
        price = data['Global Quote']['05. price']
        return price
    except Exception:
        print(f"Error retrieving stock price: {e}")
        return None

def get_symbol(company):
    try:
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        data = data['bestMatches'][0]
        return data['1. symbol'], data['2. name']
    except Exception:
        return None

while True:
    print("Welcome! The market is open!")
    print("1. Buy a stock\n2. Sell a stock\n3. View portfolio\n4. Exit")
    
    #! Get proper input
    try:
        op = int(input("> "))
        if op < 1 or op > 4:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    
    #! Check for win/loss
    if portfolio_value <= 0:
        print("You have gone bankrupt. Game Over!")
        username = ""
        portfolio_value = 10000
        portfolio = []
        break
    elif portfolio_value >= 1000000:
        print("Your portfolio has grown by 100 times! You're rich. Restart from the beginning for another challenge!")
        username = ""
        portfolio_value = 10000
        portfolio = []
        break
    
    #! Handle user input
    if op == 1:
        company = input("Enter a stock symbol/company name: ")
        symbol, name = get_symbol(company)
        if input().lower() != "y":
            continue
        print(f"You bought {name} for {symbol}")
        price = get_current_stock_price(symbol)
        if price is None:
            print("Error retrieving stock price. Please try again later.")
            continue
        portfolio_value += price
        portfolio.append({'symbol': symbol, 'name': name, 'price': price})
    elif op == 2:
        # if len(portfolio) == 0:
        #     print("You have no stocks to sell.")
        #     continue
        # print("Enter the symbol of the stock you want to sell:")
        # for i, stock in enumerate(portfolio):
        #     print(f"{i+1}. {stock['symbol']} - {stock['name']}")
        # try:
        #     index = int(input("> ")) - 1
        #     if index < 0 or index >= len(portfolio):
        #         raise ValueError
        #     symbol = portfolio[index]['symbol']
        #     name = portfolio[index]['name']

#? END OF SESSION SAVE
# with open('Python\Stocks\Stock Trading Game\save.json', 'w') as f:
#     json.dump({'username': username, 'portfolio_value': portfolio_value, 'portfolio': portfolio}, f)