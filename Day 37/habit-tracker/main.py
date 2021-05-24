import requests
import datetime as dt
from datetime import timedelta

USERNAME = "yanjun"
TOKEN = "a2siunv12yuior4aqeor5ha"
GRAPH_ID = "yjgraph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = str(dt.datetime.today().date().strftime("%Y%m%d"))
yesterday = str((dt.datetime.today().date() - timedelta(1)).strftime("%Y%m%d"))

post_pixel_params = {
    "date": today,
    "quantity": input("How many kilometres did you cycled today? ")
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)


update_pixel_endpoint = f"{post_pixel_endpoint}/{yesterday}"

update_pixel_params = {
    "quantity": "20"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# response.raise_for_status()
# print(response.text)

delete_pixel_endpoint = f"{post_pixel_endpoint}/{yesterday}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
