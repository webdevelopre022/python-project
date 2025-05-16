#YouTube channel 5starcoder
#subscribe my channel 
#project_09

import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert"
    params = {
        'from': from_currency.upper(),
        'to': to_currency.upper(),
        'amount': amount
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200 or 'result' not in data:
        raise Exception("Error fetching exchange rate")

    return data['result']

# Example usage
try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g., EUR): ")

    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
except Exception as e:
    print("Error:", e)
