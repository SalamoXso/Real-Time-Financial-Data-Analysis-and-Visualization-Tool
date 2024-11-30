import pytest
from data_processing.fetch_data import fetch_data
from unittest.mock import patch

# Mocking the external API request
@patch('data_processing.fetch_data.make_request')
def test_fetch_data(mock_request):
    # Mock response data
    mock_response = [
        {"timestamp": "2024-11-29T12:00:00", "symbol": "AAPL", "price": 150.0},
        {"timestamp": "2024-11-29T12:01:00", "symbol": "AAPL", "price": 151.0}
    ]
    mock_request.return_value = mock_response
    
    # Call the function
    df = fetch_data()
    
    # Assertions
    assert not df.empty
    assert df.shape == (2, 3)
    assert df['symbol'].iloc[0] == "AAPL"
    assert df['price'].iloc[1] == 151.0
