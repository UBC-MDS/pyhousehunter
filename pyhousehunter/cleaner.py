import pandas as pd
import numpy as np
import re

def data_cleaner(raw_data_filepath, seperator=','):
    """A function to clean web-scraped data with Pandas and Regex.

    Parameters
    ----------
    raw_data_filepath : str
        The path of the raw data spreadsheet.
    seperator: str, default ‘,’
        Delimiter to use.

    Returns
    -------
    cleaned_df: DataFrame
        A cleaned DataFrame object ready for data filtering and analysis.
    

    Examples
    --------
    >>> data_cleaner("data/raw.csv")
    """ 

