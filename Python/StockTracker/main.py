from simple_colors import *
from bs4 import BeautifulSoup
import requests
import os

os.system("cls")

print('Name the person you want to track: ')
person_to_track = input('> ')
print(f'Trying to find information about {person_to_track}')
# person_to_track = "Warren Buffett"
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
    for thing in holdings_soup.find_all('div', id="wrap"):
        print(thing)
        print("\n\n\n")
else:
    print(red("Superinvestor not found! Recheck the given name!", "bold"))

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# for job in jobs:
#     company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
#     skills = job.find('span', class_='srp-skills').text.replace(' ', '')
#     published_date = job.find('span', class_='sim-posted').text
#     more_info = job.header.h2.a['href']
#     if "few" in published_date:
#         if unfamiliar_skill not in skills:    
#             print(f"Company Name: {company_name.strip()}\nRequired Skills: {skills.strip()}\nMore Info: {more_info}\n")