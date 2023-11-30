import datetime

import requests
from dateutil.relativedelta import relativedelta


class FlightData:
    def __init__(self):
        self.endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.fly_from = 'LON'
        self.header = {
            'apikey': 'sUP3L0QCyMDmA2HILytggxSFq2bAgW59'
        }

    def get_flight(self, destination):
        print(f'Looking flights to {destination}')
        six_months = datetime.date.today() + relativedelta(months=+6)
        params = {
            'fly_from': self.fly_from,
            'fly_to': destination,
            'date_from': datetime.datetime.now().strftime('%d/%m/%Y'),
            'date_to': six_months.strftime('%d/%m/%Y'),
            'max_stopovers': 0,
            'limit': 1,
            'curr': 'GBP',
            'return_from': (six_months + relativedelta(days=+7)).strftime('%d/%m/%Y'),
            'return_to': (six_months + relativedelta(days=+28)).strftime('%d/%m/%Y'),
        }
        response = requests.get(url=self.endpoint, params=params, headers=self.header)
        if response.json()['data']:
            print(response.json())
            return response.json()
        else:
            print('LOOKING FOR A FLIGHT WITH 1 STOP OVER')
            params['max_stopovers'] = 5
            response = requests.get(url=self.endpoint, params=params, headers=self.header)
            print(response.json())
            return response.json()
