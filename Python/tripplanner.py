from simple_colors import *
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

os.system("cls")
starting_location = input("Enter starting location: ")

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(f'https://www.google.com/flights?q=from+{starting_location}/')
button = driver.find_element_by_id("loadMoreButton")
button.click()
driver.implicitly_wait(30)
text = driver.page_source
driver.quit()

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6757.105 Safari/537.36 Brave/4.0.2164.182"}
# text = requests.get(f'https://www.google.com/flights?q=from+{starting_location}/', headers=headers).text
soup = BeautifulSoup(text, 'lxml')
print(soup.prettify())