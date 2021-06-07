from InstaFollower import InstaFollower
import os

INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
INSTAGRAM_URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "chefsteps"
account_to_visit = INSTAGRAM_URL+SIMILAR_ACCOUNT

insta = InstaFollower()
insta.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
insta.find_followers(account_to_visit)
insta.follow()
