import calendar
from datetime import datetime

def generate_calendar(day, month, year):
    try:
        # Validate and create a datetime object
        date_obj = datetime(year, month, day)
        # Get the weekday name
        weekday_name = date_obj.strftime("%A")
        # Display results
        print(f"Date Entered: {day}-{month}-{year}")
        print(f"Day of the Week: {weekday_name}\n")
        print("Monthly Calendar:")
        print(calendar.month(year, month))
    except ValueError as e:
        print("Invalid date:", e)

# Example: May 17, 2025
generate_calendar(17, 5, 2025)
