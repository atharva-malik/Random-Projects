"""
This Project is a simple Stock Report Generator for different super investors
as listed on the Dataroma website. It uses BeautifulSoup to scrape the data
and then prints it to the console in a simple and readable format.
"""

from simple_colors import *
from bs4 import BeautifulSoup
import requests
from rich.table import Table
from rich import print as p
import os

os.system("cls")

print('Name the person you want to track: ')
person_to_track = input('> ')
print(f'Trying to find information about {person_to_track}')
# person_to_track = "Warren Buffett"

table = Table(title="Stock Report for " + person_to_track)
table.add_column("Stock", justify="left")
table.add_column("% of\nPortfolio", justify="center")
table.add_column("Recent Activity", justify="right")

#? This is an interesting workaround to dataroma blocking requests
base_link = "https://www.dataroma.com"
link = base_link
# member_code = ""
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6757.105 Safari/537.36 Brave/4.0.2164.182"}
text = requests.get('https://www.dataroma.com/m/home.php', headers=headers).text
soup = BeautifulSoup(text, 'lxml')
people = soup.find_all('ul')[1]
for person in people:
    if person_to_track in person.text:
        link += person.a["href"]
        # member_code = person.a["href"][person.a["href"].find("m=")+2:]
        break

if link != base_link:
    print(green("Superinvestor found! Getting information", "bold"))
    holdings_link = link
    holdings_soup = BeautifulSoup(requests.get(holdings_link, headers=headers).text, 'lxml')
    
    # buys_link = base_link + "/m/m_activity.php?m=" + member_code + "&type=b"
    # buys_soup = BeautifulSoup(requests.get(link, headers=headers).text, 'lxml')
    
    # sells_link = base_link + "/m/m_activity.php?m=" + member_code + "&type=s"
    # sells_soup = BeautifulSoup(requests.get(link, headers=headers).text, 'lxml')
    stocks = []
    percentages = []
    recent_activities = []
    items_in_the_table = holdings_soup.find('table', id="grid").tbody
    for item in items_in_the_table.find_all('tr'):
        # print(item.find_all('td')[0])
        stock = item.find_all('td')[1].text
        percentage = item.find_all('td')[2].text
        recent_activity = item.find_all('td')[3].text
        # if (recent_activity[0].lower() == 'r'):
        #     stocks.append(red(stock))
        #     percentages.append(red(percentage))
        #     recent_activities.append(red(recent_activity))
        # elif (recent_activity[0].lower() == 'a'):
        #     stocks.append(green(stock))
        #     percentages.append(green(percentage))
        #     recent_activities.append(green(recent_activity))
        # else:
        stocks.append(stock)
        percentages.append(percentage)
        recent_activities.append(recent_activity)
    for stock, percentage, recent_activity in zip(stocks, percentages, recent_activities):
        table.add_row(stock, percentage, recent_activity)
    
    p(table)
    
else:
    print(red("Superinvestor not found! Recheck the given name!", "bold"))
