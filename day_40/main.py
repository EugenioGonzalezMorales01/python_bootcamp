#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()

# ----------------------- User Data Processing -------------------
# loop = True
# while loop:
#     name = input("Name: ")
#     last_name = input("Last Name: ")
#     email = input("Email: ")
#     if email == input("Email (Again): "):
#         print("You have been registered!")
#         loop = False
#
# user_data = {
#     'firstName': name,
#     'lastName': last_name,
#     'email': email
# }
#
# dm = DataManager()
# dm.set_user(user_data)




# ----------------------- Flight Data Processing ----------------
sheety_data = fs.get_prices_list()

fd = FlightData()

for flight in sheety_data:
    cheaper_flights = fd.get_flight(flight['iataCode'])
    try:
        if cheaper_flights["data"][0]["price"] < flight['lowestPrice']:
            print('\033[92m Round Cheaper Direct Flight Found! \033[0m')
            # nm.send_message(cheaper_flights)
            nm.send_email(cheaper_flights, dm.get_users())
    except IndexError:
        print(f'No fly found.')







