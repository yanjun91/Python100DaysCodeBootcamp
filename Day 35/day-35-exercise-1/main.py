import requests

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "<OPEN_WEATHER_MAP_API_KEY>"
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
