import requests

API_KEY = "fca_live_2CdlMQ0kQGsUw29EKZq7DOm0uPU4mEhOSAerbHu8"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "ZAR"]

def convert_currency(a_base):
    l_currencies = ",".join(CURENCIES)
    l_url = f"{BASE_URL}&base_currency={a_base}&currencies={l_currencies}"
    
    try:
        l_response = requests.get(l_url)
        data = l_response.json()
        return data["data"]
    except Exception as e:
        print(f"error converting currency {e}")
        return {}
    
def readable_print(a_dictionary):
    for ticker, value in a_dictionary.items():
        if value != 1:
            print(f"{ticker}: {value}")

while True:
    base = input("Enter currency or q to quit: ").upper()

    if base == "Q":
        break

    curr_data = convert_currency(base)

    readable_print(curr_data)