from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

# This class is responsible for interacting with the web page.
# Since hotels.com is a dynamic web page, we need to use Selenium to interact with it.
class WebInteractor:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH))

    def navigate_to_page(self, url):
        self.driver.get(url)

    def click_search_button(self):
        time.sleep(0.5)  # Wait for 0.5 seconds before finding the element
        button = self.driver.find_element(By.CSS_SELECTOR, '.uitk-fake-input.uitk-form-field-trigger')
        button.click()
        time.sleep(1)

    def input_destination_and_search(self, destination):
        input_field = self.driver.find_element(By.CSS_SELECTOR, '[data-stid="destination_form_field-menu-input"]')
        input_field.send_keys(destination)
        time.sleep(1)
        input_field.send_keys(Keys.RETURN)
        time.sleep(1.5)  # Wait for 5 seconds before executing the next step

    def quit(self):
        self.driver.quit()
