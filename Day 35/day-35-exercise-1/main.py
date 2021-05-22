import requests

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "98d20d2f4005334b32aa45860564d8cc"
MY_LAT = 5.329910
MY_LONG = 100.266040

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
print(response.json())
