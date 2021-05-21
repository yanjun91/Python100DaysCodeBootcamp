import requests
from datetime import datetime as dt
from datetime import timezone as tz
import smtplib
import time

MY_LAT = 5.329910
MY_LONG = 100.266040

my_email = "<YOUR_EMAIL>"
password = "<YOUR_PASSWORD>"
recipient = "<RECIPIENT_EMAIL>"

def is_iss_overhead():
    iss_response = requests.get(url="https://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    # Convert both datetime to local timezone
    sunrise_dt_obj = dt.strptime(sunrise, "%Y-%m-%dT%H:%M:%S%z")
    sunrise_in_utc_8 = sunrise_dt_obj.replace(tzinfo=tz.utc).astimezone(tz=None)
    sunset_dt_obj = dt.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
    sunset_in_utc_8 = sunset_dt_obj.replace(tzinfo=tz.utc).astimezone(tz=None)

    # Extract hour component
    sunrise_hour = int(str(sunrise_in_utc_8).split(" ")[1].split(":")[0])
    sunset_hour = int(str(sunset_in_utc_8).split(" ")[1].split(":")[0])

    time_now_hour = dt.now().hour
    return time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour


# Run repeatedly every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=f"Subject:Look up👆\n\nThe ISS is above you in the sky")
