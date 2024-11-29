import httpx

def make_request(url, params=None, headers=None):
    """
    Makes a GET request to the provided URL with optional parameters and headers.
    """
    response = httpx.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}: {response.status_code}")
        return None
