"""
Task
Copy the company name into the sheet.
Copy the website link into the sheet
Copy the CEO's name into the sheet
Copy the CEO's LinkedIn Profile link into the sheet.
"""
from bs4 import BeautifulSoup
import requests
import brotli
import json
import time
import random

# Load data from API retrieved on scraper_api.py
with open('./site.json','r',  encoding="utf8") as response:
    response_py = json.load(response)

# Get the result of the query
response_list = list(response_py.values())
companies = response_list[0][0]['hits']

# Instantiate 3 list to store slugs, names and websites of each company, and the final dict.
slugs = []

names = []

websites = []

companies_data = {}

for company in companies:# This for loop take each company of the JSON file and save the requested data.
    slug = company['slug']
    name = company['_highlightResult']["name"]["value"] # Copy the company name into the sheet.
    website = company['_highlightResult']["website"]["value"]# Copy the website link into the sheet

    slugs.append(slug) #I store in memory to loop over this list and get access to each particular company details.

    companies_data[slug] = {'Company name':name,'Website':website}

print('json done')

log_dict = {} #Store any failure in the for loop

for slug in slugs:

    print(slug)

    url=f'https://www.ycombinator.com/companies/{slug}'

    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
    session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    session.headers['Accept-Encoding'] = 'gzip, deflate, br'
    session.headers['Accept-Lenguaje'] = 'en-US,en;q=0.9'

    response = session.get(url)
    # Check response headers
    encoding = response.encoding
    # This site has a method of encryption particular.
    html_get = response.content.decode(encoding)

    bs_parsed = BeautifulSoup(html_get, "html.parser")
    # Get all CEO's data
    leaders = bs_parsed.findAll('div', class_='leading-snug')

    name_ls = []

    linked_ls = []
    
    for leader in leaders: # This loop loops through the data for each CEO and stores it in the company_dict.
        details = leader.findAll('div')
        try:
            name = details[0].text 
        except:#if no name displayed i store the slung
            log_dict[slug] = 'CEO Name'

        try:
            linkedin = details.find('a', {'title':'LinkedIn profile'}).get('href')
        except:#if no linkedin displayed i store the slung
            log_dict[slug] = 'CEO Linkedin'

        name_ls.append(name)
        linked_ls.append(linkedin)
        
        companies_data[slug]['CEO Name'] = name_ls
        companies_data[slug]['LinkedIn'] = linked_ls
    
    time.sleep(random.randint(1,5))

#Now with all the data stored in company_dict it is stored as a JSON
with open('./companies.json', 'w') as companies_json:
     json.dump(companies_data, companies_json, indent=4)


with open('./log_failed.json', 'w') as logs:
    json.dump(log_dict, logs, indent=4)
