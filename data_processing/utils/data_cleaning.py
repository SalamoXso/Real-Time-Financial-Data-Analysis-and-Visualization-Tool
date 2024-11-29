import pandas as pd

def clean_data(df):
    """
    Cleans and prepares the data for further analysis.
    """
    # Remove any rows with missing data
    df = df.dropna()
    
    # Convert columns to appropriate data types if necessary
    df = df.astype({'price': 'float', 'volume': 'int'})
    
    return df
