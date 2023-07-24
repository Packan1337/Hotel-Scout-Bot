from date_calculator import WeekendFinder
from web_interactor import WebInteractor
from dotenv import load_dotenv
import os

load_dotenv()
HOTELS_URL = os.getenv("HOTELS_URL")

# Store the next weekend in variables to be converted to the hotels.com format.
# When looking for a hotel, the check-in date is the next Friday and the check-out date is the next Sunday.
weekend_finder = WeekendFinder()
next_friday, next_sunday = weekend_finder.get_next_weekend()
print(f"✅ Provided correct dates ({next_friday} & {next_sunday})")

# Convert the dates to the correct format for the website
converted_friday_date = weekend_finder.format_date(next_friday.strftime("%Y-%m-%d"))
converted_sunday_date = weekend_finder.format_date(next_sunday.strftime("%Y-%m-%d"))
print(f"✅ Converted {next_friday} and {next_sunday} to {converted_friday_date} and {converted_sunday_date}")

# Create a WebInteractor instance and navigate to the webpage.
web_interactor = WebInteractor()
web_interactor.navigate_to_page(HOTELS_URL)
print("✅ Navigated to Hotels.com")

# Click the Destination field-button and input the destination.
web_interactor.click_search_button()
print("✅ Clicked Destination field-button Hotels.com")
web_interactor.input_destination_and_search("Rom")
print("✅ Inputted destination and hit enter")

# Click the date selector and input the dates.
web_interactor.click_date_selector()
print("✅ Clicked Date field-button")

full_month_friday_date = weekend_finder.convert_date_month_short_to_full(converted_friday_date)
full_month_sunday_date = weekend_finder.convert_date_month_short_to_full(converted_sunday_date)

print(f"✅ Converted {converted_friday_date} and {converted_sunday_date} to {full_month_friday_date} and {full_month_sunday_date}")

friday_month_full_name = web_interactor.select_correct_month(full_month_friday_date)
sunday_month_full_name = web_interactor.select_correct_month(full_month_sunday_date)

print(f"✅ Selected correct month ({friday_month_full_name} and {sunday_month_full_name})")
