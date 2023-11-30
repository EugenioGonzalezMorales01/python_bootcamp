#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()

sheety_data = fs.get_prices_list()

# sheety_data = fs.get_aita_code(sheety_data)
#
# sheety_data = dm.get_iata_codes_from_tequila(sheety_data)
# dm.set_iata_codes_in_sheety(sheety_data)

fd = FlightData()

for flight in sheety_data:
    cheaper_flights = fd.get_flight(flight['iataCode'])
    try:
        if cheaper_flights["data"][0]["price"] < flight['lowestPrice']:
            print('\033[92m Round Cheaper Direct Flight Found! \033[0m')
            nm.send_message(cheaper_flights)
    except KeyError:
        print(f'No fly found.\n{ValueError}')



