from datetime import datetime, timedelta


# Class that finds the next weekend
# Data will be used for input when web scraping.
class WeekendFinder:
    def __init__(self):
        self.today = datetime.today().date()
        self.next_friday = None
        self.next_sunday = None

    # If today is Friday, return today as the next Friday
    def get_next_weekend(self):
        days_until_friday = (
            4 - self.today.weekday() + 7
        ) % 7  # 4 is the index of Friday in Python's weekday()
        self.next_friday = self.today + timedelta(days_until_friday)
        self.next_sunday = self.next_friday + timedelta(days=2)
        return self.next_friday, self.next_sunday

    def format_date(self, date_string):
        # Parse the date string
        date = datetime.strptime(date_string, "%Y-%m-%d")

        # Format the date
        formatted_date = date.strftime("%d %b %Y")

        # Translate the month name to Swedish
        formatted_date = self.translate_month_to_swedish(formatted_date)

        return formatted_date

    def translate_month_to_swedish(self, formatted_date):
        # Dictionary to map English month abbreviations to Swedish
        month_translation = {
            "Jan": "jan.",
            "Feb": "feb.",
            "Mar": "mars",
            "Apr": "apr.",
            "May": "maj",
            "Jun": "juni",
            "Jul": "juli",
            "Aug": "aug.",
            "Sep": "sep.",
            "Oct": "okt.",
            "Nov": "nov.",
            "Dec": "dec.",
        }

        for eng_month, swe_month in month_translation.items():
            if eng_month in formatted_date:
                return formatted_date.replace(eng_month, swe_month)

        return formatted_date

    def convert_date_month_short_to_full(self, date_string):
        # Split the date string on spaces to isolate the month
        day, month_short, year = date_string.split(" ")

        # Dictionary to map Swedish short month names to full month names
        short_to_full_month_translation = {
            "jan.": "januari",
            "feb.": "februari",
            "mars": "mars",
            "apr.": "april",
            "maj": "maj",
            "juni": "juni",
            "juli": "juli",
            "aug.": "augusti",
            "sep.": "september",
            "okt.": "oktober",
            "nov.": "november",
            "dec.": "december",
        }

        return short_to_full_month_translation.get(month_short)
