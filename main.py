from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import dateparser
import datetime

# TODO: add option for just a single ticket

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.southeasternrailway.co.uk/")
assert "South" in driver.title

# entering the year doesn't do anything
DEPARTING_DATE = "11/10/2023"
DEPART_DEPARTURE_OR_ARRIVAL = "Leaving at"
DEPART_TIME = "11:30"

ARRIVING_DATE = "20/10/2023"
ARRIVE_DEPARTURE_OR_ARRIVAL = "Arriving at"
ARRIVE_TIME = "17:30"

dateparer_settings = {'DATE_ORDER': 'DMY'}
RAILCARD = "16-25 Railcard"

def get_shadow_root():
    shadow_root_wrapper = driver.find_element(By.XPATH, '//*[@id="otrl-custom-hero"]')
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_root_wrapper)
    # shadow_root = driver.execute_script("return arguments[0].shadowRoot.querySelector('//*')", shadow_root_wrapper)
    return shadow_root

def find_element_by_css_selector(css):
    shadow_root = get_shadow_root()
    return shadow_root.find_element(By.CSS_SELECTOR, css)

def find_elements_by_css_selector(css):
    shadow_root = get_shadow_root()
    return shadow_root.find_elements(By.CSS_SELECTOR, css)


def close_cookie_popup():
    cookies_button = driver.find_element(By.CSS_SELECTOR, "a").text
    if cookies_button == "Allow All Cookies":
        click_cookie_button = driver.find_element(By.LINK_TEXT, "Allow All Cookies")
        click_cookie_button.click()


def select_return_button():
    shadow_root = get_shadow_root()

    shadow_root.find_elements(By.CLASS_NAME, 'otrl-jp__mobile-ticket-radio')[1].click()

def select_calendar_details(return_or_arrive, DATE, DEPARTURE_OR_ARRIVAL, TIME):
    shadow_root = get_shadow_root()

    # get month out of DATE. Eg: returns 10 for "14/10/2023"
    parsed_month = dateparser.parse(DATE, settings={'DATE_ORDER': 'DMY'}).month
    # Get month name for corresponding month number. Eg: gets "March" from 3
    month_name = dateparser.parse(f"{parsed_month}/1").strftime('%B')

    # "Outbound" is [0] and "Return" is [1]
    calendar = shadow_root.find_elements(By.CLASS_NAME, 'otrl-jp__date-input__container')

    # click on calendar selector
    if return_or_arrive == "Return":
        calendar[0].click()
    else:
        calendar[1].click()

    # Get what month it is on datepicker
    month_on_calendar = shadow_root.find_element(By.CLASS_NAME, "DayPicker-Caption").text.split(" ")[0]
    # while the correct month is not on the screen
    while month_on_calendar != month_name:
        # Click on "next month" button
        shadow_root.find_element(By.CLASS_NAME, "otrl-ui__date-picker__month-selector__button--next").click()
        month_on_calendar = shadow_root.find_element(By.CLASS_NAME, "DayPicker-Caption").text.split(" ")[0]

    formatted_date = dateparser.parse(DATE, settings={'DATE_ORDER': 'DMY'}).strftime("%a %b %d %Y")
    # Click on date on datepicker
    find_element_by_css_selector(f'[aria-label="{formatted_date}"]').click()

    # change Leaving at/Arriving at based on what user wants
    select = Select(shadow_root.find_element(By.NAME, "timeType"))
    if DEPARTURE_OR_ARRIVAL != select.first_selected_option.text:
        select.select_by_visible_text(DEPARTURE_OR_ARRIVAL)

    # change time based on what user wants
    select = Select(shadow_root.find_element(By.NAME, "time"))
    if TIME != select.first_selected_option.text:
        select.select_by_value(TIME)

    # click on "Done" button
    done_button = find_elements_by_css_selector('button[type="submit"]')[1]
    if done_button.text == "Done":
        done_button.click()
    pass

def add_railcard():
    shadow_root = get_shadow_root()

    # click on "passengers" button
    shadow_root.find_element(By.CLASS_NAME, 'otrl-jp__passengers__button').click()
    # click on "Add Railcard" button
    shadow_root.find_element(By.CLASS_NAME, 'otrl-jp__railcards-selector__button__text').click()

    select = Select(find_element_by_css_selector('[aria-label="Railcard type"]'))
    if select.first_selected_option.text != RAILCARD:
        select.select_by_visible_text(RAILCARD)


close_cookie_popup()
select_return_button()
select_calendar_details("Return", DEPARTING_DATE, DEPART_DEPARTURE_OR_ARRIVAL, DEPART_TIME)
select_calendar_details("Arrive", ARRIVING_DATE, ARRIVE_DEPARTURE_OR_ARRIVAL, ARRIVE_TIME)
add_railcard()

driver.close()