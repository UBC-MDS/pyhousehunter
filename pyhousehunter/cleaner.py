import pandas as pd
import numpy as np
import re

def data_cleaner(raw_data_filepath, save_to_csv = False):
    """A function to clean web-scraped data with Pandas and Regex.

    Parameters
    ----------
    raw_data_filepath : str
        The path of the raw data CSV file.
    save_to_csv: bool
        Whether to export the cleaned data into a CSV file (default = False)

    Returns
    -------
    pandas.core.frame.DataFrame
        A cleaned dataframe ready for filtering and analysis. 
        A csv containing the cleaned dataframe could also be exported with `save_to_csv` option is True.
    

    Examples
    --------
    >>> data_cleaner("data/raw.csv")
    """ 
    return True

