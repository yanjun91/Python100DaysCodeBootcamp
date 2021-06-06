from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_btn = self.driver.find_element_by_class_name("start-text")
        go_btn.click()
        time.sleep(50)  # Wait for 50 seconds for the speedtest to complete
        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)

    def tweet_at_provider(self, username, password, tweet):
        self.driver.get("https://twitter.com/")
        self.driver.find_element_by_link_text("Log in").click()
        time.sleep(1)  # Wait for a second for the page to load

        # Login to Twitter
        username_input = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        # Tweet complaint
        new_tweet_div = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        new_tweet_div.click()  # to activate the input field
        new_tweet_div.send_keys(tweet)
        tweet_btn = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        tweet_btn.click()
