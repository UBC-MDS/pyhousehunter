# Python House Hunter 

[![build](https://github.com/UBC-MDS/pyhousehunter/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/pyhousehunter/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/UBC-MDS/pyhousehunter/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyhousehunter) ![Release](https://github.com/elabandari/pyhousehunter/workflows/Release/badge.svg)[![Documentation Status](https://readthedocs.org/projects/pyhousehunter/badge/?version=latest&style=plastic)](https://pyhousehunter.readthedocs.io/en/latest/)


Python package for searching for housing on Craigslist.

-   Author: Ela Bandari, Junting He, Ling (Elina) Lin, Alex Truong


## Overview

Hunting for rentals can be an exhausting and frustrating experience in Canada, but this process can be made easy with a simple installation of our package. This Python package intends to facilitate the house hunting process by scraping the listing information from Craigslist and orgaCancel Changesnizing the extracted data for the user. Instead of having to manually go on the website to catch up with individual new listings, the user will be updated through email with new results as per their selection criteria. 


## Functions

| Function Name | Input | Output | Description |
|-----------|------------|---------------|------------------|
| scraper | url | Pandas DataFrame | Scrape data from rental websites into a Pandas DataFrame|
| data_cleaner | Pandas DataFrame |  Pandas DataFrame | Clean the extracted data |
| data_filter | Pandas DataFrame, min_price, max_price, sqrt_ft, num_bathroom, num_bedroom, neighbourhood | Pandas DataFrame | Filter the cleaned data set based on user inputs|
| send_email | Pandas DataFrame, email address | csv file | Send the organized listing information to user email |



## Our Package in the Python Ecosystem

To the best of our knowledge, there is currently no existing Python package that simplifies the entire rental searching process with such a  comprehensive functionality. This package takes care of all the steps including scraping rental websites, processing the data, and emailing users with the updated listing information. Plenty of general scraper packages exist in the Python ecosystem, but they lack the focus on house rental and emailing functionality, such as the following two: https://github.com/narfman0/craigslist-scraper and https://github.com/juliomalegria/python-craigslist. 



## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pyhousehunter
```

## Features
The pyhousehunter package contains the following four functions:
- `scraper()`
A function to scrape housing data from a given Craiglist url
-`data_cleaner()`
A function to clean web-scraped data with Pandas and Regex.
- `data_filter()`
Function to filter the given dataframe as per selection inputs
-`send_email()`
A function to email search filtered search results.
## Dependencies

- python = "^3.8"
- beautifulsoup4 = "^4.9.3"
- requests = "^2.25.1"
- pandas = "^1.2.3"
- regex = "^2020.11.13"
- geotext = "^0.4.0"

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://pyhousehunter.readthedocs.io/en/latest/

## Contributors
The names and GitHub handles of core development team is listed below.

Name|Github Handle
------|----------
Alex Truong Hai Yen|athy9193
Ela Bandari|elabandari
Elina Lin|elina-linglin
Junting He|juntinghe

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/pyhousehunter/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
