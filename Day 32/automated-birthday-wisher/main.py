import smtplib
import random
import datetime as dt
import pandas

MY_EMAIL = "<YOUR_EMAIL>"
MY_PASSWORD = "<YOUR_PASSWORD>"
RECIPIENT = "<RECIPIENT_EMAIL"
letter_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

# Get all birthdays from csv file
birthdays_df = pandas.read_csv("birthdays.csv")
# Convert DataFrame into dictionary with (month, day) tuple as key
birthday_dict = {(int(row["month"]), int(row["day"])): row for (index, row) in birthdays_df.iterrows()}

# Check if today's month, day tuple key exist in the dictionary
if(today_month, today_day) in birthday_dict:
    birthday_person = birthday_dict[(today_month, today_day)]
    # Get randomised letter content and replace name placeholder
    with open(random.choice(letter_list)) as letter_file:
        letter_content = letter_file.read()
        final_content = letter_content.replace("[NAME]", birthday_person["name"])

    # Send birthday email
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:Happy Birthday!\n\n{final_content}"
        )
