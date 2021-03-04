# author: Alex Truong Hai Yen
# date: 2021-03-04

from pyhousehunter import scraper
import pandas as pd

url = 'https://vancouver.craigslist.org/search/van/apa'
data = scraper.scraper(url = url, save_csv = True)
data_csv = pd.read_csv('raw.csv')

# Black box  test
def test_offline_output():
    assert data.equals(data_csv)
