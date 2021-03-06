# author: Elina (Ling) Lin
# date: 2021-03-05

from pyhousehunter import filter
import pandas as pd
from pytest import raises
import regex as re
import random


toy_data = pd.read_csv('tests/cleaned_toy_data.csv', index_col=0)
empty_data = toy_data[toy_data["price"] == -1]

# Tests on input
def test_filter_price_range():
    """
    Test to ensure min_price and max_price 
    non-negative and min_price <= max_price
    """
    with raises(ValueError):
        filter.data_filter(toy_data, -10, 1000, 500, 2, "Vancouver")
        filter.data_filter(toy_data, 1000, -10, 500, 2, "Vancouver")


def test_filter_price_type():
    """
    Test to ensure the max_price or min_price are both either int or float.
    """
    with raises(TypeError):
        filter.data_filter(toy_data, "hello", 2000, 500, 2, "Vancouver")


def test_filter_sqrt_ft_type():
    """
    Test to confirm that sqrt_ft is of type integer.
    """
    with raises(TypeError):
        filter.data_filter(toy_data, 1000, 2000, "hellp", 2, "Vancouver")


def test_filter_num_bedroom_type():
    with raises(TypeError):
        filter.data_filter(toy_data, 1000, 2000, 500, 2.3, "Vancouver")

def test_filter_num_bedroom_range():
    with raises(ValueError):
        filter.data_filter(toy_data, 1000, 2000, 500, -3, "Vancouver")


def test_filter_city_name_type():
    with raises(TypeError):
        filter.data_filter(toy_data, 1000, 2000, 500, 2, 10)


# Test for output
def test_filter_output_city_case_insensitive():
    assert filter.data_filter(toy_data, 1000, 2000, 600, 1, "burnaby").equals(toy_data.iloc[[0], :])

def test_filter_output_empty_result():
    print(empty_data)
    print(filter.data_filter(toy_data, 1000, 2000, 500, 1, "richmond").equals(empty_data))
    assert filter.data_filter(toy_data, 1000, 2000, 500, 1, "richmond").equals(empty_data)

def test_filter_output_column_with_nan():
    assert filter.data_filter(toy_data, 1000, 1500, 400, 2, "Surrey").equals(toy_data.iloc[[1], :])