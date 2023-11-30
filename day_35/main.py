import requests
from twilio.rest import Client
import os

# Getting weather data
OWH_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_key = "b7bffc42f340d03d20af8fbe6d6f490d"
weather_params = {
    "lat": 16.5612,
    "lon": -94.6139,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_key,
}
response = requests.get(OWH_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
# Picking a list of the first 12 codes of weather
weather_12h_list = [item["weather"][0]["id"] for item in weather_data["hourly"][:12]]

# Twilio credentials
account_sid = 'AC4e7278511d438c2e09ce64876767b8fb'
auth_token = 'a90993fc42dc322a61f4bee733911f4d'
# Twilio auth
client = Client(account_sid, auth_token)


for number in weather_12h_list:
    if number < 700:
        # Twilio request
        message = client.messages.create(
            body="It's dangerous to go alone\nTake this ☂️",
            from_='whatsapp:+14155238886',
            to='whatsapp:+5212211250450'
        )
        break



