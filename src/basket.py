from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_to_basket(driver):
    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/section/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/button")))
    element.click()
