from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
RECIPIENT_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=RECIPIENT_NUMBER,
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
