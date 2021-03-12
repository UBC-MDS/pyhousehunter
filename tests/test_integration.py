from pyhousehunter import scraper
from pyhousehunter import cleaner
from pyhousehunter import filter
from pyhousehunter import emailer
import pandas as pd
from pytest import raises
import regex as re
import random


url = "https://vancouver.craigslist.org/d/apartments-housing-for-rent/search/apa"

scraped_data = scraper.scraper(url)
cleaned_data = cleaner.data_cleaner(scraped_data)
filtered_data = filter.data_filter(cleaned_data, 1500, 2000, 500, 1, "Vancouver")


def test_scrape_clean_filter():
    assert (
        int(filter.data_filter(cleaned_data, 10000, 15000, 500, 4, "")["price"])
        == 14000
    )


def test_full_integration():
    assert (
        emailer.send_email(
            email_recipient="elabandari@gmail.com",
            filtered_data=filtered_data,
            email_subject="Integration Test Success!",
        )
        == None
    )
