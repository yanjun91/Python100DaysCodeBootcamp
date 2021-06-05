from selenium import webdriver
import os
import time

'''
Save all job search result in first page of result
'''

LINKEDIN_USERNAME = os.environ.get("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

chrome_driver_path = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?geoId=103532529&keywords=web%20developer&location=Penang%2C%20Malaysia&locationId=&sortBy=R")

sign_in_btn = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_btn.click()

driver.find_element_by_id("username").send_keys(LINKEDIN_USERNAME)
driver.find_element_by_id("password").send_keys(LINKEDIN_PASSWORD)

login_btn = driver.find_element_by_css_selector(".login__form_action_container button")
login_btn.click()

search_result_list = driver.find_element_by_class_name("jobs-search-results__list")
job_list = search_result_list.find_elements_by_class_name("job-card-list__title")
for job in job_list:
    print(f"Saving {job.text} job")
    job.click()
    time.sleep(1)
    save_btn = driver.find_element_by_class_name("jobs-save-button")
    save_btn.click()




