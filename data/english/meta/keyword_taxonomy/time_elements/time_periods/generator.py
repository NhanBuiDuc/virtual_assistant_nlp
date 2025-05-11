import json
import os
from datetime import datetime

def generate_time_periods_json():
    """
    Generate a JSON file with time period expressions as commonly spoken.
    Each entry includes a breakdown of when the time period occurs with approximate hours.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    time_periods = {}
    
    # Helper function to add a time period with incremented ID
    def add_time_period(key, standard_form, start_hour=None, end_hour=None, 
                       qualifier=None, daylight=None, description=None):
        """
        Add a time period with structured metadata
        """
        nonlocal id_counter
        time_periods[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "start_hour": start_hour,
            "end_hour": end_hour,
            "qualifier": qualifier,
            "daylight": daylight,
            "description": description
        }
        id_counter += 1
    
    # Basic time periods
    add_time_period("morning", "morning", 6, 12, daylight=True, 
                   description="Period from sunrise until noon")
    
    add_time_period("afternoon", "afternoon", 12, 17, daylight=True, 
                   description="Period from noon until evening")
    
    add_time_period("evening", "evening", 17, 21, daylight=False, 
                   description="Period from end of afternoon until night")
    
    add_time_period("night", "night", 21, 6, daylight=False, 
                   description="Period from evening until morning")
    
    add_time_period("nighttime", "night", 21, 6, daylight=False, 
                   description="Period from evening until morning")
    
    add_time_period("dawn", "dawn", 5, 7, daylight=True, 
                   description="Period of sunrise/first light")
    
    add_time_period("dusk", "dusk", 17, 19, daylight=False, 
                   description="Period of sunset/last light")
    
    add_time_period("sunrise", "dawn", 5, 7, daylight=True, 
                   description="Time when sun appears on the horizon")
    
    add_time_period("sunset", "dusk", 17, 19, daylight=False, 
                   description="Time when sun disappears below the horizon")
    
    add_time_period("daybreak", "dawn", 5, 7, daylight=True, 
                   description="Beginning of day when light first appears")
    
    add_time_period("twilight", "dusk", 17, 19, daylight=False, 
                   description="Soft glowing light before full darkness")
    
    add_time_period("sundown", "dusk", 17, 19, daylight=False, 
                   description="Time when sun sets")
    
    add_time_period("sunup", "dawn", 5, 7, daylight=True, 
                   description="Time when sun rises")
    
    add_time_period("midnight", "midnight", 0, 0, daylight=False, 
                   description="Twelve o'clock at night")
    
    add_time_period("noon", "noon", 12, 12, daylight=True, 
                   description="Twelve o'clock in the day")
    
    add_time_period("midday", "noon", 12, 12, daylight=True, 
                   description="Middle of the day/noon")
    
    # Specific parts of periods
    add_time_period("early morning", "early morning", 6, 9, qualifier="early", daylight=True, 
                   description="First part of the morning")
    
    add_time_period("late morning", "late morning", 9, 12, qualifier="late", daylight=True, 
                   description="Later part of the morning")
    
    add_time_period("early afternoon", "early afternoon", 12, 14, qualifier="early", daylight=True, 
                   description="First part of the afternoon")
    
    add_time_period("late afternoon", "late afternoon", 14, 17, qualifier="late", daylight=True, 
                   description="Later part of the afternoon")
    
    add_time_period("early evening", "early evening", 17, 19, qualifier="early", daylight=False, 
                   description="First part of the evening")
    
    add_time_period("late evening", "late evening", 19, 21, qualifier="late", daylight=False, 
                   description="Later part of the evening")
    
    add_time_period("early night", "early night", 21, 0, qualifier="early", daylight=False, 
                   description="First part of the night")
    
    add_time_period("late night", "late night", 0, 3, qualifier="late", daylight=False, 
                   description="Later part of the night")
    
    add_time_period("middle of the night", "middle of the night", 0, 3, qualifier="middle", daylight=False, 
                   description="Period in the middle of the night, usually past midnight")
    
    add_time_period("dead of night", "middle of the night", 0, 3, qualifier="middle", daylight=False, 
                   description="Deepest, darkest part of night")
    
    # Time ranges with "in the"
    add_time_period("in the morning", "morning", 6, 12, daylight=True, 
                   description="Period from sunrise until noon")
    
    add_time_period("in the afternoon", "afternoon", 12, 17, daylight=True, 
                   description="Period from noon until evening")
    
    add_time_period("in the evening", "evening", 17, 21, daylight=False, 
                   description="Period from end of afternoon until night")
    
    add_time_period("in the night", "night", 21, 6, daylight=False, 
                   description="Period from evening until morning")
    
    add_time_period("at night", "night", 21, 6, daylight=False, 
                   description="Period from evening until morning")
    
    add_time_period("at dawn", "dawn", 5, 7, daylight=True, 
                   description="At the time of sunrise/first light")
    
    add_time_period("at dusk", "dusk", 17, 19, daylight=False, 
                   description="At the time of sunset/last light")
    
    add_time_period("at sunrise", "dawn", 5, 7, daylight=True, 
                   description="At the time when sun appears on horizon")
    
    add_time_period("at sunset", "dusk", 17, 19, daylight=False, 
                   description="At the time when sun disappears below horizon")
    
    add_time_period("at daybreak", "dawn", 5, 7, daylight=True, 
                   description="At the time when light first appears")
    
    add_time_period("at twilight", "dusk", 17, 19, daylight=False, 
                   description="At the time of soft glowing light before darkness")
    
    add_time_period("at midnight", "midnight", 0, 0, daylight=False, 
                   description="At twelve o'clock at night")
    
    add_time_period("at noon", "noon", 12, 12, daylight=True, 
                   description="At twelve o'clock in the day")
    
    # Beginning and end references
    add_time_period("beginning of the day", "early morning", 6, 8, qualifier="early", daylight=True, 
                   description="Start of the day, early morning")
    
    add_time_period("start of the day", "early morning", 6, 8, qualifier="early", daylight=True, 
                   description="Start of the day, early morning")
    
    add_time_period("end of the day", "late evening", 17, 21, qualifier="late", daylight=False, 
                   description="Final part of the day before night")
    
    add_time_period("close of day", "late evening", 17, 21, qualifier="late", daylight=False, 
                   description="Final part of the day before night")
    
    # Other common expressions
    add_time_period("break of day", "dawn", 5, 7, daylight=True, 
                   description="First appearance of light in the morning")
    
    add_time_period("crack of dawn", "dawn", 5, 6, daylight=True, 
                   description="Very early morning, as sun begins to rise")
    
    add_time_period("first light", "dawn", 5, 6, daylight=True, 
                   description="Earliest light in the morning")
    
    add_time_period("wee hours", "early morning", 1, 4, qualifier="early", daylight=False, 
                   description="Very early morning hours after midnight")
    
    add_time_period("small hours", "early morning", 1, 4, qualifier="early", daylight=False, 
                   description="Very early morning hours after midnight")
    
    add_time_period("before sunrise", "early morning", 4, 6, qualifier="early", daylight=False, 
                   description="Time just before the sun rises")
    
    add_time_period("after sunset", "evening", 18, 20, daylight=False, 
                   description="Time just after the sun sets")
    
    # Time-specific references
    add_time_period("breakfast time", "morning", 7, 9, daylight=True, 
                   description="Morning time typically for breakfast")
    
    add_time_period("lunch time", "noon", 12, 13, daylight=True, 
                   description="Midday time typically for lunch")
    
    add_time_period("dinner time", "evening", 18, 20, daylight=False, 
                   description="Evening time typically for dinner")
    
    add_time_period("bedtime", "night", 21, 23, daylight=False, 
                   description="Evening time typically for going to bed")
    
    add_time_period("working hours", "daytime", 9, 17, daylight=True, 
                   description="Hours during the day typically for work")
    
    add_time_period("business hours", "daytime", 9, 17, daylight=True, 
                   description="Hours during the day when businesses are open")
    
    # Day divisions
    add_time_period("daytime", "daytime", 6, 18, daylight=True, 
                   description="Period when there is natural light")
    
    add_time_period("day time", "daytime", 6, 18, daylight=True, 
                   description="Period when there is natural light")
    
    add_time_period("nighttime", "night", 18, 6, daylight=False, 
                   description="Period when it is dark")
    
    add_time_period("night time", "night", 18, 6, daylight=False, 
                   description="Period when it is dark")
    
    add_time_period("overnight", "night", 21, 6, daylight=False, 
                   description="During the night, especially while sleeping")
    
    # Other variations
    add_time_period("first thing in the morning", "early morning", 6, 8, qualifier="early", daylight=True, 
                   description="Very first part of the morning")
    
    add_time_period("last thing at night", "late night", 21, 23, qualifier="late", daylight=False, 
                   description="Final part of the day before sleep")
    
    add_time_period("bright and early", "early morning", 6, 8, qualifier="early", daylight=True, 
                   description="Very early in the morning")
    
    add_time_period("after dark", "night", 18, 6, daylight=False, 
                   description="Period after sunset when it's dark")
    
    add_time_period("before dark", "evening", 16, 18, daylight=True, 
                   description="Late afternoon/early evening before sunset")
    
    add_time_period("as the day ends", "evening", 17, 19, daylight=False, 
                   description="Late afternoon/early evening as daylight fades")
    
    add_time_period("the stroke of midnight", "midnight", 0, 0, daylight=False, 
                   description="Exactly 12:00 AM")
    
    add_time_period("high noon", "noon", 12, 12, daylight=True, 
                   description="Exactly 12:00 PM when sun is at highest point")
    
    # Create the final JSON object
    time_periods_json = {
        "description": "General parts of the day as commonly referenced in conversation",
        "examples": ["morning", "afternoon", "evening", "night", "dawn", "dusk"],
        "values": time_periods,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return time_periods_json

# Generate the JSON data
json_data = generate_time_periods_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/time_periods/vocabulary/time_periods.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} time period expressions and saved to time_periods.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["morning", "at sunset", "end of the day", "wee hours", "after dark", "first thing in the morning"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')