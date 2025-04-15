import json

def generate_time_periods_json():
    """
    Generate a JSON file with time period expressions as commonly spoken.
    Each key is a verbal reference to a part of the day, and the value is the standardized period.
    """
    time_periods = {
        # Basic time periods
        "morning": "morning",
        "afternoon": "afternoon",
        "evening": "evening",
        "night": "night",
        "nighttime": "night",
        "dawn": "dawn",
        "dusk": "dusk",
        "sunrise": "dawn",
        "sunset": "dusk",
        "daybreak": "dawn",
        "twilight": "dusk",
        "sundown": "dusk",
        "sunup": "dawn",
        "midnight": "midnight",
        "noon": "noon",
        "midday": "noon",
        
        # Specific parts of periods
        "early morning": "early morning",
        "late morning": "late morning",
        "early afternoon": "early afternoon",
        "late afternoon": "late afternoon",
        "early evening": "early evening",
        "late evening": "late evening",
        "early night": "early night",
        "late night": "late night",
        "middle of the night": "middle of the night",
        "dead of night": "middle of the night",
        
        # Time ranges with "in the"
        "in the morning": "morning",
        "in the afternoon": "afternoon",
        "in the evening": "evening",
        "in the night": "night",
        "at night": "night",
        "at dawn": "dawn",
        "at dusk": "dusk",
        "at sunrise": "dawn",
        "at sunset": "dusk",
        "at daybreak": "dawn",
        "at twilight": "dusk",
        "at midnight": "midnight",
        "at noon": "noon",
        
        # Beginning and end references
        "beginning of the day": "early morning",
        "start of the day": "early morning",
        "end of the day": "late evening",
        "close of day": "late evening",
        "start of morning": "early morning",
        "end of morning": "late morning",
        "start of afternoon": "early afternoon",
        "end of afternoon": "late afternoon",
        "start of evening": "early evening",
        "end of evening": "late evening",
        "start of night": "early night",
        "end of night": "late night",
        
        # Other common expressions
        "break of day": "dawn",
        "crack of dawn": "dawn",
        "first light": "dawn",
        "wee hours": "early morning",
        "small hours": "early morning",
        "wee hours of the morning": "early morning",
        "before sunrise": "early morning",
        "after sunset": "evening",
        "before midnight": "late evening",
        "after midnight": "early morning",
        "pre-dawn": "early morning",
        "post-dusk": "evening",
        
        # Time-specific references
        "breakfast time": "morning",
        "lunch time": "noon",
        "dinner time": "evening",
        "bedtime": "night",
        "sleeping hours": "night",
        "working hours": "daytime",
        "business hours": "daytime",
        
        # Day divisions
        "daytime": "daytime",
        "day time": "daytime",
        "nighttime": "night",
        "night time": "night",
        "overnight": "night",
        "during the day": "daytime",
        "during the night": "night",
        
        # Poetic/literary terms
        "witching hour": "midnight",
        "golden hour": "sunset",
        "blue hour": "dusk",
        "gloaming": "dusk",
        
        # Other variations
        "first thing in the morning": "early morning",
        "last thing at night": "late night",
        "bright and early": "early morning",
        "at the crack of dawn": "dawn",
        "when the sun comes up": "dawn",
        "when the sun goes down": "dusk",
        "after dark": "night",
        "before dark": "evening",
        "as the day ends": "evening",
        "as night falls": "evening",
        "the stroke of midnight": "midnight",
        "high noon": "noon"
    }
    
    # Create the final JSON object
    time_periods_json = {
        "description": "General parts of the day as commonly referenced in conversation",
        "examples": ["morning", "afternoon", "evening", "night", "dawn", "dusk"],
        "values": time_periods
    }
    
    return time_periods_json

# Generate the JSON data
json_data = generate_time_periods_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/time_periods/vocabulary/time_periods.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} time period expressions and saved to time_periods.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["morning", "at sunset", "end of the day", "wee hours", "after dark", "first thing in the morning"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": "{json_data["values"][key]}"')