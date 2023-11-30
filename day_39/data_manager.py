import requests
class DataManager:
    def __init__(self):
        self.sheety_endpoint = 'https://api.sheety.co/bd4984be7623b2068281ac82f86d05d8/flightDeals/prices'
        self.header = {
            'apikey': 'sUP3L0QCyMDmA2HILytggxSFq2bAgW59'
        }

    def get_iata_codes_from_tequila(self, sheety_data):
        for flight in sheety_data:
            params = {
                'term': flight['city']
            }
            response = requests.get(url='https://api.tequila.kiwi.com/locations/query', params=params, headers=self.header)
            flight['iataCode'] = response.json()['locations'][0]['code']

        return sheety_data
    def set_iata_codes_in_sheety(self, sheety_data):

        for x in range(len(sheety_data)):
            price_dict = {
                'price': sheety_data[x]
            }
            requests.put(url=f'{self.sheety_endpoint}/{price_dict["price"]["id"]}', json=price_dict)