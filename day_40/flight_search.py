import requests


class FlightSearch:
    def __init__(self):
        sheety_endpoint = 'https://api.sheety.co/bd4984be7623b2068281ac82f86d05d8/flightDeals/prices'
        response = requests.get(url=sheety_endpoint)
        self.sheet_data = [item for item in response.json()['prices']]

    def get_prices_list(self):
        return self.sheet_data

    def get_aita_code(self, sheet_data):
        for flight in sheet_data:
            if flight['iataCode'] == '':
                flight['iataCode'] = 'TESTING'
        return sheet_data
