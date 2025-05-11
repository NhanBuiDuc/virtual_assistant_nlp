import json
import os
from datetime import datetime

def generate_frequency_json():
    """
    Generate a JSON file with frequency expressions.
    Each entry includes a breakdown of the frequency into component time units.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    frequencies = {}
    
    # Helper function to add a frequency with incremented ID
    def add_frequency(key, standard_form, frequency_type="regular", 
                     second=None, minute=None, hour=None, day=None, 
                     week=None, month=None, quarter=None, year=None, 
                     number_of_occurrences=1, specific_day=None, specific_date=None, 
                     period=None, approximation=None):
        """
        Add a frequency with structured time components
        """
        nonlocal id_counter
        frequencies[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "frequency_type": frequency_type,
            "second": second,
            "minute": minute,
            "hour": hour,
            "day": day,
            "week": week,
            "month": month,
            "quarter": quarter,
            "year": year,
            "number_of_occurrences": number_of_occurrences,
            "specific_day": specific_day,
            "specific_date": specific_date,
            "period": period,
            "approximation": approximation
        }
        id_counter += 1
    
    # Basic adverbial frequencies
    add_frequency("hourly", "hourly", hour=1)
    add_frequency("daily", "daily", day=1)
    add_frequency("nightly", "nightly", day=1, period="night")
    add_frequency("weekly", "weekly", week=1)
    add_frequency("bi-weekly", "bi-weekly", week=2)
    add_frequency("biweekly", "bi-weekly", week=2)
    add_frequency("fortnightly", "fortnightly", week=2)
    add_frequency("monthly", "monthly", month=1)
    add_frequency("quarterly", "quarterly", quarter=1)
    add_frequency("yearly", "yearly", year=1)
    add_frequency("annually", "annually", year=1)
    
    # Every X expressions
    add_frequency("every hour", "hourly", hour=1)
    add_frequency("every day", "daily", day=1)
    add_frequency("every night", "nightly", day=1, period="night")
    add_frequency("every week", "weekly", week=1)
    add_frequency("every month", "monthly", month=1)
    add_frequency("every year", "yearly", year=1)
    
    # Multiple occurrences per period
    add_frequency("twice a day", "twice daily", day=1, number_of_occurrences=2)
    add_frequency("twice daily", "twice daily", day=1, number_of_occurrences=2)
    add_frequency("twice a week", "twice weekly", week=1, number_of_occurrences=2)
    add_frequency("twice weekly", "twice weekly", week=1, number_of_occurrences=2)
    add_frequency("twice a month", "twice monthly", month=1, number_of_occurrences=2)
    add_frequency("twice monthly", "twice monthly", month=1, number_of_occurrences=2)
    add_frequency("twice a year", "twice yearly", year=1, number_of_occurrences=2)
    add_frequency("twice yearly", "twice yearly", year=1, number_of_occurrences=2)
    add_frequency("twice annually", "twice yearly", year=1, number_of_occurrences=2)
    
    add_frequency("three times a day", "three times daily", day=1, number_of_occurrences=3)
    add_frequency("three times a week", "three times weekly", week=1, number_of_occurrences=3)
    add_frequency("three times a month", "three times monthly", month=1, number_of_occurrences=3)
    add_frequency("three times a year", "three times yearly", year=1, number_of_occurrences=3)
    
    add_frequency("four times a day", "four times daily", day=1, number_of_occurrences=4)
    add_frequency("four times a week", "four times weekly", week=1, number_of_occurrences=4)
    add_frequency("four times a month", "four times monthly", month=1, number_of_occurrences=4)
    add_frequency("four times a year", "four times yearly", year=1, number_of_occurrences=4)
    
    # Every X hours/days/weeks/months
    add_frequency("every two hours", "every 2 hours", hour=2)
    add_frequency("every three hours", "every 3 hours", hour=3)
    add_frequency("every four hours", "every 4 hours", hour=4)
    add_frequency("every six hours", "every 6 hours", hour=6)
    add_frequency("every eight hours", "every 8 hours", hour=8)
    add_frequency("every twelve hours", "every 12 hours", hour=12)
    
    add_frequency("every two days", "every 2 days", day=2)
    add_frequency("every three days", "every 3 days", day=3)
    add_frequency("every four days", "every 4 days", day=4)
    add_frequency("every five days", "every 5 days", day=5)
    add_frequency("every six days", "every 6 days", day=6)
    
    add_frequency("every two weeks", "every 2 weeks", week=2)
    add_frequency("every three weeks", "every 3 weeks", week=3)
    add_frequency("every four weeks", "every 4 weeks", week=4)
    
    add_frequency("every two months", "every 2 months", month=2)
    add_frequency("every three months", "every 3 months", month=3, quarter=1)
    add_frequency("every four months", "every 4 months", month=4)
    add_frequency("every six months", "every 6 months", month=6, year=0.5)
    
    add_frequency("every other day", "every 2 days", day=2)
    add_frequency("every other week", "every 2 weeks", week=2)
    add_frequency("every other month", "every 2 months", month=2)
    add_frequency("every other year", "every 2 years", year=2)
    
    # Specific day frequencies
    add_frequency("every Monday", "every Monday", week=1, specific_day="Monday")
    add_frequency("every Tuesday", "every Tuesday", week=1, specific_day="Tuesday")
    add_frequency("every Wednesday", "every Wednesday", week=1, specific_day="Wednesday")
    add_frequency("every Thursday", "every Thursday", week=1, specific_day="Thursday")
    add_frequency("every Friday", "every Friday", week=1, specific_day="Friday")
    add_frequency("every Saturday", "every Saturday", week=1, specific_day="Saturday")
    add_frequency("every Sunday", "every Sunday", week=1, specific_day="Sunday")
    
    add_frequency("every weekday", "every weekday", day=1, frequency_type="weekday")
    add_frequency("every weekend", "every weekend", week=1, frequency_type="weekend")
    add_frequency("every business day", "every business day", day=1, frequency_type="business_day")
    add_frequency("every working day", "every working day", day=1, frequency_type="business_day")
    
    # Approximate frequencies
    add_frequency("constantly", "constantly", frequency_type="approximate", minute=1, approximation="very high")
    add_frequency("continuously", "continuously", frequency_type="approximate", minute=1, approximation="very high")
    add_frequency("all the time", "all the time", frequency_type="approximate", minute=1, approximation="very high")
    add_frequency("frequently", "frequently", frequency_type="approximate", hour=1, approximation="high")
    add_frequency("regularly", "regularly", frequency_type="approximate", day=1, approximation="medium")
    add_frequency("often", "often", frequency_type="approximate", hour=4, approximation="medium")
    add_frequency("occasionally", "occasionally", frequency_type="approximate", week=1, approximation="low")
    add_frequency("sometimes", "sometimes", frequency_type="approximate", day=3, approximation="low")
    add_frequency("rarely", "rarely", frequency_type="approximate", month=1, approximation="very low")
    add_frequency("seldom", "seldom", frequency_type="approximate", month=2, approximation="very low")
    add_frequency("hardly ever", "hardly ever", frequency_type="approximate", month=3, approximation="very low")
    add_frequency("almost never", "almost never", frequency_type="approximate", month=6, approximation="extremely low")
    add_frequency("never", "never", frequency_type="approximate", year=100, approximation="never")
    
    # Specific time-based
    add_frequency("every morning", "every morning", day=1, period="morning")
    add_frequency("every afternoon", "every afternoon", day=1, period="afternoon")
    add_frequency("every evening", "every evening", day=1, period="evening")
    add_frequency("every night", "every night", day=1, period="night")
    
    # Numeric frequencies (X times)
    add_frequency("once", "once", frequency_type="unspecified", number_of_occurrences=1)
    add_frequency("once a day", "daily", day=1, number_of_occurrences=1)
    add_frequency("once a week", "weekly", week=1, number_of_occurrences=1)
    add_frequency("once a month", "monthly", month=1, number_of_occurrences=1)
    add_frequency("once a year", "yearly", year=1, number_of_occurrences=1)
    add_frequency("once daily", "daily", day=1, number_of_occurrences=1)
    add_frequency("once weekly", "weekly", week=1, number_of_occurrences=1)
    add_frequency("once monthly", "monthly", month=1, number_of_occurrences=1)
    add_frequency("once yearly", "yearly", year=1, number_of_occurrences=1)
    add_frequency("once annually", "yearly", year=1, number_of_occurrences=1)
    
    # Specific numeric intervals
    add_frequency("every 15 minutes", "every 15 minutes", minute=15)
    add_frequency("every 30 minutes", "every 30 minutes", minute=30, hour=0.5)
    add_frequency("every 45 minutes", "every 45 minutes", minute=45, hour=0.75)
    add_frequency("every 60 minutes", "hourly", hour=1, minute=60)
    add_frequency("every 90 minutes", "every 90 minutes", minute=90, hour=1.5)
    add_frequency("every 120 minutes", "every 2 hours", hour=2, minute=120)
    
    # Other common expressions
    add_frequency("around the clock", "around the clock", frequency_type="continuous", hour=1)
    add_frequency("24/7", "24/7", frequency_type="continuous", hour=1)
    add_frequency("24-7", "24/7", frequency_type="continuous", hour=1)
    add_frequency("all day every day", "all day every day", frequency_type="continuous", hour=1)
    add_frequency("periodically", "periodically", frequency_type="approximate", day=1, approximation="medium")
    add_frequency("intermittently", "intermittently", frequency_type="approximate", hour=4, approximation="medium")
    add_frequency("sporadically", "sporadically", frequency_type="approximate", week=1, approximation="low")
    add_frequency("on a regular basis", "on a regular basis", frequency_type="approximate", day=1, approximation="medium")
    add_frequency("on and off", "on and off", frequency_type="approximate", hour=4, approximation="medium")
    add_frequency("from time to time", "from time to time", frequency_type="approximate", week=1, approximation="low")
    add_frequency("now and then", "now and then", frequency_type="approximate", week=2, approximation="low")
    add_frequency("once in a while", "once in a while", frequency_type="approximate", month=1, approximation="very low")
    add_frequency("once in a blue moon", "once in a blue moon", frequency_type="approximate", year=1, approximation="extremely low")
    
    # Multiple times per week
    add_frequency("Monday and Wednesday", "Monday and Wednesday", week=1, number_of_occurrences=2, 
                 specific_day="Monday,Wednesday", frequency_type="specific_days")
    add_frequency("Tuesday and Thursday", "Tuesday and Thursday", week=1, number_of_occurrences=2, 
                 specific_day="Tuesday,Thursday", frequency_type="specific_days")
    add_frequency("Monday, Wednesday, and Friday", "Monday, Wednesday, Friday", week=1, number_of_occurrences=3, 
                 specific_day="Monday,Wednesday,Friday", frequency_type="specific_days")
    add_frequency("weekends", "weekends", week=1, number_of_occurrences=2, 
                 specific_day="Saturday,Sunday", frequency_type="weekend")
    
    # Generate numeric expressions (every X minutes/hours)
    for num in [5, 10, 15, 20, 30, 45]:
        add_frequency(f"every {num} minutes", f"every {num} minutes", minute=num)
    
    for num in [1, 2, 3, 4, 6, 8, 12]:
        add_frequency(f"every {num} hours", f"every {num} hours", hour=num)
    
    # Create variations with number words
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30
    }
    
    # Every X time_units with word numbers
    for word, num in number_words.items():
        # Hours
        if num <= 12:
            add_frequency(f"every {word} hours", f"every {num} hours", hour=num)
            add_frequency(f"every {word} hour" if num == 1 else f"every {word} hours", 
                         f"every {num} hours", hour=num)
        
        # Days
        if num <= 10:
            add_frequency(f"every {word} days", f"every {num} days", day=num)
            add_frequency(f"every {word} day" if num == 1 else f"every {word} days", 
                         f"every {num} days", day=num)
        
        # Weeks
        if num <= 5:
            add_frequency(f"every {word} weeks", f"every {num} weeks", week=num)
            add_frequency(f"every {word} week" if num == 1 else f"every {word} weeks", 
                         f"every {num} weeks", week=num)
        
        # Months
        if num <= 12:
            add_frequency(f"every {word} months", f"every {num} months", month=num)
            add_frequency(f"every {word} month" if num == 1 else f"every {word} months", 
                         f"every {num} months", month=num)
        
        # Years
        if num <= 10:
            add_frequency(f"every {word} years", f"every {num} years", year=num)
            add_frequency(f"every {word} year" if num == 1 else f"every {word} years", 
                         f"every {num} years", year=num)
    
    # Create the final JSON object
    frequency_json = {
        "description": "How often something occurs, with breakdown into time units",
        "examples": ["daily", "weekly", "every Monday", "twice a month", "annually", "frequently"],
        "values": frequencies,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return frequency_json

# Generate the JSON data
json_data = generate_frequency_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/frequency/vocabulary/frequency.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} frequency expressions and saved to frequency.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["daily", "weekly", "every Monday", "twice a month", "annually", "frequently"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')