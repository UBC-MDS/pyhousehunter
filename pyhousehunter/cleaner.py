# author: Junting He
# date: 2021-03-05

import pandas as pd
import numpy as np
import re
from geotext import GeoText
from operator import attrgetter

def data_cleaner(scraped_df):
    """A function to clean web-scraped data with Pandas and Regex.

    Parameters
    ----------
    scraped_df: pandas.core.frame.DataFrame
        A dataframe containing web-scraped data like listing url, price and house type. 

    Returns
    -------
    pandas.core.frame.DataFrame
        A cleaned dataframe containing ininformation like listing url, price, number of bedroom, area in sqft, and city.
    

    Examples
    --------
    >>> data_cleaner(scraped_df)
    """ 
    
    if not isinstance(scraped_df, pd.DataFrame):
        raise ValueError("Invalid input. Please enter a dataframe object")

    if scraped_df.empty:
        raise ValueError("The input dataframe is empty")

    if not 'price' in scraped_df.columns:
        raise ValueError("Missing price column in the input dataframe")

    if not 'house_type' in scraped_df.columns:
        raise ValueError("Missing house_type column in the input dataframe")

    if not 'listing_url' in scraped_df.columns:
        raise ValueError("Missing price listing_url column in the input dataframe")
   
    data = scraped_df.copy()
    
    ### convert the price column into numerice data types
    data['price'] = data['price'].str.replace('$', '', regex=False).str.replace(',', '')
    data['price'] = pd.to_numeric(data['price'])
    
    ### extract the information about the number of bedroom of the housing 
    data['num_bedroom'] = data['house_type'].str.extract(r'([0-9]+[b]{1}[r]{1})')
    data['num_bedroom'] = data['num_bedroom'].str.replace('br', '')
    data['num_bedroom'] = pd.to_numeric(data['num_bedroom'])
    data['num_bedroom'] = data['num_bedroom'].astype('Int64')

    ### extract the information about the area of the housing
    data['area_sqft'] = data['house_type'].str.extract(r'([0-9]+[f]{1}[t]{1}[2]{1})')
    data['area_sqft'] = data['area_sqft'].str.replace('ft2', '')
    data['area_sqft'] = pd.to_numeric(data['area_sqft'])
    data['area_sqft'] = data['area_sqft'].astype('Int64')
    
    ### extract the information about which city are the housing located in 
    data['city'] = data['listing_url'].str.extract(r'([d]{1}[/]{1}[a-z]+[-]{1})')
    data['city'] = data['city'].str.replace('d/', '', regex=False).str.replace('-', '').str.title()
    data['city'] = data['city'].apply(GeoText).apply(attrgetter('cities'))
    data['city']  = data['city'].apply(lambda x: np.nan if len(x)==0 else x).str[0]
    
    ### select the columns which are useful for future filtering
    cleaned_data = data[["listing_url", "price", "num_bedroom", "area_sqft", "city"]]
    
    ### activate the option to write results to CSV file

    return cleaned_data
