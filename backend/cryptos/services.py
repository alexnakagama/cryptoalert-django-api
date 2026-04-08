import requests

def get_price(url: str, params=None):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error ocurred at the time of consuming the API: {e}")
        return None
        
def get_crypto_price(symbol: str, currency: str, volume):
    return get_price(f'https://criptoya.com/api/{symbol}/{currency}/{volume}')