import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/AmazonBasics-Puresoft-PU-Padded-Mid-Back-Computer/dp/B081H43WV2/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&keywords=desk%2Bchair&pf_rd_i=14544463011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=c23f35de-b906-43a0-ac4d-4e459ff65c0b&pf_rd_r=2F0XQQY2B61GRWCRHXKK&pf_rd_s=merchandised-search-1&pf_rd_t=101&qid=1622540153&refinements=p_89%3AAmazonBasics%7CFlash%2BFurniture%7CHON%7CHerman%2BMiller%7CModway%7COFM%7CPOLY%2B%26%2BBARK%7CSteelcase%2Cp_72%3A1248915011&rnid=1248913011&s=home-garden&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOEhYVVM2UkgwRTlTJmVuY3J5cHRlZElkPUEwMTc5NjI5SFpQUTJYV1I2WlpDJmVuY3J5cHRlZEFkSWQ9QTA0NDc2OTgzU1ZESjk0RUYwTENCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
TARGET_PRICE = 100.0
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT = "<RECIPIENT_EMAIL>"


def scrap_website():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url=URL, headers=headers)
    return BeautifulSoup(response.text, "lxml")


def get_current_price(soup):
    price_list = soup.find_all(name="span", id="priceblock_ourprice")
    try:
        price_in_str = price_list[0].getText()
    except IndexError:
        print("This item is not available")
        return -999
    else:
        return float(price_in_str.split("$")[1])


def get_product(soup):
    product_title_element = soup.find_all(name="span", id="productTitle")
    try:
        product_title = product_title_element[0].getText().strip()
    except IndexError:
        print("This product is not available")
        return "Product not available"
    else:
        return product_title


scrapped_content = scrap_website()
price = get_current_price(scrapped_content)
product_name = get_product(scrapped_content)
if price != -999 and price < TARGET_PRICE:
    email_content = f"{product_name} is now ${price}\n{URL}"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:Amazon Price Alert!\n\n{email_content}"
        )
