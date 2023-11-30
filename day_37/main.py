import datetime

import requests


# ---------------------- USER CREATION ----------------------
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "qwerasdfzxcvqwe"
USERNAME = "justeugenio"
GRAPH_ID = "codegraph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------------------- GRAPH CREATION ----------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "coding graph",
    "unit": "minutes",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# ---------------------- PIXEL CREATION ----------------------
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.datetime.now().date()
date = date.strftime("%Y%m%d")
pixel_params = {
    "date": date,
    "quantity": "60",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# ---------------------- PIXEL UPDATE ----------------------
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

date = datetime.datetime.now().date()
date = date.strftime("%Y%m%d")
pixel_params = {
    "quantity": "62",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.status_code)

# ---------------------- PIXEL DELETE ----------------------
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

date = datetime.datetime.now().date()
date = date.strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.delete(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

