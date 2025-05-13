import json
import os
from datetime import datetime

def generate_specific_times_json():
    """
    Generate a JSON file with various verbal expressions of specific dates.
    Each entry includes a verbalization of a date with its standard form (DD/MM).
    """
    # Counter for simple ID generation
    id_counter = 1
    
    specific_times = {}
    
    # Helper function to add a specific time with incremented ID
    def add_specific_time(key, standard_form, month=None, day=None, 
                         description=None, variants=None):
        """
        Add a specific time with structured metadata
        """
        nonlocal id_counter
        specific_times[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "month": month,
            "day": day,
            "description": description,
            "variants": variants or []
        }
        id_counter += 1
    
    # Mapping for ordinal suffixes
    ordinal_suffixes = {
        1: "st", 2: "nd", 3: "rd", 21: "st", 22: "nd", 23: "rd", 31: "st"
    }
    
    # Get the ordinal suffix for a number
    def get_ordinal(day):
        if day in ordinal_suffixes:
            return f"{day}{ordinal_suffixes[day]}"
        return f"{day}th"
    
    # Get the ordinal word for a number
    def get_ordinal_word(day):
        words = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", 
                 "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", 
                 "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", 
                 "nineteenth", "twentieth", "twenty-first", "twenty-second", 
                 "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", 
                 "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth", 
                 "thirty-first"]
        return words[day-1] if 1 <= day <= 31 else str(day)
    
    # Month names
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    # Generate entries for all days and months
    for month_idx, month_name in enumerate(months, 1):
        # Determine max days for the month (simplified)
        if month_idx in [4, 6, 9, 11]:  # Apr, Jun, Sep, Nov
            max_days = 30
        elif month_idx == 2:  # Feb
            max_days = 29  # Including leap year possibility
        else:
            max_days = 31
        
        for day in range(1, max_days + 1):
            # Standard form: DD/MM
            standard_form = f"{day:02d}/{month_idx:02d}"
            
            # Month abbreviation (first 3 letters)
            month_abbr = month_name[:3]
            
            # Format 1: [Ordinal] [Month]
            ordinal_month = f"{get_ordinal(day)} {month_name}"
            description = f"The {get_ordinal_word(day)} day of {month_name}"
            
            variants = [
                f"{get_ordinal(day)} {month_abbr}",  # 1st Jan
                f"{get_ordinal(day)} of {month_name}",  # 1st of January
                f"{get_ordinal(day)} of {month_abbr}",  # 1st of Jan
                f"the {get_ordinal_word(day)} of {month_name}",  # the first of January
                f"the {get_ordinal_word(day)} of {month_abbr}"  # the first of Jan
            ]
            
            # Add the main entry
            add_specific_time(ordinal_month, standard_form, month=month_idx, day=day, 
                             description=description, variants=variants)
            
            # Format 2: [Month] [Ordinal]
            month_ordinal = f"{month_name} {get_ordinal(day)}"
            variants = [
                f"{month_abbr} {get_ordinal(day)}",  # Jan 1st
                f"{month_name} the {get_ordinal_word(day)}",  # January the first
                f"{month_abbr} the {get_ordinal_word(day)}"  # Jan the first
            ]
            
            # Add the alternative format
            add_specific_time(month_ordinal, standard_form, month=month_idx, day=day, 
                             description=description, variants=variants)
            
            # Format 3: [Month] [Ordinal word]
            if day <= 31:  # Only add if we have the ordinal word
                month_ordinal_word = f"{month_name} {get_ordinal_word(day)}"
                
                # Only add if not already the same as previous entry
                if month_ordinal_word != month_ordinal:
                    variants = [
                        f"{month_abbr} {get_ordinal_word(day)}"  # Jan first
                    ]
                    
                    # Add the word-based format
                    add_specific_time(month_ordinal_word, standard_form, month=month_idx, day=day, 
                                     description=description, variants=variants)
    
    # Create the final JSON object
    specific_times_json = {
        "description": "Specific dates as commonly referenced in conversation",
        "examples": ["1st January", "January 1st", "third September", "October 15th"],
        "values": specific_times,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return specific_times_json

# Generate the JSON data
json_data = generate_specific_times_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/specific_times/vocabulary/specific_time.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} specific date expressions and saved to specific_time.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["1st January", "January 1st", "third September", "15th October", 
               "First January", "January first", "25th December", "December twenty-fifth"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')
    else:
        # Try finding a case-insensitive match
        matches = [k for k in json_data["values"].keys() if k.lower() == key.lower()]
        if matches:
            print(f'"{matches[0]}": {json.dumps(json_data["values"][matches[0]], indent=2)}')
        else:
            print(f'"{key}": Not found in generated data')