from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import dateparser
import datetime
import time


from dotenv import load_dotenv
import os
from driver import *

load_dotenv()

# TODO: add option for just a single ticket
dateparer_settings = {"DATE_ORDER": "DMY"}


def find_element_by_css_selector(shadow_root, css):
    return shadow_root.find_element(By.CSS_SELECTOR, css)


def find_elements_by_css_selector(shadow_root, css):
    return shadow_root.find_elements(By.CSS_SELECTOR, css)


def close_cookie_popup(driver):
    cookies_button = driver.find_element(By.CSS_SELECTOR, "a").text
    if cookies_button == "Allow All Cookies":
        click_cookie_button = driver.find_element(By.LINK_TEXT, "Allow All Cookies")
        click_cookie_button.click()


def select_return_button(shadow_root):
    shadow_root.find_elements(By.CLASS_NAME, "otrl-jp__mobile-ticket-radio")[1].click()


def select_calendar_details(shadow_root, return_or_arrive, DATE, DEPARTURE_OR_ARRIVAL, TIME):

    # get month out of DATE. Eg: returns 10 for "14/10/2023"
    parsed_month = dateparser.parse(DATE, settings={"DATE_ORDER": "DMY"}).month

    # Get month name for corresponding month number. Eg: gets "March" from 3
    month_name = dateparser.parse(f"{parsed_month}/1").strftime("%B")

    # "Outbound" is [0] and "Return" is [1]
    calendar = shadow_root.find_elements(
        By.CLASS_NAME, "otrl-jp__date-input__container"
    )

    # click on calendar selector
    if return_or_arrive == "Return":
        calendar[0].click()
    else:
        calendar[1].click()

    # Get what month it is on datepicker
    month_on_calendar = shadow_root.find_element(
        By.CLASS_NAME, "DayPicker-Caption"
    ).text.split(" ")[0]
    # while the correct month is not on the screen
    while month_on_calendar != month_name:
        # Click on "next month" button
        shadow_root.find_element(
            By.CLASS_NAME, "otrl-ui__date-picker__month-selector__button--next"
        ).click()
        month_on_calendar = shadow_root.find_element(
            By.CLASS_NAME, "DayPicker-Caption"
        ).text.split(" ")[0]

    formatted_date = dateparser.parse(DATE, settings={"DATE_ORDER": "DMY"}).strftime(
        "%a %b %d %Y"
    )
    # Click on date on datepicker
    find_element_by_css_selector(shadow_root, f'[aria-label="{formatted_date}"]').click()

    # change Leaving at/Arriving at based on what user wants
    select = Select(shadow_root.find_element(By.NAME, "timeType"))
    if DEPARTURE_OR_ARRIVAL != select.first_selected_option.text:
        select.select_by_visible_text(DEPARTURE_OR_ARRIVAL)

    # change time based on what user wants
    select = Select(shadow_root.find_element(By.NAME, "time"))
    if TIME != select.first_selected_option.text:
        select.select_by_value(TIME)

    # click on "Done" button
    done_button = find_elements_by_css_selector(shadow_root, 'button[type="submit"]')[1]
    if done_button.text == "Done":
        done_button.click()
    pass


def add_railcard(shadow_root, railcard):
    # click on "passengers" button
    shadow_root.find_element(By.CLASS_NAME, "otrl-jp__passengers__button").click()
    # click on "Add Railcard" button
    shadow_root.find_element(
        By.CLASS_NAME, "otrl-jp__railcards-selector__button__text"
    ).click()

    select = Select(find_element_by_css_selector(shadow_root, '[aria-label="Railcard type"]'))
    if select.first_selected_option.text != railcard:
        select.select_by_visible_text(railcard)

    find_elements_by_css_selector(shadow_root, "button")[-1].click()


def click_find_times_and_tickets(shadow_root):
    find_element_by_css_selector(shadow_root, 'button[type="submit"]').click()


def destination_or_arrival(shadow_root, driver, departure_or_arrival, leaving_station):
    dropdown = ""
    if departure_or_arrival == "departure":
        dropdown = find_element_by_css_selector(shadow_root, '[placeholder="Leaving from..."]')

    elif departure_or_arrival == "arrival":
        dropdown = find_element_by_css_selector(shadow_root, '[placeholder="Going to..."]')
    dropdown.click()
    active_element = driver.switch_to.active_element
    active_element.send_keys(leaving_station)
    # active_element.send_keys(Keys.ENTER)
    time.sleep(2)
    first_suggestion = shadow_root.find_element(
        By.CLASS_NAME, "otrl-jp__station-autosuggest__item__name"
    )
    if first_suggestion.text == leaving_station:
        first_suggestion.click()
