import os
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
down = bot.down
up = bot.up
print(f"Download: {down}Mbps, Upload: {up}Mbps")
if down < PROMISED_DOWN or up < PROMISED_UP:
    print("Speed not as promised! Tweeting a complaint...")
    tweet = f"Hey Internet Provider, why is my internet speed {down}down/{up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, tweet)
else:
    print("Promised speed met!")
