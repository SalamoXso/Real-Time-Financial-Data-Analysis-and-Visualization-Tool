import pandas as pd
from .utils.data_cleaning import clean_data
from .utils.data_validation import validate_data
from db.models import FinancialData
from db.db_setup import engine
from sqlalchemy.orm import sessionmaker

def process_data(df):
    """
    Processes and validates data, then saves it to the database.
    """
    # Validate the data
    if validate_data(df):
        # Clean the data
        df = clean_data(df)

        # Save to the database
        Session = sessionmaker(bind=engine)
        session = Session()

        for _, row in df.iterrows():
            data_entry = FinancialData(
                symbol=row['symbol'],
                timestamp=row['timestamp'],
                price=row['price'],
                volume=row['volume']
            )
            session.add(data_entry)

        session.commit()
        session.close()
        print("Data processed and stored successfully.")
    else:
        print("Data validation failed.")

if __name__ == "__main__":
    # Example usage
    sample_data = pd.DataFrame({
        'symbol': ['AAPL', 'AAPL', 'GOOG'],
        'timestamp': pd.to_datetime(['2024-11-29 14:30', '2024-11-29 14:31', '2024-11-29 14:32']),
        'price': [175.45, 176.10, 2923.25],
        'volume': [1500, 2000, 1000]
    })
    process_data(sample_data)
