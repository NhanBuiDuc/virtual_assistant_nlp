import json

def generate_deadlines_json():
    """
    Generate a JSON file with deadline expressions as commonly spoken.
    Each key is a verbal reference to a deadline, and the value is a standardized form.
    """
    deadlines = {
        # Basic deadline terms
        "deadline": "deadline",
        "due date": "deadline",
        "due": "deadline",
        "cutoff": "deadline",
        "time limit": "deadline",
        
        # Common abbreviations
        "ASAP": "as soon as possible",
        "EOD": "end of day",
        "COB": "close of business",
        "EOP": "end of period",
        "EOB": "end of business",
        "EOW": "end of week",
        "EOM": "end of month",
        "EOQ": "end of quarter",
        "EOY": "end of year",
        
        # Time-based deadlines
        "by morning": "by morning",
        "by noon": "by noon",
        "by afternoon": "by afternoon",
        "by evening": "by evening",
        "by night": "by night",
        "by midnight": "by midnight",
        "before morning": "before morning",
        "before noon": "before noon",
        "before afternoon": "before afternoon",
        "before evening": "before evening",
        "before night": "before night",
        "before midnight": "before midnight",
        
        # Day-based deadlines with "by"
        "by today": "by today",
        "by tomorrow": "by tomorrow",
        "by Monday": "by Monday",
        "by Tuesday": "by Tuesday",
        "by Wednesday": "by Wednesday",
        "by Thursday": "by Thursday",
        "by Friday": "by Friday",
        "by Saturday": "by Saturday",
        "by Sunday": "by Sunday",
        "by next week": "by next week",
        "by next month": "by next month",
        "by next year": "by next year",
        
        # Day-based deadlines with "due"
        "due today": "due today",
        "due tomorrow": "due tomorrow",
        "due Monday": "due Monday",
        "due Tuesday": "due Tuesday",
        "due Wednesday": "due Wednesday",
        "due Thursday": "due Thursday",
        "due Friday": "due Friday",
        "due Saturday": "due Saturday",
        "due Sunday": "due Sunday",
        "due next week": "due next week",
        "due next month": "due next month",
        
        # End of period expressions
        "end of day": "end of day",
        "end of business": "end of business",
        "close of business": "close of business",
        "end of week": "end of week",
        "end of month": "end of month",
        "end of quarter": "end of quarter",
        "end of year": "end of year",
        "close of day": "end of day",
        "by the end of day": "end of day",
        "by the end of business": "end of business",
        "by the end of the week": "end of week",
        "by the end of the month": "end of month",
        "by the end of the quarter": "end of quarter",
        "by the end of the year": "end of year",
        
        # Urgency expressions
        "as soon as possible": "as soon as possible",
        "immediately": "immediately",
        "right away": "immediately",
        "right now": "immediately",
        "at once": "immediately",
        "without delay": "immediately",
        "STAT": "immediately",
        "urgent": "urgent",
        "top priority": "urgent",
        "high priority": "urgent",
        "rush": "urgent",
        "expedite": "urgent",
        "time-sensitive": "urgent",
        
        # Specific time expressions
        "by 5 PM": "by specific time",
        "by 5:00": "by specific time",
        "by 5 o'clock": "by specific time",
        "due at 5 PM": "by specific time",
        "due at 5:00": "by specific time",
        "due at 5 o'clock": "by specific time",
        "no later than 5 PM": "by specific time",
        "no later than 5:00": "by specific time",
        "before 5 PM": "by specific time",
        "before 5:00": "by specific time",
        
        # Within timeframe expressions
        "within 24 hours": "within timeframe",
        "within the hour": "within timeframe",
        "within the day": "within timeframe",
        "within the week": "within timeframe",
        "within a week": "within timeframe",
        "within 7 days": "within timeframe",
        "within 30 days": "within timeframe",
        "within a month": "within timeframe",
        
        # No later than expressions
        "no later than today": "no later than today",
        "no later than tomorrow": "no later than tomorrow",
        "no later than Monday": "no later than Monday",
        "no later than Tuesday": "no later than Tuesday",
        "no later than Wednesday": "no later than Wednesday",
        "no later than Thursday": "no later than Thursday",
        "no later than Friday": "no later than Friday",
        "no later than Saturday": "no later than Saturday",
        "no later than Sunday": "no later than Sunday",
        
        # Other common deadline phrases
        "on my desk by morning": "by morning",
        "first thing tomorrow": "by morning tomorrow",
        "first thing Monday": "by morning Monday",
        "before you leave today": "end of day",
        "before the weekend": "end of week",
        "before the holidays": "specific deadline",
        "by the time I get back": "specific deadline",
        "get back to me by": "specific deadline",
        "respond by": "specific deadline",
        "submit by": "specific deadline",
        "finish by": "specific deadline",
        "complete by": "specific deadline",
        
        # Reminder-based deadlines
        "don't forget": "reminder",
        "remember to": "reminder",
        "keep in mind": "reminder",
        "make sure to": "reminder",
        "be sure to": "reminder",
        
        # Informal deadline expressions
        "yesterday": "overdue",
        "needed it yesterday": "overdue",
        "already late": "overdue",
        "past due": "overdue",
        "overdue": "overdue",
        "behind schedule": "overdue",
        "running late": "urgent",
        "crunch time": "urgent",
        "down to the wire": "urgent",
        "eleventh hour": "urgent",
        "last minute": "urgent",
        
        # Flexible/vague deadlines
        "when you can": "flexible",
        "when you get a chance": "flexible",
        "when you have time": "flexible",
        "at your convenience": "flexible",
        "no rush": "flexible",
        "take your time": "flexible",
        "whenever": "flexible",
        "soon": "soon",
        "in the near future": "soon",
        "shortly": "soon",
        "in due course": "eventual",
        "in good time": "eventual"
    }
    
    # Create the final JSON object
    deadlines_json = {
        "description": "Time limits for completion as commonly expressed in conversation",
        "examples": ["by Friday", "due tomorrow", "before noon", "deadline", "EOD", "ASAP"],
        "values": deadlines
    }
    
    return deadlines_json

# Generate the JSON data
json_data = generate_deadlines_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/deadlines/vocabulary/deadlines.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} deadline expressions and saved to deadlines.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["ASAP", "by Friday", "due tomorrow", "EOD", "as soon as possible", "within the week"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": "{json_data["values"][key]}"')