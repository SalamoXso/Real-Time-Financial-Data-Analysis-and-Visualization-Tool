import pandas as pd

def validate_data(df):
    """
    Validates the data to ensure it meets the expected format and criteria.
    """
    if not all(column in df.columns for column in ['timestamp', 'price', 'volume']):
        raise ValueError("Data is missing required columns")
    
    # Ensure data types are correct
    if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        raise ValueError("Timestamp column must be datetime type")
    
    return True
