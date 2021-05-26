#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
from datetime import timedelta

ORIGIN_CITY_CODE = "LON"
FLIGHT_TYPE= "round"
STAY_NIGHT_FROM = 7
STAY_NIGHT_TO = 28
CURRENCY = "GBP"

data_manager = DataManager()
sheet_data = data_manager.sheet_data.json()["prices"]
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Update city code if not exist
for data in sheet_data:
    print(data)
    id = data["id"]
    city = data["city"]
    iata_code = data["iataCode"]
    lowest_price = data["lowestPrice"]
    if iata_code == "":
        iata_code = flight_search.get_iata_code(city).json()["locations"][0]["code"]
        print(data_manager.update_data(id, city, iata_code, lowest_price).text)

tomorrow_date = dt.datetime.today().date() + timedelta(1)
six_month_from_today_date = dt.datetime.today().date() + timedelta(6*30)

for destination in sheet_data:
    flight = flight_search.get_flights_data(
        departure_city=ORIGIN_CITY_CODE,
        destination_city=destination["iataCode"],
        departure_date_from=tomorrow_date,
        departure_date_to=six_month_from_today_date,
        flight_type=FLIGHT_TYPE,
        nights_in_dst_from=STAY_NIGHT_FROM,
        nights_in_dst_to=STAY_NIGHT_TO,
        currency=CURRENCY
    )
    if flight.price != -999 and flight.price < destination["lowestPrice"]:
        print(flight)
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )