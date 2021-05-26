import requests
import os
from flight_data import FlightData

KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_LOCATION_QUERY_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_FLIGHT_QUERY_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": KIWI_API_KEY
        }

        self.parameters = {
            "term": ""
        }

    def get_iata_code(self, city):
        self.parameters = {
            "term": city,
            "location_types": city
        }
        return requests.get(url=KIWI_LOCATION_QUERY_ENDPOINT, params=self.parameters, headers=self.headers)

    def get_flights_data(self, departure_city, destination_city, departure_date_from, departure_date_to,
                         flight_type, nights_in_dst_from, nights_in_dst_to, currency):
        parameters = {
            "fly_from": departure_city,
            "fly_to": destination_city,
            "date_from": departure_date_from,
            "date_to": departure_date_to,
            "flight_type": flight_type,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": currency
        }
        response = requests.get(url=KIWI_FLIGHT_QUERY_ENDPOINT, params=parameters, headers=self.headers)
        try:
            flight_response_data = response.json()["data"][0]
        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(
                url=KIWI_FLIGHT_QUERY_ENDPOINT, params=parameters, headers=self.headers)
            try:
                data = response.json()["data"][0]
                print(data)
            except IndexError:
                print(f"Flight from {departure_city} to {destination_city} with 1 stopover not found")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        flight_data = FlightData(
            price=flight_response_data["price"],
            origin_city=flight_response_data["route"][0]["cityFrom"],
            origin_airport=flight_response_data["route"][0]["flyFrom"],
            destination_city=flight_response_data["route"][0]["cityTo"],
            destination_airport=flight_response_data["route"][0]["flyTo"],
            out_date=flight_response_data["route"][0]["local_departure"].split("T")[0],
            return_date=flight_response_data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
