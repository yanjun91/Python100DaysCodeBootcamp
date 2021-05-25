import requests
import os
import datetime as dt

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_AUTH = f"Bearer {os.environ.get('SHEETY_AUTH')}"

GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/06a9ee1734ad5334a87ca74d54cf36b1/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(nutritionix_endpoint, json=parameters, headers=headers)
print(response.json())

exercises = response.json()["exercises"]

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_AUTH
}

today = dt.datetime.now()

for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": today.date().strftime("%d/%m/%Y"),
            "time": today.time().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    print(sheety_response.text)
