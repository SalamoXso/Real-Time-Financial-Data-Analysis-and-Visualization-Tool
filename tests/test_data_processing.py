import unittest
import pandas as pd
from data_processing.process_data import process_data
from data_processing.utils.data_cleaning import clean_data

class TestDataProcessing(unittest.TestCase):
    def test_data_cleaning(self):
        df = pd.DataFrame({
            'symbol': ['AAPL', 'GOOG', 'AMZN'],
            'timestamp': ['2024-11-29 14:30', '2024-11-29 14:31', '2024-11-29 14:32'],
            'price': [175.45, 2923.25, 3342.15],
            'volume': [1500, 1000, 2000]
        })
        cleaned_df = clean_data(df)
        self.assertFalse(cleaned_df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
