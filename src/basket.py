from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_to_basket(driver):
    grid_button = driver.find_element(By.XPATH, "//*[@id='service-grid-v2']/div/div[2]/div[1]/div[2]/div[1]/div[1]/nav/ul/li[1]/span")
    grid_button.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/section/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/button")))
    element.click()
