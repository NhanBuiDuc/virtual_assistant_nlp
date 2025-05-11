import json
import os
from datetime import datetime

def generate_days_of_week_json():
    """
    Generate a JSON file with days of the week as spoken by humans.
    This focuses solely on the day names and categorizes them appropriately.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    days_of_week = {}
    
    # Helper function to add a day with incremented ID
    def add_day(key, standard_form, category):
        nonlocal id_counter
        days_of_week[key] = {
            "id": id_counter,
            "day_of_week": standard_form,
            "category": category
        }
        id_counter += 1
    
    # Full names (standard)
    add_day("Monday", "Monday", "weekday")
    add_day("Tuesday", "Tuesday", "weekday")
    add_day("Wednesday", "Wednesday", "weekday")
    add_day("Thursday", "Thursday", "weekday")
    add_day("Friday", "Friday", "weekday")
    add_day("Saturday", "Saturday", "weekend")
    add_day("Sunday", "Sunday", "weekend")
    
    # Common abbreviations
    add_day("Mon", "Monday", "weekday")
    add_day("Tue", "Tuesday", "weekday")
    add_day("Tues", "Tuesday", "weekday")
    add_day("Wed", "Wednesday", "weekday")
    add_day("Weds", "Wednesday", "weekday")
    add_day("Thu", "Thursday", "weekday")
    add_day("Thur", "Thursday", "weekday")
    add_day("Thurs", "Thursday", "weekday")
    add_day("Fri", "Friday", "weekday")
    add_day("Sat", "Saturday", "weekend")
    add_day("Sun", "Sunday", "weekend")
    
    # Contextual terms
    add_day("weekday", "weekday", "weekday_category")
    add_day("weekend", "weekend", "weekend_category")
    add_day("workday", "workday", "weekday_category")
    add_day("business day", "business day", "weekday_category")
    
    # Create the final JSON object
    days_of_week_json = {
        "description": "Specific days of the week as commonly spoken",
        "examples": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "values": days_of_week,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return days_of_week_json

# Now let's create a separate generator for time quantities

def generate_time_quantities_json():
    """
    Generate a JSON file with time quantity expressions as commonly spoken.
    This covers seconds, minutes, hours, days, weeks, etc. as quantities.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    time_quantities = {}
    
    # Helper function to add a time quantity with incremented ID
    def add_quantity(key, value, unit, standard_form):
        nonlocal id_counter
        time_quantities[key] = {
            "id": id_counter,
            "value": value,
            "unit": unit,
            "standard_form": standard_form
        }
        id_counter += 1
    
    # Seconds
    add_quantity("one second", 1, "second", "1 second")
    add_quantity("two seconds", 2, "second", "2 seconds")
    add_quantity("five seconds", 5, "second", "5 seconds")
    add_quantity("ten seconds", 10, "second", "10 seconds")
    add_quantity("thirty seconds", 30, "second", "30 seconds")
    add_quantity("half a minute", 30, "second", "30 seconds")
    
    # Minutes
    add_quantity("one minute", 1, "minute", "1 minute")
    add_quantity("two minutes", 2, "minute", "2 minutes")
    add_quantity("five minutes", 5, "minute", "5 minutes")
    add_quantity("ten minutes", 10, "minute", "10 minutes")
    add_quantity("fifteen minutes", 15, "minute", "15 minutes")
    add_quantity("quarter hour", 15, "minute", "15 minutes")
    add_quantity("half hour", 30, "minute", "30 minutes")
    add_quantity("thirty minutes", 30, "minute", "30 minutes")
    add_quantity("forty-five minutes", 45, "minute", "45 minutes")
    add_quantity("an hour", 60, "minute", "60 minutes")
    
    # Hours
    add_quantity("one hour", 1, "hour", "1 hour")
    add_quantity("two hours", 2, "hour", "2 hours")
    add_quantity("three hours", 3, "hour", "3 hours")
    add_quantity("four hours", 4, "hour", "4 hours")
    add_quantity("six hours", 6, "hour", "6 hours")
    add_quantity("eight hours", 8, "hour", "8 hours")
    add_quantity("twelve hours", 12, "hour", "12 hours")
    add_quantity("twenty-four hours", 24, "hour", "24 hours")
    add_quantity("a day", 24, "hour", "24 hours")
    
    # Days
    add_quantity("one day", 1, "day", "1 day")
    add_quantity("two days", 2, "day", "2 days")
    add_quantity("three days", 3, "day", "3 days")
    add_quantity("a few days", 3, "day", "3 days")
    add_quantity("four days", 4, "day", "4 days")
    add_quantity("five days", 5, "day", "5 days")
    add_quantity("a week", 7, "day", "7 days")
    add_quantity("seven days", 7, "day", "7 days")
    
    # Weeks
    add_quantity("one week", 1, "week", "1 week")
    add_quantity("two weeks", 2, "week", "2 weeks")
    add_quantity("a fortnight", 2, "week", "2 weeks")
    add_quantity("three weeks", 3, "week", "3 weeks")
    add_quantity("four weeks", 4, "week", "4 weeks")
    add_quantity("a month", 4, "week", "4 weeks")
    
    # Months
    add_quantity("one month", 1, "month", "1 month")
    add_quantity("two months", 2, "month", "2 months")
    add_quantity("three months", 3, "month", "3 months")
    add_quantity("a quarter", 3, "month", "3 months")
    add_quantity("six months", 6, "month", "6 months")
    add_quantity("half a year", 6, "month", "6 months")
    add_quantity("nine months", 9, "month", "9 months")
    add_quantity("twelve months", 12, "month", "12 months")
    add_quantity("a year", 12, "month", "12 months")
    
    # Years
    add_quantity("one year", 1, "year", "1 year")
    add_quantity("two years", 2, "year", "2 years")
    add_quantity("three years", 3, "year", "3 years")
    add_quantity("five years", 5, "year", "5 years")
    add_quantity("a decade", 10, "year", "10 years")
    add_quantity("ten years", 10, "year", "10 years")
    add_quantity("twenty years", 20, "year", "20 years")
    add_quantity("fifty years", 50, "year", "50 years")
    add_quantity("a century", 100, "year", "100 years")
    add_quantity("a hundred years", 100, "year", "100 years")
    
    # Create the final JSON object
    time_quantities_json = {
        "description": "Time quantities as commonly expressed in conversation",
        "examples": ["one minute", "two hours", "three days", "four weeks"],
        "values": time_quantities,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return time_quantities_json

# Generate the JSON data for days of week
days_json_data = generate_days_of_week_json()

# Write to a file
days_output_path = 'data/english/meta/keyword_taxonomy/time_elements/dates/days_of_week/vocabulary/days_of_week.json'
os.makedirs(os.path.dirname(days_output_path), exist_ok=True)  # Create directories if they don't exist
with open(days_output_path, 'w', encoding='utf-8') as f:
    json.dump(days_json_data, f, indent=2)

print(f"Generated {len(days_json_data['values'])} day of week variations and saved to days_of_week.json")

# Generate the JSON data for time quantities
quantities_json_data = generate_time_quantities_json()

# Write to a file
quantities_output_path = 'data/english/meta/keyword_taxonomy/time_elements/durations/vocabulary/time_quantities.json'
os.makedirs(os.path.dirname(quantities_output_path), exist_ok=True)  # Create directories if they don't exist
with open(quantities_output_path, 'w', encoding='utf-8') as f:
    json.dump(quantities_json_data, f, indent=2)

print(f"Generated {len(quantities_json_data['values'])} time quantity expressions and saved to time_quantities.json")

# Print some examples
print("\nSample days of week entries:")
sample_days = ["Monday", "Fri", "weekend"]
for key in sample_days:
    if key in days_json_data["values"]:
        print(f'"{key}": {json.dumps(days_json_data["values"][key], indent=2)}')

print("\nSample time quantity entries:")
sample_quantities = ["one minute", "two hours", "a week", "half a year"]
for key in sample_quantities:
    if key in quantities_json_data["values"]:
        print(f'"{key}": {json.dumps(quantities_json_data["values"][key], indent=2)}')