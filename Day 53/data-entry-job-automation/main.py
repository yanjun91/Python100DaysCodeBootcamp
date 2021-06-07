from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdL6MWRLJ75aKw3L5q3awhmLt144JuRAhq-KaQpFVaT8t_mvw/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
listings = soup.find_all(name="div", class_="list-card-info")
all_listing_postings = []
for listing in listings:
    anchor = listing.find(name="a", class_="list-card-link")
    price_element = listing.find(name="div", class_="list-card-price")
    if anchor is not None:
        link = anchor.get('href')
        address = anchor.getText()
        price = price_element.getText().split('/')[0]
        if "+" in price:
            price = price.split("+")[0]
        if link.startswith("/b"):
            link = "https://www.zillow.com" + link
        rental_listing_info = {
            "link": link,
            "address": address,
            "price": price
        }
        all_listing_postings.append(rental_listing_info)

print(all_listing_postings)

# Fill up Google Form
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

for listing in all_listing_postings:
    driver.get(GOOGLE_FORM_URL)

    time.sleep(1)

    # Get all input as well as submit button elements
    address_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_btn = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div")

    # Enter all details and submit the form
    address_input.send_keys(listing.get("address"))
    price_input.send_keys(listing.get("price"))
    link_input.send_keys(listing.get("link"))
    submit_btn.click()
