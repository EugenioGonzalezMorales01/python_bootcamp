import datetime
import os

import requests as requests

# ------------------------------- Request to Nutritionix -----------------------------
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
nutrition_API_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
date = datetime.datetime.now()

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

nutrition_API_body = {
    'query': input('What have yo done today? '),
    'gender': 'male',
    'weight_kg': '70',
    "height_cm": 165,
    "age": 22
}

response = requests.post(url=nutrition_API_endpoint, json=nutrition_API_body, headers=headers)
print(response.text)
# ------------------------------- Proccesing the data from Nutritionix -----------------------------
data = response.json()['exercises']
data = response.json()['exercises'][:len(data)]
now = datetime.datetime.now()
new_data = {}

# ------------------------------- Request to Sheety -------------------------
sheety_endpoint = os.environ.get('sheety_endpoint')
sheety_header = {
    'Authorization': os.environ.get('Authorization')
}
for dict in data:
    new_data['date'] = now.date().strftime('%d/%m/%Y')
    new_data['time'] = now.time().strftime('%H:%M:%S')
    new_data['exercise'] = dict['user_input']
    new_data['duration'] = str(dict['duration_min'])
    new_data['calories'] = str(dict['nf_calories'])
    sheety_body = {
        'workout': new_data

    }
    response = response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_header)






