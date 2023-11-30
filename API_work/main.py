import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #Raise an exception with the adecuate status code
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# print(data)

LATITUDE = 19.03793
LONGITUD =

parameters = {
    "lat" : LATITUDE,
    "lon" : LONGITUD,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
print(f"{sunrise} | {sunset}")

time_now = datetime.now()
print(time_now.hour)




