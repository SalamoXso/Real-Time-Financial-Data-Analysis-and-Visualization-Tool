import httpx
import pandas as pd
from config.config import ALPHA_VANTAGE_API_KEY

def fetch_data(symbol, interval='1min'):
    """
    Fetches real-time data for a given symbol from Alpha Vantage API.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        time_series = data.get('Time Series (1min)', {})
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        return df
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    symbol = 'AAPL'  # Example symbol
    data = fetch_data(symbol)
    if data is not None:
        print(data.head())
