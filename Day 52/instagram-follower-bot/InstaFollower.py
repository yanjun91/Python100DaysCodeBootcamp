from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self, account_to_follow):
        self.driver.get(account_to_follow)
        fbody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 10:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
            time.sleep(2)
            scroll += 1

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
