from simple_colors import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os, time
from pprint import pprint

os.system("cls")
starting_location = input("Enter starting location: ")
budget = int(input("Enter your max budget: "))

def humaniser(inp):
    output = ""
    for i in inp:
        # elif i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        #     output += i + " "
        if i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
            output += " " + i
        elif i == ",":
            pass
        else:
            output += i
    return output

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(f'https://www.google.com/flights?q=from+{starting_location}/')
button = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button")
button.click()
time.sleep(10)
text = driver.page_source
driver.quit()

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6757.105 Safari/537.36 Brave/4.0.2164.182"}
# text = requests.get(f'https://www.google.com/flights?q=from+{starting_location}/', headers=headers).text
soup = BeautifulSoup(text, 'lxml')
locs = soup.find("div", style="z-index: 3; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px; touch-action: pan-x pan-y;").text.strip().split("A$")
locs.pop(0)
for i in locs:
    try:
        if int(humaniser(i).split(" ")[0]) < budget/2:
            print("You could travel to: $" + humaniser(i))
    except Exception:
        pass
    
