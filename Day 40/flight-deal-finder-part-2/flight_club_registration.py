import requests
import os

SHEETY_POST_ENDPOINT = "https://api.sheety.co/06a9ee1734ad5334a87ca74d54cf36b1/flightDeals/users"
SHEETY_AUTH = f"Bearer {os.environ.get('SHEETY_AUTH')}"

print("Welcome to Angela's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? \n")
last_name = input("What is your last name? \n")
email = input("What is your email? \n")
email2 = input("Type your email again.\n")

while email != email2:
    print("Email does not matched. Please re-enter your email.")
    email = input("What is your email? \n")
    email2 = input("Type your email again.\n")

headers = {
    "Authorization": SHEETY_AUTH
}

params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

response = requests.post(url=SHEETY_POST_ENDPOINT, json=params, headers=headers)
if response.status_code == 200:
    print("You're in the club!")
