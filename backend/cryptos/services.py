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

def get_min_price(symbol, currency, volume):
    data = get_crypto_price(symbol, currency, volume)
    if not data:
        return None
    prices = []
    for exchange in data:
        if 'totalAsk' in data[exchange]:
            prices.append(data[exchange]['totalAsk'])         
    if prices:
        return min(prices)
    return None

def get_max_price(symbol, currency, volume):
    data = get_crypto_price(symbol, currency, volume)
    if not data:
        return None
    prices = []
    for exchange in data:
        if 'totalAsk' in data[exchange]:
            prices.append(data[exchange]['totalAsk'])         
    if prices:
        return max(prices)
    return None