import os

import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 5.329910
MY_LONG = 100.266040

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"]
twelve_hour_data = hourly_data[:12]

will_rain = False

for hour_data in twelve_hour_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring an ☔",
                         from_='<TWILIO_PHONE_NUMBER>',
                         to='<RECIPIENT_PHONE_NUMBER>'
                     )

    print(message.status)
