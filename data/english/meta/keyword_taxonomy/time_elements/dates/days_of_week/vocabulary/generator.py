import json

def generate_days_of_week_json():
    """
    Generate a simple JSON file with days of the week as spoken by humans.
    """
    # Standard days of the week
    standard_days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    
    # Common spoken variations
    spoken_variations = {
        # Full names (standard)
        "Monday": "Monday",
        "Tuesday": "Tuesday",
        "Wednesday": "Wednesday",
        "Thursday": "Thursday",
        "Friday": "Friday",
        "Saturday": "Saturday",
        "Sunday": "Sunday",
        
        # Common abbreviations
        "Mon": "Monday",
        "Tue": "Tuesday",
        "Tues": "Tuesday",
        "Wed": "Wednesday",
        "Weds": "Wednesday",
        "Thu": "Thursday",
        "Thur": "Thursday",
        "Thurs": "Thursday",
        "Fri": "Friday",
        "Sat": "Saturday",
        "Sun": "Sunday",
        
        # Contextual terms
        "weekday": "weekday",
        "weekend": "weekend",
        "workday": "workday",
        "business day": "business day"
    }
    
    # Create the final JSON object
    days_of_week_json = {
        "description": "Specific days of the week as commonly spoken",
        "examples": standard_days,
        "values": spoken_variations
    }
    
    return days_of_week_json

# Generate the JSON data
json_data = generate_days_of_week_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/dates/days_of_week/vocabulary/days_of_week.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} day of week variations and saved to days_of_week.json")