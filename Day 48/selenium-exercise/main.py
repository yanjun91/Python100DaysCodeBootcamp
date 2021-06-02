from selenium import webdriver

chrome_driver_path = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Find element content by id
# driver.get("https://www.amazon.com/AmazonBasics-Puresoft-PU-Padded-Mid-Back-Computer/dp/B081H43WV2/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&keywords=desk%2Bchair&pf_rd_i=14544463011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=c23f35de-b906-43a0-ac4d-4e459ff65c0b&pf_rd_r=2F0XQQY2B61GRWCRHXKK&pf_rd_s=merchandised-search-1&pf_rd_t=101&qid=1622540153&refinements=p_89%3AAmazonBasics%7CFlash%2BFurniture%7CHON%7CHerman%2BMiller%7CModway%7COFM%7CPOLY%2B%26%2BBARK%7CSteelcase%2Cp_72%3A1248915011&rnid=1248913011&s=home-garden&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOEhYVVM2UkgwRTlTJmVuY3J5cHRlZElkPUEwMTc5NjI5SFpQUTJYV1I2WlpDJmVuY3J5cHRlZEFkSWQ9QTA0NDc2OTgzU1ZESjk0RUYwTENCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# Find element by name. Normally used to fill in form
driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

# If all else wont work on getting element then can use xpath
report_bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(report_bug_link.text)

# driver.close()  # Close that particular tab
driver.quit()  # Close the entire windows