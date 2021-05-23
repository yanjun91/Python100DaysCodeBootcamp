import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = "<TWILIO_PHONE_NUMBER>"
MY_PHONE_NUMBER = "<MY_PHONE_NUMBER>"


def get_stock_price_data():
    stock_api_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API_KEY
    }
    response = requests.get(url=STOCK_ENDPOINT, params=stock_api_parameters)
    return response.json()["Time Series (Daily)"]


def percentage_change(current, previous):
    difference = current - previous
    try:
        if difference > 0:
            change_icon = "🔺"
            print("price up")
        elif difference < 0:
            change_icon = "🔻"
            print("price drop")
        else:
            change_icon = "➖"

        return (abs(difference) / previous) * 100.0, change_icon
    except ZeroDivisionError:
        return 0, change_icon


def get_latest_three_articles(stock_price_change, icon):
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    latest_3_articles = news_response.json()["articles"][:3]
    return [
        f"{STOCK}: {icon}{stock_price_change[0]}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in latest_3_articles]


def send_sms(formatted_articles_to_send):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # Send each article as a separate message via Twilio.
    for article in formatted_articles_to_send:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_PHONE_NUMBER
        )

    print(message.status)


data = get_stock_price_data()
# Convert to list for easy access
data_list = [value for (key, value) in data.items()]

yesterday_price = float(data_list[0]["4. close"])
day_before_yesterday_price = float(data_list[1]["4. close"])

price_change = percentage_change(yesterday_price, day_before_yesterday_price)
price_change_icon = round(price_change[1], 2)

# Only send sms if price change percentage is more than 5%
if price_change[0] >= 5:
    formatted_articles = get_latest_three_articles(price_change, price_change_icon)
    print(formatted_articles)
    send_sms(formatted_articles)
