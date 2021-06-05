from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import os
import time

TINDER_USERNAME = os.environ.get("TINDER_USERNAME")
TINDER_PASSWORD = os.environ.get("TINDER_PASSWORD")

chrome_driver_path = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.tinder.com/")

time.sleep(2)  # Wait for windows to finish loading
login_button = driver.find_element_by_xpath('//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()

time.sleep(2)  # Wait for windows to finish loading
fb_login = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

time.sleep(2)
tinder_main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# Switch to Facebook login window
driver.switch_to.window(fb_login_window)
print(driver.title)

# Enter login details and hit Enter key
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
email.send_keys("test")
password.send_keys("Test")
# password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(tinder_main_window)
print(driver.title)

# Delay by 5 seconds to allow page to load.
time.sleep(5)

# Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):

    # Add a 1 second delay between clicks.
    time.sleep(1)

    try:
        nope_button = driver.find_element_by_xpath(
            '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        nope_button.click()
    # if button not loaded, wait for 2 seconds before retrying.
    except NoSuchElementException:
        time.sleep(2)
