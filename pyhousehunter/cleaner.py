# author: Junting He
# date: 2021-03-05

import pandas as pd
import numpy as np
import re
from geotext import GeoText
from operator import attrgetter

def data_cleaner(raw_data_filepath, save_to_csv = False):
    """A function to clean web-scraped data with Pandas and Regex.

    Parameters
    ----------
    raw_data_filepath : str
        The relative path of the raw data CSV file.
    save_to_csv: bool
        Whether to export the cleaned data into a CSV file (default = False)

    Returns
    -------
    pandas.core.frame.DataFrame
        A cleaned dataframe ready for filtering and analysis. 
        A csv containing the cleaned dataframe could also be exported with `save_to_csv` option is True.
    

    Examples
    --------
    >>> data_cleaner("raw.csv")
    """ 
    
    ### read the data into a panda dataframe and make a copy of it
    df = pd.read_csv(raw_data_filepath)
    data = df.copy()
    
    ### convert the price column into numerice data types
    data['price'] = data['price'].str.replace('$', '', regex=False).str.replace(',', '')
    data['price'] = pd.to_numeric(data['price'])
    
    ### extract the information about the number of bedroom of the housing 
    data['bed_num'] = data['house_type'].str.extract(r'([0-9]+[b]{1}[r]{1})')
    data['bed_num'] = data['bed_num'].str.replace('br', '')
    data['bed_num'] = pd.to_numeric(data['bed_num'])

    ### extract the information about the area of the housing
    data['area(ft2)'] = data['house_type'].str.extract(r'([0-9]+[f]{1}[t]{1}[2]{1})')
    data['area(ft2)'] = data['area(ft2)'].str.replace('ft2', '')
    data['area(ft2)'] = pd.to_numeric(data['area(ft2)'])
    
    ### extract the information about which city are the housing located in 
    data['city'] = data['listing_url'].str.extract(r'([d]{1}[/]{1}[a-z]+[-]{1})')
    data['city'] = data['city'].str.replace('d/', '', regex=False).str.replace('-', '').str.title()
    data['city'] = data['city'].apply(GeoText).apply(attrgetter('cities'))
    data['city']  = data['city'].apply(lambda x: np.nan if len(x)==0 else x).str[0]
    
    ### drop the column which is not useful for future filtering
    data.drop(columns=['listing_id', 'house_type', 'neighborhood'], inplace=True)
    
    ### activate the option to write results to CSV file
    if save_to_csv:
        data.to_csv('cleaned_data.csv', index_label = "serial_no")

    return data
