from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

### PART1: scraping directly from the web
url = 'https://vancouver.craigslist.org/search/van/apa' 

def online_scraper(url):
    headers = {
        'DNT': '1',
        'Referer': 'https://vancouver.craigslist.org/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    page = requests.get(url, headers = headers)

    # checking scrape status
    if page.status_code == 200:
        print("OK")
    else: 
        print(page.status_code)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    return soup



### PART2: extracting information from scrape results

#soup = online_scraper(url) # online scraping
soup = BeautifulSoup(open("../van_housing_listings.html"), "html.parser") # local scraping
listings = soup.find_all('div', attrs = {'class': 'result-info'})
data = []

for i in range(len(listings)):
    listing_id = listings[i].find('a').get('data-id')
    listing_url = listings[i].find('a').get('href')
    price= listings[i].find('span', attrs = {'class': 'result-price'}).text
    house = listings[i].find('span', attrs = {'class': 'housing'})
    neighborhood = listings[i].find('span', attrs = {'class': 'result-hood'})

    data.append((listing_id, listing_url, price, house, neighborhood))


### PART2B: preprocessing (to be abstracted to another scrip and work directly with csv)

# price
#processed_price = int("".join(price.split('$')[1].split(',')))
#print(processed_price+1) # test for numeric output


### PART3: writing results to CSV file

with open('raw.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for listing_id, listing_url, price, house, neighborhood in data:
        writer.writerow([listing_id, listing_url, price, house, neighborhood])

