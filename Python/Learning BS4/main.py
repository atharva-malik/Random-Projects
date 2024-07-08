from bs4 import BeautifulSoup
import requests

text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    skills = job.find('span', class_='srp-skills').text
    published_date = job.find('span', class_='sim-posted').replace(')', '')
    if "few" in published_date:
        print(f"Company Name: {company_name.strip()}\nRequired Skills: {skills.strip()}\n")