import requests

class ForexConverter:
    def __init__(self, base_currency="USD"):
        self.base_currency = base_currency

    def get_exchange_rate(self, target_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data["rates"].get(target_currency)
        return exchange_rate


