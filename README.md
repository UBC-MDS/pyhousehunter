# Python House Hunter 

![](https://github.com/elabandari/pyhousehunter/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/elabandari/pyhousehunter/branch/main/graph/badge.svg)](https://codecov.io/gh/elabandari/pyhousehunter) ![Release](https://github.com/elabandari/pyhousehunter/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyhousehunter/badge/?version=latest)](https://pyhousehunter.readthedocs.io/en/latest/?badge=latest)

Python package for searching for housing on Craigslist.

-   Author: Ela Bandari, Junting He, Ling (Elina) Lin, Alex Truong


## Overview

Hunting for rental can be an exhausting and frustrating experience in Canada, but this process can be made easy with a simple installation of our package. This Python package intends to facilitate house hunting by scraping the listing information from Craigslist and organizing the extracted data for the users. Instead of having to manually go on the website to catch up with individual new listings, the users will be updated through email with new listings as per their selection criteria. 

## Functions

| Function Name | Input | Output | Description |
|-----------|------------|---------------|------------------|
| web_scraper | url | csv file | Scrape data from rental websites into a csv file.|
| data_cleaner | csv file location | csv file | Clean the extracted data |
| data_filter | csv file, min_price, max_price, sqrt_ft, no_bathroom, no_bedroom, neighbourhood | csv file | Filter the cleaned data set based on user inputs|
| emailer | csv file, email address | csv file | Send the organized listing information to user email |



## Our Package in the Python Ecosystem

To the best of our knowledge, there is currently no existing Python package that simplifies the entire rental searching process with such a  comprehensive functionality. This package takes care of all the steps including scraping rental websites, processing the data, and emailing users with the updated listing information. Plenty of general scraper packages exist in the Python ecosystem, but they lack the focus on house rental and emailing functionality, such as the following two: https://github.com/narfman0/craigslist-scraper and https://github.com/juliomalegria/python-craigslist. 



## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pyhousehunter
```

## Features

- TODO

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://pyhousehunter.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/elabandari/pyhousehunter/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
