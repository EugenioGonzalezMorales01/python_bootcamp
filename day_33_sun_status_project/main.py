import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 3 # Your latitude
MY_LONG = 32 # Your longitude
SERVER = "smtp.gmail.com"
PORT = 587
EMAIL = "eugenio.de.astora@gmail.com"
PASSWORD = "mxenjbgvqivxmpst"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(f"{sunset} | {sunrise}")
print(time_now.hour)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if (MY_LAT + 5) > iss_latitude > (MY_LAT - 5) and (MY_LONG + 5) > iss_longitude > (MY_LONG - 5):
        if time_now.now().hour >= sunset or time_now.hour <= sunrise:
            with smtplib.SMTP(SERVER, PORT) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs="eugenio.g.m@outlook.es", msg="Subject:SATELITE IS CLOSE\n\nLook Up!")
        else:
            print("The satelite is close, but is day time.")
    else:
        print("The satelite is not close of your position")
    time.sleep(60)


