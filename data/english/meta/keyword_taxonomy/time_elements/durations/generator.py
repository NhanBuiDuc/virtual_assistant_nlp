import json
import os
from datetime import datetime

def generate_durations_json():
    """
    Generate a JSON file with time duration expressions.
    Each entry includes a breakdown of the duration into component time units.
    Limited to durations of a week or less.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    durations = {}
    
    # Helper function to add a duration with incremented ID
    def add_duration(key, standard_form, duration_type="exact", second=0, minute=0, hour=0, day=0, week=0, month=0, year=0, time_period=None):
        """
        Add a duration with structured time components
        """
        nonlocal id_counter
        durations[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "duration_type": duration_type,
            "second": second,
            "minute": minute,
            "hour": hour,
            "day": day,
            "week": week,
            "month": month,
            "year": year,
            "time_period": time_period
        }
        id_counter += 1
    
    # Basic time units - singular
    add_duration("a second", "1 second", second=1)
    add_duration("a minute", "1 minute", minute=1)
    add_duration("an hour", "1 hour", hour=1)
    add_duration("a day", "1 day", day=1)
    add_duration("a week", "1 week", week=1)
    add_duration("a month", "1 month", month=1)
    add_duration("a year", "1 year", year=1)
    
    # Add "for" prefix variants
    add_duration("for a second", "1 second", second=1)
    add_duration("for a minute", "1 minute", minute=1)
    add_duration("for an hour", "1 hour", hour=1)
    add_duration("for a day", "1 day", day=1)
    add_duration("for a week", "1 week", week=1)
    add_duration("for a month", "1 month", month=1)
    add_duration("for a year", "1 year", year=1)
    
    # Common minute values
    for mins in [1, 2, 3, 5, 10, 15, 20, 30, 45]:
        add_duration(f"{mins} minutes", f"{mins} minutes", minute=mins)
        add_duration(f"{mins} minute" if mins == 1 else f"{mins} minutes", f"{mins} minutes", minute=mins)
        add_duration(f"for {mins} minutes", f"{mins} minutes", minute=mins)
        add_duration(f"for {mins} minute" if mins == 1 else f"for {mins} minutes", f"{mins} minutes", minute=mins)
    
    # Common hour values
    for hrs in [1, 2, 3, 4, 5, 6, 8, 10, 12, 24, 48, 72]:
        add_duration(f"{hrs} hours", f"{hrs} hours", hour=hrs)
        add_duration(f"{hrs} hour" if hrs == 1 else f"{hrs} hours", f"{hrs} hours", hour=hrs)
        add_duration(f"for {hrs} hours", f"{hrs} hours", hour=hrs)
        add_duration(f"for {hrs} hour" if hrs == 1 else f"for {hrs} hours", f"{hrs} hours", hour=hrs)
        add_duration(f"for the next {hrs} hours", f"{hrs} hours", hour=hrs)
    
    # Common day values
    for days in [1, 2, 3, 4, 5, 6, 7, 10, 14, 30]:
        add_duration(f"{days} days", f"{days} days", day=days)
        add_duration(f"{days} day" if days == 1 else f"{days} days", f"{days} days", day=days)
        add_duration(f"for {days} days", f"{days} days", day=days)
        add_duration(f"for {days} day" if days == 1 else f"for {days} days", f"{days} days", day=days)
        add_duration(f"for the next {days} days", f"{days} days", day=days)
    
    # Common week values
    for weeks in [1, 2, 3, 4]:
        add_duration(f"{weeks} weeks", f"{weeks} weeks", week=weeks)
        add_duration(f"{weeks} week" if weeks == 1 else f"{weeks} weeks", f"{weeks} weeks", week=weeks)
        add_duration(f"for {weeks} weeks", f"{weeks} weeks", week=weeks)
        add_duration(f"for {weeks} week" if weeks == 1 else f"for {weeks} weeks", f"{weeks} weeks", week=weeks)
        add_duration(f"for the next {weeks} weeks", f"{weeks} weeks", week=weeks)
    
    # Text number expressions
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20
    }
    
    # Minutes with word numbers
    for word, num in number_words.items():
        add_duration(f"{word} minutes", f"{num} minutes", minute=num)
        add_duration(f"{word} minute" if num == 1 else f"{word} minutes", f"{num} minutes", minute=num)
        add_duration(f"for {word} minutes", f"{num} minutes", minute=num)
        add_duration(f"for {word} minute" if num == 1 else f"for {word} minutes", f"{num} minutes", minute=num)
    
    # Hours with word numbers
    for word, num in number_words.items():
        if num <= 12:  # Limit to reasonable hour values
            add_duration(f"{word} hours", f"{num} hours", hour=num)
            add_duration(f"{word} hour" if num == 1 else f"{word} hours", f"{num} hours", hour=num)
            add_duration(f"for {word} hours", f"{num} hours", hour=num)
            add_duration(f"for {word} hour" if num == 1 else f"for {word} hours", f"{num} hours", hour=num)
    
    # Days with word numbers
    for word, num in number_words.items():
        if num <= 7:  # Limit to a week
            add_duration(f"{word} days", f"{num} days", day=num)
            add_duration(f"{word} day" if num == 1 else f"{word} days", f"{num} days", day=num)
            add_duration(f"for {word} days", f"{num} days", day=num)
            add_duration(f"for {word} day" if num == 1 else f"for {word} days", f"{num} days", day=num)
    
    # Weeks with word numbers
    for word, num in number_words.items():
        if num <= 4:  # Limit to reasonable week values
            add_duration(f"{word} weeks", f"{num} weeks", week=num)
            add_duration(f"{word} week" if num == 1 else f"{word} weeks", f"{num} weeks", week=num)
            add_duration(f"for {word} weeks", f"{num} weeks", week=num)
            add_duration(f"for {word} week" if num == 1 else f"for {word} weeks", f"{num} weeks", week=num)
    
    # Special expressions
    add_duration("half a minute", "30 seconds", second=30)
    add_duration("half an hour", "30 minutes", minute=30)
    add_duration("quarter of an hour", "15 minutes", minute=15)
    add_duration("an hour and a half", "90 minutes", hour=1, minute=30)
    add_duration("an hour and a quarter", "75 minutes", hour=1, minute=15)
    add_duration("half a day", "12 hours", hour=12)
    add_duration("a day and a half", "36 hours", day=1, hour=12)
    
    # Few/couple expressions
    add_duration("a few minutes", "few minutes", duration_type="approximate", minute=3)
    add_duration("a few hours", "few hours", duration_type="approximate", hour=3)
    add_duration("a few days", "few days", duration_type="approximate", day=3)
    add_duration("a few weeks", "few weeks", duration_type="approximate", week=3)
    
    add_duration("a couple of minutes", "couple minutes", duration_type="approximate", minute=2)
    add_duration("a couple of hours", "couple hours", duration_type="approximate", hour=2)
    add_duration("a couple of days", "couple days", duration_type="approximate", day=2)
    add_duration("a couple of weeks", "couple weeks", duration_type="approximate", week=2)
    
    add_duration("for a few minutes", "few minutes", duration_type="approximate", minute=3)
    add_duration("for a few hours", "few hours", duration_type="approximate", hour=3)
    add_duration("for a few days", "few days", duration_type="approximate", day=3)
    add_duration("for a few weeks", "few weeks", duration_type="approximate", week=3)
    
    add_duration("for a couple of minutes", "couple minutes", duration_type="approximate", minute=2)
    add_duration("for a couple of hours", "couple hours", duration_type="approximate", hour=2)
    add_duration("for a couple of days", "couple days", duration_type="approximate", day=2)
    add_duration("for a couple of weeks", "couple weeks", duration_type="approximate", week=2)
    
    # Several expressions
    add_duration("several minutes", "several minutes", duration_type="approximate", minute=5)
    add_duration("several hours", "several hours", duration_type="approximate", hour=4)
    add_duration("several days", "several days", duration_type="approximate", day=4)
    add_duration("several weeks", "several weeks", duration_type="approximate", week=3)
    
    # Time periods
    add_duration("morning", "morning", duration_type="period", hour=3, time_period="morning")
    add_duration("afternoon", "afternoon", duration_type="period", hour=6, time_period="afternoon")
    add_duration("evening", "evening", duration_type="period", hour=3, time_period="evening")
    add_duration("night", "night", duration_type="period", hour=8, time_period="night")
    
    add_duration("all morning", "all morning", duration_type="period", hour=5, time_period="morning")
    add_duration("all afternoon", "all afternoon", duration_type="period", hour=6, time_period="afternoon")
    add_duration("all evening", "all evening", duration_type="period", hour=5, time_period="evening")
    add_duration("all night", "all night", duration_type="period", hour=10, time_period="night")
    add_duration("all day", "all day", duration_type="period", day=1)
    add_duration("all day long", "all day", duration_type="period", day=1)
    add_duration("the whole day", "all day", duration_type="period", day=1)
    add_duration("the entire day", "all day", duration_type="period", day=1)
    add_duration("the whole week", "all week", duration_type="period", week=1)
    add_duration("the entire week", "all week", duration_type="period", week=1)
    add_duration("overnight", "overnight", duration_type="period", hour=12, time_period="night")
    
    # For prefixes for time periods
    add_duration("for the morning", "morning", duration_type="period", hour=3, time_period="morning")
    add_duration("for the afternoon", "afternoon", duration_type="period", hour=6, time_period="afternoon")
    add_duration("for the evening", "evening", duration_type="period", hour=3, time_period="evening")
    add_duration("for the night", "night", duration_type="period", hour=8, time_period="night")
    
    # Other time ranges
    add_duration("until morning", "until morning", duration_type="range", hour=12, time_period="night")
    add_duration("until tomorrow", "until tomorrow", duration_type="range", hour=12)
    add_duration("until tonight", "until tonight", duration_type="range", hour=8)
    add_duration("until tomorrow morning", "until tomorrow morning", duration_type="range", hour=16)
    add_duration("until next week", "until next week", duration_type="range", week=1)
    add_duration("for the rest of the day", "rest of day", duration_type="range", hour=8)
    add_duration("for the rest of the week", "rest of week", duration_type="range", day=3)
    
    # Create the final JSON object
    durations_json = {
        "description": "Time spans with breakdown into time units",
        "examples": ["for an hour", "30 minutes", "all day", "overnight", "for a week", "two hours"],
        "values": durations,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return durations_json

# Generate the JSON data
json_data = generate_durations_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/durations/vocabulary/durations.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} duration expressions and saved to durations.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["30 minutes", "for an hour", "all day", "overnight", "two days", "for the next 24 hours"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')