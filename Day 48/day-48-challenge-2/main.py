from selenium import webdriver

chrome_driver_path = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
sign_up_btn = driver.find_element_by_css_selector(".form-signin button")

fname.send_keys("Yan Jun")
lname.send_keys("Lim")
email.send_keys("yanjun@email.com")
sign_up_btn.click()

