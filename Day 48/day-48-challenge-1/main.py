from selenium import webdriver

chrome_driver_path = "C:\\Users\\YanJun\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = [{"time": time.text, "event": event.text} for time in event_times for event in event_names]
print(events)

driver.quit()
