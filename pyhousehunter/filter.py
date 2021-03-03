import pandas as pd
import csv

def data_filter(csv,
                min_price,
                max_price,
                sqrt_ft,
                num_bedroom,
                num_bathroom,
                neighbourhood):

    """Function to filter the given csv as per selection inputs
    Parameters
    ----------
    csv: csv
        A cleaned csv file
    min_price: int
        Minimum price 
    max_price: int
        Maximum price
    sqrt_ft: int
        Minimum square feet
    num_bedroom: int
        Number of bedroom 
    num_bathroom: int
        Number of bathroom
    neighbourhood: string
        A neighbourhood 

    
    Returns
    -------
    A csv
        The filtered csv based on user selection criteria

    Examples
    -------
    >>> filter(cleaned_info.csv, 2000, 3000, 900, 2, 2, "Downtown")
               
    """

    return True
