import json
import os
from datetime import datetime

def generate_months_json():
    """
    Generate a JSON file with month references as commonly spoken by people.
    Each entry includes the standard form and the month_in_year attribute.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    month_variations = {}
    
    # Helper function to add month with incremented ID
    def add_month(key, standard_form, month_in_year):
        nonlocal id_counter
        month_variations[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "month_in_year": month_in_year
        }
        id_counter += 1
    
    # Standard months with numeric positions
    months = [
        {"name": "January", "position": 1},
        {"name": "February", "position": 2},
        {"name": "March", "position": 3},
        {"name": "April", "position": 4},
        {"name": "May", "position": 5},
        {"name": "June", "position": 6},
        {"name": "July", "position": 7},
        {"name": "August", "position": 8},
        {"name": "September", "position": 9},
        {"name": "October", "position": 10},
        {"name": "November", "position": 11},
        {"name": "December", "position": 12}
    ]
    
    # Full names
    for month in months:
        add_month(month["name"], month["name"], month["position"])
    
    # Common abbreviations
    abbreviations = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Sept": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }
    
    for abbr, month_name in abbreviations.items():
        month_position = next(m["position"] for m in months if m["name"] == month_name)
        add_month(abbr, month_name, month_position)
    
    # Ordinal references (first month, second month, etc.)
    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", 
                "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    
    for i, ordinal in enumerate(ordinals):
        add_month(f"{ordinal} month", months[i]["name"], i+1)
        add_month(f"{ordinal} month of the year", months[i]["name"], i+1)
        add_month(f"the {ordinal} month", months[i]["name"], i+1)
        add_month(f"the {ordinal} month of the year", months[i]["name"], i+1)
    
    # Numeric references
    for i in range(1, 13):
        add_month(f"month {i}", months[i-1]["name"], i)
        add_month(f"month {i} of the year", months[i-1]["name"], i)
    
    # Special references
    add_month("first month of the year", "January", 1)
    add_month("last month of the year", "December", 12)
    add_month("last month", "December", 12)
    add_month("middle of the year", "June", 6)  # Approximation
    add_month("mid-year", "June", 6)
    add_month("beginning of the year", "January", 1)
    add_month("end of the year", "December", 12)
    
    # Seasons (approximate month associations)
    add_month("winter", "January", 1)  # Northern hemisphere approximation
    add_month("spring", "April", 4)  
    add_month("summer", "July", 7)   
    add_month("fall", "October", 10)  
    add_month("autumn", "October", 10)
    
    # Create the final JSON object
    months_json = {
        "description": "Calendar months as commonly spoken",
        "examples": ["January", "February", "March", "April", "May", "June", 
                     "July", "August", "September", "October", "November", "December"],
        "values": month_variations,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return months_json

# Generate the JSON data
json_data = generate_months_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/dates/months/vocabulary/months.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} month variations and saved to months.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["January", "Apr", "third month", "month 7", "winter"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')