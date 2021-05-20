import smtplib
import datetime as dt
import random

my_email = "<YOUR_EMAIL>"
password = "<YOUR_PASSWORD>"
recipient = "<RECIPIENT_EMAIL"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()  # 0 is monday, ...

if day_of_week == 3:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()

    random_quotes = random.choice(quotes)
    print(random_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Hello\n\n{random_quotes}")




