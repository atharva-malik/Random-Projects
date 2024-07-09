import requests
import json

last_money = 0
portfolio_value = 0
spare_money = 0
username = ""
portfolio = []
with open('Python\Stocks\Stock Trading Game\save.json', 'r') as f:
    pf = json.load(f)
    portfolio_value = pf['portfolio_value']
    username = pf['username']
    portfolio = pf['portfolio']
    spare_money = pf['spare_money']
    last_money = portfolio_value + spare_money

if username == "":
    print("Please enter a username")
    while username == "":
        username = input("> ")
    portfolio = []
    portfolio_value = 0
    spare_money = 10000
    last_money = portfolio_value + spare_money
else:
    print(f"Welcome back {username}")

api_key = 'ENTER_YOUR_API_KEY_HERE'

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

def addStock(symbol, name, amount, price):
    global portfolio
    for i in portfolio:
        if i["symbol"] == symbol and i["price"] == price:
            i["amount"] += amount
            if i["amount"] == 0:
                portfolio.remove(i)
            return
    portfolio.append({"symbol": symbol, "name": name, "amount": amount, "price": price})

def get_symbol(company):
    try:
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        data = data['bestMatches'][0]
        return data['1. symbol'], data['2. name']
    except Exception:
        return None

print("The market is open!")
while True:
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
    if portfolio_value < 0:
        spare_money += portfolio_value
        portfolio_value = 0
    if portfolio_value+spare_money <= 0:
        print("You have gone bankrupt. Game Over!")
        username = ""
        portfolio_value = 0
        spare_money = 10000
        portfolio = []
        break
    elif portfolio_value+spare_money >= 1000000:
        print("Your portfolio has grown by 100 times! You're rich. Restart from the beginning for another challenge!")
        username = ""
        portfolio_value = 0
        spare_money = 10000
        portfolio = []
        break
    
    #! Handle user input
    if op == 1:
        company = input("Enter a stock symbol/company name: ")
        symbol, name = get_symbol(company)
        price = round(float(get_current_stock_price(symbol)),2)
        if price is None:
            print("Error retrieving stock price. Please try again later.")
            continue
        if input(f"Did you mean {symbol}, {name} (y/N): ").lower() != "y":
            continue
        print(f"The current price of {name} is {price}, you have {spare_money} spare money.")
        while True:
            try:
                print("How many stocks do you want? ")
                op = int(input("> "))
                if op < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        if price * op > spare_money:
            print("You don't have enough money to buy that many stocks.")
            print(f"You have {spare_money} and you can't afford {op} stocks")
            print(f"Try sell some stocks before buying that many stocks of {name}")
            continue
        print(f"You bought {op} of {symbol} at {price} each. You have {round((spare_money-price*op), 2)} left.")
        portfolio_value += price * op
        portfolio_value = round(portfolio_value, 2)
        spare_money -= price * op
        spare_money = round(spare_money, 2)
        addStock(symbol=symbol, name=name, amount=op, price=price)
    elif op == 2:
        if len(portfolio) == 0:
            print("You have no stocks to sell.")
            continue
        print("Enter the number of the stock you want to sell:")
        for i, stock in enumerate(portfolio):
            print(f"{i+1}. {stock['amount']} x {stock['symbol']} - {stock['name']} which you bought at {stock['price']}")
        while True:
            try:
                index = int(input("> ")) - 1
                if index < 0 or index >= len(portfolio):
                    raise ValueError
                stock = portfolio[index]
                symbol = stock['symbol']
                name = stock['name']
                og_price = stock['price']
                price = get_current_stock_price(symbol)
                print(f"Currently, {symbol} is going for {price}")
                print("How many stocks do you want to sell?")
                while True:
                    try:
                        op = int(input("> "))
                        if op < 0 or op > stock['amount']:
                            raise ValueError
                        break
                    except ValueError:
                        print(f"Invalid input. Please enter a number between 0 and {stock['amount']}.")
                        continue
                addStock(symbol=symbol, name=name, amount=-op, price=og_price)
                portfolio_value -= og_price * op
                portfolio_value = round(portfolio_value, 2)
                spare_money += og_price * op
                spare_money += ((price-og_price) * op) - ((price-og_price) * op)*0.0075
                spare_money = round(spare_money, 2)
                print(f"You sold {op} of {symbol} at {price} each. A transaction fee of 0.75% has been deducted.\nYou have {spare_money+portfolio_value} left.")
                break
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {len(portfolio)}.")
                continue
    elif op == 3:
        for i, stock in enumerate(portfolio):
            print(f"{i+1}. {stock['symbol']} - {stock['name']}: {stock['amount']}")
        print(f"Your current portfolio value is {portfolio_value}\nYour spare money is {spare_money}")
    elif op == 4:
        print("The market closes!")
        print(f"You started with {last_money}, and now have {portfolio_value+spare_money}")
        if last_money > portfolio_value+spare_money:
            print(f"You lost {round((last_money-(portfolio_value+spare_money))/last_money, 2)}% of your initial money.")
        else:
            print(f"You have made a profit of {round(((portfolio_value+spare_money)-last_money)/last_money, 2)}% on your initial money.")
        break

#? END OF SESSION SAVE
with open('Python\Stocks\Stock Trading Game\save.json', 'w') as f:
    json.dump({'username': username, 'portfolio_value': portfolio_value, 'portfolio': portfolio, 'spare_money': spare_money}, f)