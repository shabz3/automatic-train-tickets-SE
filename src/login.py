from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def login(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-login"))
    )
    element.click()


def enter_details(driver):
    email_field = driver.find_element(By.ID, "username")
    # email.click()
    email_field.send_keys(os.environ.get("EMAIL"))

    password_field = driver.find_element(By.XPATH, "//*[@id='password']")
    # password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

    password_field.send_keys(os.environ.get("PASSWORD"))

    # login_button = WebDriverWait(driver, 6).until(
    #     EC.element_to_be_clickable((By.XPATH, f"/html/body/section/div/div[2]/div/div/div[3]/button"))
    # )
    login_button = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div/div[3]/button")
    time.sleep(1)
    login_button.click()
