import json

def generate_frequency_json():
    """
    Generate a JSON file with frequency expressions.
    Each key is a verbal expression, and the value is the frequency in minutes between occurrences.
    """
    frequencies = {}
    
    # Constants for time calculations
    MINUTE = 1
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    WEEK = 7 * DAY
    MONTH = 30 * DAY  # Approximation
    QUARTER = 3 * MONTH
    YEAR = 365 * DAY  # Approximation
    
    # Basic frequencies (adverbs)
    basic_frequencies = {
        "hourly": HOUR,
        "daily": DAY,
        "nightly": DAY,
        "weekly": WEEK,
        "bi-weekly": 2 * WEEK,
        "biweekly": 2 * WEEK,
        "fortnightly": 2 * WEEK,
        "monthly": MONTH,
        "quarterly": QUARTER,
        "yearly": YEAR,
        "annually": YEAR,
        
        # Common expressions
        "every hour": HOUR,
        "every day": DAY,
        "every night": DAY,
        "every week": WEEK,
        "every month": MONTH,
        "every year": YEAR,
        
        # Multiples per period
        "twice a day": DAY / 2,
        "twice daily": DAY / 2,
        "twice a week": WEEK / 2,
        "twice weekly": WEEK / 2,
        "twice a month": MONTH / 2,
        "twice monthly": MONTH / 2,
        "twice a year": YEAR / 2,
        "twice yearly": YEAR / 2,
        "twice annually": YEAR / 2,
        
        "three times a day": DAY / 3,
        "three times a week": WEEK / 3,
        "three times a month": MONTH / 3,
        "three times a year": YEAR / 3,
        
        "four times a day": DAY / 4,
        "four times a week": WEEK / 4,
        "four times a month": MONTH / 4,
        "four times a year": YEAR / 4,
        
        # Every X hours/days/weeks/months
        "every two hours": 2 * HOUR,
        "every three hours": 3 * HOUR,
        "every four hours": 4 * HOUR,
        "every six hours": 6 * HOUR,
        "every eight hours": 8 * HOUR,
        "every twelve hours": 12 * HOUR,
        
        "every two days": 2 * DAY,
        "every three days": 3 * DAY,
        "every four days": 4 * DAY,
        "every five days": 5 * DAY,
        "every six days": 6 * DAY,
        
        "every two weeks": 2 * WEEK,
        "every three weeks": 3 * WEEK,
        "every four weeks": 4 * WEEK,
        
        "every two months": 2 * MONTH,
        "every three months": 3 * MONTH,
        "every four months": 4 * MONTH,
        "every six months": 6 * MONTH,
        
        "every other day": 2 * DAY,
        "every other week": 2 * WEEK,
        "every other month": 2 * MONTH,
        "every other year": 2 * YEAR,
        
        # Specific day frequencies
        "every Monday": WEEK,
        "every Tuesday": WEEK,
        "every Wednesday": WEEK,
        "every Thursday": WEEK,
        "every Friday": WEEK,
        "every Saturday": WEEK,
        "every Sunday": WEEK,
        
        "every weekday": DAY,
        "every weekend": WEEK,
        "every business day": DAY,
        "every working day": DAY,
        
        # Approximate frequencies
        "constantly": MINUTE,
        "continuously": MINUTE,
        "all the time": MINUTE,
        "frequently": HOUR,
        "regularly": DAY,
        "often": 4 * HOUR,
        "occasionally": WEEK,
        "sometimes": 3 * DAY,
        "rarely": MONTH,
        "seldom": 2 * MONTH,
        "hardly ever": 3 * MONTH,
        "almost never": 6 * MONTH,
        "never": YEAR * 100,  # Practical "never"
        
        # Specific time-based
        "every morning": DAY,
        "every afternoon": DAY,
        "every evening": DAY,
        "every night": DAY,
        
        # Numeric frequencies (X times)
        "once": YEAR,  # Default for "once" without context
        "once a day": DAY,
        "once a week": WEEK,
        "once a month": MONTH,
        "once a year": YEAR,
        "once daily": DAY,
        "once weekly": WEEK,
        "once monthly": MONTH,
        "once yearly": YEAR,
        "once annually": YEAR,
        
        # Specific numeric intervals
        "every 15 minutes": 15 * MINUTE,
        "every 30 minutes": 30 * MINUTE,
        "every 45 minutes": 45 * MINUTE,
        "every 60 minutes": 60 * MINUTE,
        "every 90 minutes": 90 * MINUTE,
        "every 120 minutes": 120 * MINUTE,
        
        # Other common expressions
        "around the clock": HOUR,
        "24/7": HOUR,
        "24-7": HOUR,
        "all day every day": HOUR,
        "periodically": DAY,
        "intermittently": 4 * HOUR,
        "sporadically": WEEK,
        "on a regular basis": DAY,
        "on and off": 4 * HOUR,
        "from time to time": WEEK,
        "now and then": 2 * WEEK,
        "once in a while": MONTH,
        "once in a blue moon": YEAR,
        
        # Multiple times per week
        "Monday and Wednesday": WEEK / 2,
        "Tuesday and Thursday": WEEK / 2,
        "Monday, Wednesday, and Friday": WEEK / 3,
        "weekends": WEEK / 2,  # Saturday and Sunday
    }
    
    frequencies.update(basic_frequencies)
    
    # Generate numeric expressions (every X minutes/hours)
    for num in [5, 10, 15, 20, 30, 45]:
        frequencies[f"every {num} minutes"] = num * MINUTE
    
    for num in [1, 2, 3, 4, 6, 8, 12]:
        frequencies[f"every {num} hours"] = num * HOUR
    
    # Create variations with number words
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30
    }
    
    time_units = {
        "minute": MINUTE,
        "minutes": MINUTE,
        "hour": HOUR,
        "hours": HOUR,
        "day": DAY,
        "days": DAY,
        "week": WEEK,
        "weeks": WEEK,
        "month": MONTH,
        "months": MONTH,
        "year": YEAR,
        "years": YEAR
    }
    
    # Every X time_units
    for word, num in number_words.items():
        for unit, value in time_units.items():
            frequencies[f"every {word} {unit}"] = num * value
    
    # Create the final JSON object
    frequency_json = {
        "description": "How often something occurs, with values in minutes between occurrences",
        "examples": ["daily", "weekly", "every Monday", "twice a month", "annually", "frequently"],
        "values": frequencies
    }
    
    return frequency_json

# Generate the JSON data
json_data = generate_frequency_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/frequency/vocabulary/frequency.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} frequency expressions and saved to frequency.json")

# Print some examples
print("\nSample entries (frequency in minutes between occurrences):")
sample_keys = ["daily", "weekly", "every Monday", "twice a month", "annually", "frequently"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json_data["values"][key]}')