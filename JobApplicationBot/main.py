from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Linkedin URL
URL = "https://www.linkedin.com/home"
URL_2 = "https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&geoId=106164952&keywords=sdet&location=Mumbai%2C%20Maharashtra%2C%20India&sortBy=R"

# User Credentials
user_email = ""
user_password = ""
user_phone = ""

# Element Locators
SIGN_IN_BUTTON_XPATH = "//a[contains(text(),'Sign in')]"
USERNAME_ID = "username"
PASSWORD_ID = "password"
SIGN_IN_BUTTON_2_XPATH = "//button[contains(text(),'Sign in')]"
JOB_SEARCH_RESULT_LIST_CSS = ".job-card-container--clickable"
APPLY_NOW_BUTTON_CSS = ".jobs-s-apply button"
IF_APPLIED_XPATH = ".artdeco-inline-feedback span"
SUBMIT_APPLICATION_CSS = ".display-flex button"
PHONE_CLASS = "ember-text-field ember-view fb-single-line-text__input"
NEXT_BUTTON_CSS = ".justify-flex-end button"
REVIEW_BUTTON_CLASS = "artdeco-button--primary ember-view"
CANCEL_BUTTON_CLASS = "artdeco-modal__dismiss"
DISCARD_BUTTON_CLASS = "artdeco-button--secondary"
DONE_BUTTON_CSS = ".artdeco-modal__actionbar button"

chrome_driver_path = "/Users/monikanawani/Downloads/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url=URL_2)
driver.maximize_window()
driver.find_element(By.XPATH, SIGN_IN_BUTTON_XPATH).click()
driver.find_element(By.ID, USERNAME_ID).send_keys(user_email)
driver.find_element(By.ID, PASSWORD_ID).send_keys(user_password)
driver.find_element(By.XPATH, SIGN_IN_BUTTON_2_XPATH).click()
results_list = driver.find_elements(By.CSS_SELECTOR, JOB_SEARCH_RESULT_LIST_CSS)

for result in results_list:
    result.click()
    time.sleep(2)
    try:
        driver.find_element(By.CSS_SELECTOR, APPLY_NOW_BUTTON_CSS).click()
        time.sleep(3)
        next_button = driver.find_element(By.CSS_SELECTOR, NEXT_BUTTON_CSS)
        next_button.click()
        # review_button = driver.find_element(By.CLASS_NAME, REVIEW_BUTTON_CLASS)
        # review_button.get_attribute("aria-label") == "Review your application":
        if next_button.get_attribute("aria-label") == "Continue to next step":
            cancel_button = driver.find_element(By.CLASS_NAME, CANCEL_BUTTON_CLASS)
            cancel_button.click()
            discard_button = driver.find_element(By.CLASS_NAME, DISCARD_BUTTON_CLASS)
            discard_button.click()
            print("Multi-step apply, skipped")
            continue
        else:
            submit_application = driver.find_element(By.CSS_SELECTOR, SUBMIT_APPLICATION_CSS)
            submit_application.click()
            driver.find_element(By.CSS_SELECTOR, DONE_BUTTON_CSS).click()
            print("Application done")

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()







