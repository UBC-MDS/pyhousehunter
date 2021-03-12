# author: Alex Truong Hai Yen
# date: 2021-03-04

from pyhousehunter import scraper
import pandas as pd
from pytest import raises
import regex as re
import random

url = "https://vancouver.craigslist.org/d/apartments-housing-for-rent/search/apa"


# Tests on input
def test_scraper_missing_required_input_url():
    """
    Test to confirm that TypeError is raised the required URL input is missing
    """
    with raises(TypeError):
        scraper.scraper(online=True)
        scraper.scraper()


def test_scraper_url_not_string():
    """
    Test to confirm that TypeError is raised the required URL input is not a string
    """
    with raises(TypeError):
        scraper.scraper(url=123, online=True)
        scraper.scraper(url=True, online=True)


def test_scraper_url_not_valid_craiglist_url():
    """
    Test to confirm that ValueError is raised the required URL input is \n
    not a valid Craiglist housing URL
    """
    with raises(ValueError):
        scraper.scraper(url="https://www.haha.com", online=True)  # fictitious website
        scraper.scraper(
            url="https://wiki.ubc.ca/Main_Page", online=True
        )  # wrong website


def test_scraper_online_not_boolean():
    """
    Test to confirm that TypeError is raised the optional input `online` is not a Boolean
    """
    with raises(TypeError):
        scraper.scraper(url=url, online=1)
        scraper.scraper(url=url, online="sunny")
        scraper.scraper(url=url, online="25yrs?")


# Tests on output

data = scraper.scraper(url=url, online=True)


def test_scraper_output_not_empty():
    """
    Test to confirm the output dataframe is not empty
    """
    assert data.empty is False


def test_scraper_output_shape():
    """
    Test to confirm the shape of the output dataframe is correct
    """
    assert data.shape == (120, 5)


def test_scraper_output_fields_is_string():
    """
    Test to confirm that the data type of each column of\n
    the output dataframe is a string
    """
    for i in random.sample(range(0, data.shape[0]), 5):
        for col in data.columns:
            assert type(data[col][i]) == str
            assert type(data[col][i]) == str
            assert type(data[col][i]) == str


def test_scraper_output_listing_url_is_url():
    """
    Test that the data in the `listing_url` column contains the correct URL
    """
    regex = r"(http|https):\/\/vancouver.craigslist.org.*"
    for i in random.sample(range(0, data.shape[0]), 5):
        listing_url = data["listing_url"][i]
        assert re.search(regex, listing_url) is not None


def test_scraper_output_price_contain_dollar_sign():
    """
    Test to confirm that the data in the `price` column contains the dollar sign ($)
    """
    regex = r"\$"
    for i in random.sample(range(0, data.shape[0]), 5):
        price = data["price"][i]
        assert re.search(regex, price) is not None


local_data = scraper.scraper(url=url, online=False)
# for local data only
toy_data = pd.read_csv("tests/toy.csv")
toy_data["price"] = toy_data["price"].astype(str).str.strip()
toy_data["listing_id"] = toy_data["listing_id"].astype(str)


def test_scraper_output_match_toy_data():
    """
    Test to confirm that the scraped data frame contains data in toy dataset
    """
    for i in range(0, toy_data.shape[0]):
        lst_id = toy_data.listing_id.tolist()
        assert local_data.loc[local_data["listing_id"] == lst_id[i], :].equals(
            pd.DataFrame(toy_data.iloc[i]).T
        )