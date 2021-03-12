# author: Junting He
# date: 2021-03-06

from pyhousehunter import cleaner
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pytest import raises

# Tests on input


def test_cleaner_scraped_df_is_dataframe():
    """
    Test to confirm that ValueError is raised when the required scraped_df \n
    input is not a dataframe
    """
    with raises(ValueError):
        cleaner.data_cleaner("raw.html")
        cleaner.data_cleaner(123)


def test_cleaner_scraped_df_not_empty():
    """
    Test to confirm the output dataframe is not empty
    """
    with raises(ValueError):
        cleaner.data_cleaner(
            pd.DataFrame({"price": [], "house_type": [], "listing_url": []})
        )


def test_cleaner_scraped_df_not_missing_price():
    """
    Test to confirm that ValueError is raised when the scraped_df input \n
    is missing the price column
    """
    with raises(ValueError):
        cleaner.data_cleaner(
            pd.DataFrame([[1, 2]], columns=["house_type", "listing_url"])
        )


def test_cleaner_scraped_df_not_missing_house_type():
    """
    Test to confirm that ValueError is raised when the scraped_df input \n
    is missing the house_type column
    """
    with raises(ValueError):
        cleaner.data_cleaner(pd.DataFrame([[1, 2]], columns=["price", "listing_url"]))


def test_cleaner_scraped_df_not_missing_listing_url():
    """
    Test to confirm that ValueError is raised when the scraped_df input \n
    is missing the listing_url column
    """
    with raises(ValueError):
        cleaner.data_cleaner(pd.DataFrame([[1, 2]], columns=["price", "house_type"]))


# Tests on output

data = cleaner.data_cleaner(pd.read_csv("tests/toy.csv"))


def test_cleaner_output_not_empty():
    """
    Test to confirm the output dataframe is not empty
    """
    assert data.empty is False


def test_cleaner_output_shape():
    """
    Test to confirm the shape of the output dataframe is correct
    """
    assert data.shape == (3, 5)


def test_cleaner_output_price_is_numeric():
    """
    Test to confirm that the data type of price column of the output dataframe is numeric
    """
    assert is_numeric_dtype(data["price"])


def test_cleaner_output_num_bedroom_is_numeric():
    """
    Test to confirm that the data type of num_bedroom column of \n
    the output dataframe is numeric
    """
    assert is_numeric_dtype(data["num_bedroom"])


def test_cleaner_area_sqft_is_numeric():
    """
    Test to confirm that the data type of area_sqft column of \n
    the output dataframe is numeric
    """
    assert is_numeric_dtype(data["area_sqft"])


def test_cleaner_output_city_is_string():
    """
    Test to confirm that the data type of city column of \n
    the output dataframe is numeric
    """
    assert is_string_dtype(data["city"])


def test_cleaner_output_match_expected():
    """
    Test to confirm that the cleaned data frame matches cleaned toy data
    """
    assert data.equals(
        pd.read_csv(
            "tests/cleaned_toy_data.csv",
            dtype={"num_bedroom": "Int64", "area_sqft": "Int64"},
        )
    )
