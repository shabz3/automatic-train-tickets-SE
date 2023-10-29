from booking_details import *
from driver import *
from dotenv import load_dotenv
from basket import *
from ticket_collection import *
import os

load_dotenv()

driver = driver()
open_website(driver, "https://www.southeasternrailway.co.uk/")

shadow_root = get_shadow_root(driver)

close_cookie_popup(driver)
select_return_button(shadow_root)
destination_or_arrival(shadow_root, driver, "departure", os.environ.get("DEPARTING_STATION"))
destination_or_arrival(shadow_root, driver, "arrival", os.environ.get("ARRIVING_STATION"))
select_calendar_details(shadow_root, "Return", os.environ.get("DEPARTING_DATE"), os.environ.get("DEPART_DEPARTURE_OR_ARRIVAL"),os.environ.get("DEPART_TIME"))
select_calendar_details(shadow_root, "Arrive", os.environ.get("ARRIVING_DATE"), os.environ.get("ARRIVE_DEPARTURE_OR_ARRIVAL"), os.environ.get("ARRIVE_TIME"))
add_railcard(shadow_root, os.environ.get("RAILCARD"))
click_find_times_and_tickets(shadow_root)
add_to_basket(driver)
eticket(driver)
continue_button(driver)

driver.close()