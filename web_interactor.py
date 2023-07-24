from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os
import logging

load_dotenv()
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler()
                    ])

class WebInteractor:
    def __init__(self):
        logging.info("Initializing WebInteractor...")
        self.driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH))

    # Navigate to the webpage.
    def navigate_to_page(self, url):
        logging.info(f"Navigating to {url}...")
        self.driver.get(url)

    # Click the Destination field-button.
    def click_search_button(self):
        logging.info("Clicking Destination field-button...")
        time.sleep(0.5)
        destination_field_button = self.driver.find_element(By.CSS_SELECTOR, '.uitk-fake-input.uitk-form-field-trigger')
        destination_field_button.click()
        time.sleep(1)

    # Locate the date form field button and click it.
    def click_date_selector(self):
        logging.info("Clicking Date field-button...")
        date_form_field_button = self.driver.find_element(By.CSS_SELECTOR, "[data-name='date_form_field']")
        date_form_field_button.click()
        time.sleep(1)

    # Input the destination and hit enter, destination variable is the name
    # of the city and will be passed in from the main.py file.
    def input_destination_and_search(self, destination):
        logging.info(f"Inputting destination ({destination}) and hitting enter...")
        input_field = self.driver.find_element(By.CSS_SELECTOR, '[data-stid="destination_form_field-menu-input"]')
        input_field.send_keys(destination)
        time.sleep(1)
        input_field.send_keys(Keys.RETURN)
        time.sleep(1.5)

    # This method simply quits the browser.
    def quit(self):
        logging.info("Quitting browser...")
        self.driver.quit()

    # Scan the calendar for the correct month.
    def select_correct_month(self, month_name):
        logging.info(f"Selecting correct month ({month_name})...")
        # Get the current displayed month
        current_month_element = self.driver.find_element(By.CSS_SELECTOR, ".uitk-date-picker-month-name.uitk-type-medium")
        current_month = current_month_element.text.split(" ")[0]  # We only want the month part, not the year

        # Check if the current displayed month matches the desired month
        while current_month != month_name:
            logging.info(f"Current month ({current_month}) does not match desired month ({month_name})")
            # If the current month does not match the desired month, click the previous month button
            previous_month_button = self.driver.find_element(By.CSS_SELECTOR, '[data-stid="date-picker-paging"]')
            previous_month_button.click()
            time.sleep(1)

            logging.info("Checking current month again...")
            # Check the current month again
            current_month_element = self.driver.find_element(By.CSS_SELECTOR, ".uitk-date-picker-month-name.uitk-type-medium")
            current_month = current_month_element.text.split(" ")[0]
            logging.info(f"Current month is now {current_month}")

        return current_month


        