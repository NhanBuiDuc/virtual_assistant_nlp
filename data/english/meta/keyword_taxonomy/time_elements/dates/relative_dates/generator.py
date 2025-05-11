import json
import os
import re
from datetime import datetime

def generate_relative_dates_json():
    """
    Generate a JSON file with relative date expressions as commonly spoken.
    Each key is a verbal reference to a relative date, and the value is an object
    containing the breakdown of time units (seconds, minutes, hours, days, weeks, months, years).
    """
    # Counter for simple ID generation
    id_counter = 1
    
    relative_dates = {}
    
    # Helper function to add a relative date with incremented ID
    def add_relative_date(key, second=0, minute=0, hour=0, day=0, week=0, month=0, year=0, direction=1):
        """
        Add a relative date with specified time units.
        direction: 1 for future, -1 for past, 0 for present
        """
        nonlocal id_counter
        relative_dates[key] = {
            "id": id_counter,
            "second": second * direction,
            "minute": minute * direction,
            "hour": hour * direction,
            "day": day * direction,
            "week": week * direction,
            "month": month * direction,
            "year": year * direction
        }
        id_counter += 1
    
    # Constants for readability
    FUTURE = 1
    PAST = -1
    PRESENT = 0
    
    # Common specific relative dates
    
    # Today/Now references
    add_relative_date("today", direction=PRESENT)
    add_relative_date("now", direction=PRESENT)
    add_relative_date("at present", direction=PRESENT)
    add_relative_date("currently", direction=PRESENT)
    add_relative_date("at the moment", direction=PRESENT)
    
    # Tomorrow/Yesterday
    add_relative_date("tomorrow", day=1, direction=FUTURE)
    add_relative_date("yesterday", day=1, direction=PAST)
    add_relative_date("day after tomorrow", day=2, direction=FUTURE)
    add_relative_date("day before yesterday", day=2, direction=PAST)
    add_relative_date("the day after", day=1, direction=FUTURE)
    add_relative_date("the day before", day=1, direction=PAST)
    add_relative_date("the following day", day=1, direction=FUTURE)
    add_relative_date("the previous day", day=1, direction=PAST)
    
    # This week/month/year
    add_relative_date("this week", direction=PRESENT)
    add_relative_date("this month", direction=PRESENT)
    add_relative_date("this year", direction=PRESENT)
    
    # Next/Last time periods
    add_relative_date("next week", week=1, direction=FUTURE)
    add_relative_date("next month", month=1, direction=FUTURE)
    add_relative_date("next year", year=1, direction=FUTURE)
    add_relative_date("last week", week=1, direction=PAST)
    add_relative_date("last month", month=1, direction=PAST)
    add_relative_date("last year", year=1, direction=PAST)
    
    # Beginning/End of periods
    # These are approximations
    add_relative_date("beginning of the week", day=3, direction=PAST)
    add_relative_date("end of the week", day=3, direction=FUTURE)
    add_relative_date("beginning of the month", day=15, direction=PAST)
    add_relative_date("end of the month", day=15, direction=FUTURE)
    add_relative_date("beginning of the year", month=6, direction=PAST)
    add_relative_date("end of the year", month=6, direction=FUTURE)
    
    # Earlier/Later this period
    add_relative_date("earlier this week", day=2, direction=PAST)
    add_relative_date("later this week", day=2, direction=FUTURE)
    add_relative_date("earlier this month", day=10, direction=PAST)
    add_relative_date("later this month", day=10, direction=FUTURE)
    add_relative_date("earlier this year", month=3, direction=PAST)
    add_relative_date("later this year", month=3, direction=FUTURE)
    
    # Specific future time intervals (minutes)
    for i in range(1, 21):  # 1 to 20 minutes
        add_relative_date(f"in {i} minutes", minute=i, direction=FUTURE)
        add_relative_date(f"{i} minutes from now", minute=i, direction=FUTURE)
        add_relative_date(f"{i} minutes ago", minute=i, direction=PAST)
    
    add_relative_date("in half an hour", minute=30, direction=FUTURE)
    add_relative_date("half an hour ago", minute=30, direction=PAST)
    add_relative_date("half hour from now", minute=30, direction=FUTURE)
    
    add_relative_date("in an hour", hour=1, direction=FUTURE)
    add_relative_date("an hour from now", hour=1, direction=FUTURE)
    add_relative_date("an hour ago", hour=1, direction=PAST)
    
    # Specific future time intervals (hours)
    for i in range(1, 13):  # 1 to 12 hours
        add_relative_date(f"in {i} hours", hour=i, direction=FUTURE)
        add_relative_date(f"{i} hours from now", hour=i, direction=FUTURE)
        add_relative_date(f"{i} hours ago", hour=i, direction=PAST)
    
    # Hours and minutes combinations
    for h in range(1, 6):  # 1 to 5 hours
        for m in [15, 30, 45]:  # Common minute increments
            add_relative_date(f"in {h} hours and {m} minutes", hour=h, minute=m, direction=FUTURE)
            add_relative_date(f"{h} hours and {m} minutes from now", hour=h, minute=m, direction=FUTURE)
            add_relative_date(f"{h} hours {m} minutes ago", hour=h, minute=m, direction=PAST)
    
    # Specific future time intervals (days)
    for i in range(1, 8):  # 1 to 7 days
        add_relative_date(f"in {i} days", day=i, direction=FUTURE)
        add_relative_date(f"{i} days from now", day=i, direction=FUTURE)
        add_relative_date(f"{i} days ago", day=i, direction=PAST)
    
    # Week-based intervals
    for i in range(1, 5):  # 1 to 4 weeks
        add_relative_date(f"in {i} weeks", week=i, direction=FUTURE)
        add_relative_date(f"{i} weeks from now", week=i, direction=FUTURE)
        add_relative_date(f"{i} weeks ago", week=i, direction=PAST)
    
    # Month-based intervals
    for i in range(1, 13):  # 1 to 12 months
        add_relative_date(f"in {i} months", month=i, direction=FUTURE)
        add_relative_date(f"{i} months from now", month=i, direction=FUTURE)
        add_relative_date(f"{i} months ago", month=i, direction=PAST)
    
    # Year-based intervals
    for i in range(1, 11):  # 1 to 10 years
        add_relative_date(f"in {i} years", year=i, direction=FUTURE)
        add_relative_date(f"{i} years from now", year=i, direction=FUTURE)
        add_relative_date(f"{i} years ago", year=i, direction=PAST)
    
    # Special cases with text numbers
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "a": 1, "an": 1
    }
    
    # Text numbers for minutes
    for word, value in number_words.items():
        add_relative_date(f"in {word} minute", minute=value, direction=FUTURE)
        add_relative_date(f"{word} minute from now", minute=value, direction=FUTURE)
        add_relative_date(f"{word} minute ago", minute=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} minutes", minute=value, direction=FUTURE)
            add_relative_date(f"{word} minutes from now", minute=value, direction=FUTURE)
            add_relative_date(f"{word} minutes ago", minute=value, direction=PAST)
    
    # Text numbers for hours
    for word, value in number_words.items():
        add_relative_date(f"in {word} hour", hour=value, direction=FUTURE)
        add_relative_date(f"{word} hour from now", hour=value, direction=FUTURE)
        add_relative_date(f"{word} hour ago", hour=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} hours", hour=value, direction=FUTURE)
            add_relative_date(f"{word} hours from now", hour=value, direction=FUTURE)
            add_relative_date(f"{word} hours ago", hour=value, direction=PAST)
    
    # Text numbers for days
    for word, value in number_words.items():
        add_relative_date(f"in {word} day", day=value, direction=FUTURE)
        add_relative_date(f"{word} day from now", day=value, direction=FUTURE)
        add_relative_date(f"{word} day ago", day=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} days", day=value, direction=FUTURE)
            add_relative_date(f"{word} days from now", day=value, direction=FUTURE)
            add_relative_date(f"{word} days ago", day=value, direction=PAST)
    
    # Text numbers for weeks
    for word, value in number_words.items():
        add_relative_date(f"in {word} week", week=value, direction=FUTURE)
        add_relative_date(f"{word} week from now", week=value, direction=FUTURE)
        add_relative_date(f"{word} week ago", week=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} weeks", week=value, direction=FUTURE)
            add_relative_date(f"{word} weeks from now", week=value, direction=FUTURE)
            add_relative_date(f"{word} weeks ago", week=value, direction=PAST)
    
    # Text numbers for months
    for word, value in number_words.items():
        add_relative_date(f"in {word} month", month=value, direction=FUTURE)
        add_relative_date(f"{word} month from now", month=value, direction=FUTURE)
        add_relative_date(f"{word} month ago", month=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} months", month=value, direction=FUTURE)
            add_relative_date(f"{word} months from now", month=value, direction=FUTURE)
            add_relative_date(f"{word} months ago", month=value, direction=PAST)
    
    # Text numbers for years
    for word, value in number_words.items():
        add_relative_date(f"in {word} year", year=value, direction=FUTURE)
        add_relative_date(f"{word} year from now", year=value, direction=FUTURE)
        add_relative_date(f"{word} year ago", year=value, direction=PAST)
        
        if word not in ["a", "an"]:  # Plural forms
            add_relative_date(f"in {word} years", year=value, direction=FUTURE)
            add_relative_date(f"{word} years from now", year=value, direction=FUTURE)
            add_relative_date(f"{word} years ago", year=value, direction=PAST)
    
    # A few combinations of text numbers and time units
    for hour_word, hour_val in number_words.items():
        for min_word, min_val in number_words.items():
            if hour_val <= 5 and min_val <= 45 and min_val % 15 == 0:  # Keep it reasonable
                add_relative_date(f"in {hour_word} hour and {min_word} minutes", 
                                 hour=hour_val, minute=min_val, direction=FUTURE)
                add_relative_date(f"{hour_word} hour and {min_word} minutes from now", 
                                 hour=hour_val, minute=min_val, direction=FUTURE)
                add_relative_date(f"{hour_word} hour and {min_word} minutes ago", 
                                 hour=hour_val, minute=min_val, direction=PAST)
    
    # Expressions with "few" (approximate as 3)
    add_relative_date("in a few seconds", second=3, direction=FUTURE)
    add_relative_date("a few seconds from now", second=3, direction=FUTURE)
    add_relative_date("a few seconds ago", second=3, direction=PAST)
    
    add_relative_date("in a few minutes", minute=3, direction=FUTURE)
    add_relative_date("a few minutes from now", minute=3, direction=FUTURE)
    add_relative_date("a few minutes ago", minute=3, direction=PAST)
    
    add_relative_date("in a few hours", hour=3, direction=FUTURE)
    add_relative_date("a few hours from now", hour=3, direction=FUTURE)
    add_relative_date("a few hours ago", hour=3, direction=PAST)
    
    add_relative_date("in a few days", day=3, direction=FUTURE)
    add_relative_date("a few days from now", day=3, direction=FUTURE)
    add_relative_date("a few days ago", day=3, direction=PAST)
    
    add_relative_date("in a few weeks", week=3, direction=FUTURE)
    add_relative_date("a few weeks from now", week=3, direction=FUTURE)
    add_relative_date("a few weeks ago", week=3, direction=PAST)
    
    add_relative_date("in a few months", month=3, direction=FUTURE)
    add_relative_date("a few months from now", month=3, direction=FUTURE)
    add_relative_date("a few months ago", month=3, direction=PAST)
    
    add_relative_date("in a few years", year=3, direction=FUTURE)
    add_relative_date("a few years from now", year=3, direction=FUTURE)
    add_relative_date("a few years ago", year=3, direction=PAST)
    
    # Expressions with "couple" (approximate as 2)
    add_relative_date("in a couple of seconds", second=2, direction=FUTURE)
    add_relative_date("a couple of seconds from now", second=2, direction=FUTURE)
    add_relative_date("a couple of seconds ago", second=2, direction=PAST)
    
    add_relative_date("in a couple of minutes", minute=2, direction=FUTURE)
    add_relative_date("a couple of minutes from now", minute=2, direction=FUTURE)
    add_relative_date("a couple of minutes ago", minute=2, direction=PAST)
    
    add_relative_date("in a couple of hours", hour=2, direction=FUTURE)
    add_relative_date("a couple of hours from now", hour=2, direction=FUTURE)
    add_relative_date("a couple of hours ago", hour=2, direction=PAST)
    
    add_relative_date("in a couple of days", day=2, direction=FUTURE)
    add_relative_date("a couple of days from now", day=2, direction=FUTURE)
    add_relative_date("a couple of days ago", day=2, direction=PAST)
    
    add_relative_date("in a couple of weeks", week=2, direction=FUTURE)
    add_relative_date("a couple of weeks from now", week=2, direction=FUTURE)
    add_relative_date("a couple of weeks ago", week=2, direction=PAST)
    
    add_relative_date("in a couple of months", month=2, direction=FUTURE)
    add_relative_date("a couple of months from now", month=2, direction=FUTURE)
    add_relative_date("a couple of months ago", month=2, direction=PAST)
    
    add_relative_date("in a couple of years", year=2, direction=FUTURE)
    add_relative_date("a couple of years from now", year=2, direction=FUTURE)
    add_relative_date("a couple of years ago", year=2, direction=PAST)
    
    # Create the final JSON object
    relative_dates_json = {
        "description": "Relative dates as commonly expressed, with breakdown into time units",
        "examples": ["tomorrow", "in 3 hours", "next week", "two days ago"],
        "values": relative_dates,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return relative_dates_json

# Generate the JSON data
json_data = generate_relative_dates_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/dates/relative_dates/vocabulary/relative_dates.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} relative date expressions and saved to relative_dates.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["tomorrow", "in 30 minutes", "2 hours ago", "next week", "in 1 hour and 30 minutes"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')