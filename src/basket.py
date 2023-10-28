from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def add_to_basket(driver):
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "element_id")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/section/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/button").click()
