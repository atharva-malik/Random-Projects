from bs4 import BeautifulSoup
import requests

print('Put one skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    published_date = job.find('span', class_='sim-posted').text
    more_info = job.header.h2.a['href']
    if "few" in published_date:
        if unfamiliar_skill not in skills:    
            print(f"Company Name: {company_name.strip()}\nRequired Skills: {skills.strip()}\nMore Info: {more_info}\n")