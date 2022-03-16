from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "/Users/monikanawani/Downloads/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.python.org/")
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "names": event_names[n].text,
#     }
# print(events)
# driver.quit()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# no_articles = driver.find_element(By.XPATH, "//a[contains(text(),'6,468,465')]")
# print(no_articles.text)

driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.find_element(By.NAME, "fName").send_keys("Monika")
driver.find_element(By.NAME, "lName").send_keys("Nawani")
driver.find_element(By.NAME, "email").send_keys("hash123@gamil.com")
driver.find_element(By.XPATH, "//button[contains(text(),'Sign Up')]").click()
driver.find_element(By.XPATH, "//h1[contains(text(),'Success!')]")
driver.quit()




