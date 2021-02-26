# author: Alex Truong Hai Yen
# date: 2021-02-25

"""""Scrape housing data from a give craiglist url and export result to csv file.

Usage: pyhousehunter/scraper.py --url=<url> 

Options:
--url=<url>              The chosen craiglist url 
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
from docopt import docopt

opt = docopt(__doc__)


### PART1: create soup object from the url
def make_soup(url):
    """Function to scrape housing data from a given craiglist url

    Parameters
    ----------
    url : url
        The given craiglist url

    Returns
    -------
    bs4.BeautifulSoup
        The soup object from scraping the url
    """
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


### PART2: extracting information from scrape results and export to csv
def extractor(soup): 
    """Extract information from the soup object and export result to csv

    Parameters
    ----------
    soup : bs4.BeautifulSoup
        The soup object from scraping the url

    Returns
    -------
        a csv file contained listing information such as price, house type and neighborhood

    """
       
    listings = soup.find_all('div', attrs = {'class': 'result-info'})
    data = []

    # extract data from soup object
    for i in range(len(listings)):
        listing_id = listings[i].find('a').get('data-id')
        listing_url = listings[i].find('a').get('href')
        price= listings[i].find('span', attrs = {'class': 'result-price'}).text
        house = listings[i].find('span', attrs = {'class': 'housing'})
        neighborhood = listings[i].find('span', attrs = {'class': 'result-hood'})

        data.append((listing_id, listing_url, price, house, neighborhood))
    
    # writing results to CSV file
    with open('raw.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for listing_id, listing_url, price, house, neighborhood in data:
            writer.writerow([listing_id, listing_url, price, house, neighborhood])


### PART3: the main function      
def main(url):
    soup = BeautifulSoup(open("pyhousehunter/temp/van_housing_listings.html"), "html.parser") # local scraping
    #soup = make_soup(url) # online scraping
    data = extractor(soup)


if __name__ == "__main__":
  main(opt["--url"])
  

