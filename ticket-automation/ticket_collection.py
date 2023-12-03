from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def eticket(driver):
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "e-ticket")))
    element.click()

def continue_button(driver):
    continue_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
    continue_button.click()