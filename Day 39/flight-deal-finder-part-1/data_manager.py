import requests
import os

SHEETY_GET_ENDPOINT = "https://api.sheety.co/06a9ee1734ad5334a87ca74d54cf36b1/flightDeals/prices"
SHEETY_POST_PUT_ENDPOINT= "https://api.sheety.co/06a9ee1734ad5334a87ca74d54cf36b1/flightDeals/prices"
SHEETY_AUTH = f"Bearer {os.environ.get('SHEETY_AUTH')}"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_headers = {
            "Authorization": SHEETY_AUTH
        }

        self.sheety_parameters = {
            "price": {
                "city": "",
                "iata code": "",
                "lowest price": ""
            }
        }

        self.sheet_data = self.get_data()

    def get_data(self):
        return requests.get(url=SHEETY_GET_ENDPOINT, headers=self.sheety_headers)

    def update_data(self, index, city, iata_code, lowest_price):
        sheety_put_endpoint = f"{SHEETY_POST_PUT_ENDPOINT}/{index}"
        self.sheety_parameters = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }
        return requests.put(url=sheety_put_endpoint, json=self.sheety_parameters, headers=self.sheety_headers)