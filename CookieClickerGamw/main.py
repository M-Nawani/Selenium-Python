from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Cookie clicker url
URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "/Users/monikanawani/Downloads/chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)
driver.maximize_window()

# Cookie to click
cookie = driver.find_element(By.XPATH, "//div[@id='bigCookie']")

timeout = time.time() + 5
game_time = time.time() + 60 * 5

while game_time:
    cookie.click()
    if time.time() > timeout:
        products = [product for product in driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')]
        if len(products) > 0:
            products[-1].click()
        timeout = time.time() + 5

    if time.time() > game_time:
        print(driver.find_element(By.CSS_SELECTOR, '#cookies div').text)
        game_time = False

driver.quit()