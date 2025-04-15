import json

def generate_durations_json():
    """
    Generate a JSON file with time duration expressions.
    Each key is a verbal expression, and the value is the duration in minutes.
    Limited to durations of a week or less.
    """
    durations = {}
    
    # Constants for time calculations
    MINUTE = 1
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    WEEK = 7 * DAY
    
    # Basic time units with singular and plural forms
    time_units = {
        "second": MINUTE / 60,
        "seconds": MINUTE / 60,
        "minute": MINUTE,
        "minutes": MINUTE,
        "hour": HOUR,
        "hours": HOUR,
        "day": DAY,
        "days": DAY,
        "week": WEEK,
        "weeks": WEEK
    }
    
    # Number words with their numeric values (1-20)
    number_words = {
        "a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        "half": 0.5, "quarter": 0.25, "couple": 2, "few": 3
    }
    
    # Simple number-unit combinations
    for number_word, number_value in number_words.items():
        for unit, unit_value in time_units.items():
            # Skip singular forms with numbers other than 1
            if unit.endswith('s') or number_value == 1:
                duration_value = int(number_value * unit_value)
                
                # Skip zero values or very small values (less than a minute)
                if duration_value > 0:
                    # Various formats
                    durations[f"{number_word} {unit}"] = duration_value
                    durations[f"for {number_word} {unit}"] = duration_value
                    durations[f"{number_word}-{unit}"] = duration_value
                    
                    # "for the next X units"
                    if number_value >= 1:
                        durations[f"for the next {number_word} {unit}"] = duration_value
    
    # Numeric values (1-100)
    for num in range(1, 101):
        # Only include common numbers to keep the list manageable
        if num <= 20 or num % 5 == 0 or num == 24 or num == 48 or num == 72 or num == 96:
            for unit, unit_value in time_units.items():
                duration_value = int(num * unit_value)
                
                # Skip very small values (less than a minute)
                if duration_value > 0:
                    durations[f"{num} {unit}"] = duration_value
                    durations[f"for {num} {unit}"] = duration_value
                    durations[f"{num}-{unit}"] = duration_value
                    
                    # "for the next X units"
                    durations[f"for the next {num} {unit}"] = duration_value
    
    # Special hour references (24, 48, 72 hours)
    for hours in [24, 48, 72]:
        durations[f"{hours} hours"] = hours * HOUR
        durations[f"for {hours} hours"] = hours * HOUR
        durations[f"for the next {hours} hours"] = hours * HOUR
    
    # Common expressions
    common_expressions = {
        "a moment": 1,
        "a minute": MINUTE,
        "a couple of minutes": 2 * MINUTE,
        "a few minutes": 3 * MINUTE,
        "several minutes": 5 * MINUTE,
        "half an hour": 30 * MINUTE,
        "an hour": HOUR,
        "an hour and a half": 90 * MINUTE,
        "a couple of hours": 2 * HOUR,
        "a few hours": 3 * HOUR,
        "several hours": 4 * HOUR,
        "half a day": 12 * HOUR,
        "all day": DAY,
        "a day": DAY,
        "a day and a half": 36 * HOUR,
        "a couple of days": 2 * DAY,
        "a few days": 3 * DAY,
        "several days": 4 * DAY,
        "almost a week": 6 * DAY,
        "a week": WEEK,
        
        "morning": 3 * HOUR,  # Approximate duration
        "afternoon": 6 * HOUR,  # Approximate duration
        "evening": 3 * HOUR,  # Approximate duration
        "night": 8 * HOUR,  # Approximate duration
        "overnight": 12 * HOUR,  # Approximate duration
        "all morning": 5 * HOUR,
        "all afternoon": 6 * HOUR,
        "all evening": 5 * HOUR,
        "all night": 10 * HOUR,
        "all day long": DAY,
        "the whole day": DAY,
        "the entire day": DAY,
        "the whole week": WEEK,
        "the entire week": WEEK
    }
    
    # Add the common expressions with "for" prefix
    for expr, value in list(common_expressions.items()):
        common_expressions[f"for {expr}"] = value
    
    durations.update(common_expressions)
    
    # Add some specific time ranges
    time_ranges = {
        "for the morning": 3 * HOUR,
        "for the afternoon": 6 * HOUR,
        "for the evening": 3 * HOUR,
        "for the night": 8 * HOUR,
        "until morning": 12 * HOUR,
        "until tomorrow": 12 * HOUR,
        "until tonight": 8 * HOUR,
        "until tomorrow morning": 16 * HOUR,
        "until next week": WEEK,
        "for the rest of the day": 8 * HOUR,  # Approximate
        "for the rest of the week": 3 * DAY,  # Approximate
    }
    durations.update(time_ranges)
    
    # Create the final JSON object
    durations_json = {
        "description": "Time spans with values in minutes",
        "examples": ["for an hour", "30 minutes", "all day", "overnight", "for a week", "two-hour"],
        "values": durations
    }
    
    return durations_json

# Generate the JSON data
json_data = generate_durations_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/durations/vocabulary/durations.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} duration expressions and saved to durations.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["30 minutes", "for an hour", "all day", "overnight", "two days", "for the next 24 hours"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json_data["values"][key]} minutes')