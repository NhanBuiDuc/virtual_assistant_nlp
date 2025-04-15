import json

def generate_months_json():
    """
    Generate a JSON file with month references as commonly spoken by people.
    Each key is a verbal reference, and the value is the actual month.
    """
    # Standard months
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    month_variations = {}
    
    # Full names
    for month in months:
        month_variations[month] = month
    
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
    month_variations.update(abbreviations)
    
    # Ordinal references (first month, second month, etc.)
    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", 
                "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    
    for i, ordinal in enumerate(ordinals):
        month_variations[f"{ordinal} month"] = months[i]
        month_variations[f"{ordinal} month of the year"] = months[i]
        month_variations[f"the {ordinal} month"] = months[i]
        month_variations[f"the {ordinal} month of the year"] = months[i]
    
    # Numeric references
    for i in range(1, 13):
        month_variations[f"month {i}"] = months[i-1]
        month_variations[f"month {i} of the year"] = months[i-1]
    
    # Special references
    month_variations["first month of the year"] = "January"
    month_variations["last month of the year"] = "December"
    month_variations["last month"] = "December"
    month_variations["middle of the year"] = "June"  # Approximation
    month_variations["mid-year"] = "June"
    month_variations["beginning of the year"] = "January"
    month_variations["end of the year"] = "December"
    
    # Seasons (approximate month associations)
    month_variations["winter"] = "January"  # Northern hemisphere approximation
    month_variations["spring"] = "April"  
    month_variations["summer"] = "July"   
    month_variations["fall"] = "October"  
    month_variations["autumn"] = "October"
    
    # Create the final JSON object
    months_json = {
        "description": "Calendar months as commonly spoken",
        "examples": months,
        "values": month_variations
    }
    
    return months_json

# Generate the JSON data
json_data = generate_months_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/dates/months/vocabulary/months.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} month variations and saved to months.json")