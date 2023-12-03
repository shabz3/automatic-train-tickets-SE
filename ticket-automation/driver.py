from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import dateparser
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver


def open_website(driver, website_url):
    driver.get(website_url)
    assert "South" in driver.title


def get_shadow_root(driver):
    shadow_root_wrapper = driver.find_element(By.XPATH, '//*[@id="otrl-custom-hero"]')
    shadow_root = driver.execute_script(
        "return arguments[0].shadowRoot", shadow_root_wrapper
    )
    return shadow_root
