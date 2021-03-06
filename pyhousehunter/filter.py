import pandas as pd
import csv

def data_filter(df,
                min_price,
                max_price,
                sqrt_ft,
                num_bedroom,
                city_name):

    """Function to filter the given dataframe as per selection inputs
    Parameters
    ----------
    df: panda.DataFrame
        A cleaned dataframe
    min_price: int
        Minimum price 
    max_price: int
        Maximum price
    sqrt_ft: int
        Minimum square feet
    num_bedroom: int
        Number of bedroom 
    city_name: string
        A city

    
    Returns
    -------
    A panda.DataFrame
        The filtered dataframe based on user selection criteria

    Examples
    -------
    >>> data_filter(cleaned_df, 2000, 3000, 900, 2, "Vancouver")
               
    """
    
    # first check input type
    if not isinstance(min_price, (int, float)):
        raise TypeError("The minimum price entered is not a number")

    elif not isinstance(max_price, (int, float)):
        raise TypeError("The maximum number entered is not a number.")
    
    elif not isinstance(sqrt_ft, int):
        raise TypeError("The square feet entered is not an integer.")

    elif not isinstance(num_bedroom, int):
        raise TypeError("The number of bedroom entered is not an integer")

    elif not isinstance(city_name, str):
        raise TypeError("The city entered is not a string.")
    
    # then check input range
    elif not 0 <= min_price <= max_price:
        raise ValueError("Please enter appropriate positive price range.")

    elif num_bedroom < 0:
        raise ValueError("Please enter non-negative bedroom number.")
    
    # function body
    filtered_df = df.query("(@min_price <= price <= @max_price)\
                        and (num_bedroom.isnull() or num_bedroom >= @num_bedroom)\
                        and (area_sqft.isnull() or area_sqft >= @sqrt_ft)\
                        and (city.isnull() or city.str.casefold() == @city_name.casefold())")

    return filtered_df
                  
                             
