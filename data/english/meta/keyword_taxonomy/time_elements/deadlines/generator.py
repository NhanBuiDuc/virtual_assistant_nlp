import json
import os
from datetime import datetime

def generate_deadlines_json():
    """
    Generate a JSON file with deadline expressions as commonly spoken.
    Each entry includes key time components extracted from the deadline expression.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    deadlines = {}
    
    # Helper function to add a deadline with incremented ID
    def add_deadline(key, standard_form, deadline_type=None, preposition=None, time_point=None, 
                    second=None, minute=None, hour=None, day=None, date=None, 
                    week=None, month=None, year=None, period=None, urgency=None):
        """
        Add a deadline with structured time components
        """
        nonlocal id_counter
        deadlines[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "deadline_type": deadline_type,
            "preposition": preposition,
            "time_point": time_point,
            "second": second,
            "minute": minute,
            "hour": hour,
            "day": day,
            "date": date,
            "week": week,
            "month": month,
            "year": year,
            "period": period,
            "urgency": urgency
        }
        id_counter += 1
    
    # Basic deadline terms
    add_deadline("deadline", "deadline", deadline_type="generic")
    add_deadline("due date", "deadline", deadline_type="generic", preposition="due")
    add_deadline("due", "deadline", deadline_type="generic", preposition="due")
    add_deadline("cutoff", "deadline", deadline_type="generic")
    add_deadline("time limit", "deadline", deadline_type="generic")
    
    # Common abbreviations
    add_deadline("ASAP", "as soon as possible", deadline_type="relative", urgency="high")
    add_deadline("EOD", "end of day", deadline_type="relative", period="day", time_point="end")
    add_deadline("COB", "close of business", deadline_type="relative", period="day", time_point="end")
    add_deadline("EOP", "end of period", deadline_type="relative", time_point="end")
    add_deadline("EOB", "end of business", deadline_type="relative", period="day", time_point="end")
    add_deadline("EOW", "end of week", deadline_type="relative", period="week", time_point="end")
    add_deadline("EOM", "end of month", deadline_type="relative", period="month", time_point="end")
    add_deadline("EOQ", "end of quarter", deadline_type="relative", period="quarter", time_point="end")
    add_deadline("EOY", "end of year", deadline_type="relative", period="year", time_point="end")
    
    # Time-based deadlines
    add_deadline("by morning", "by morning", deadline_type="relative", preposition="by", period="day", time_point="morning")
    add_deadline("by noon", "by noon", deadline_type="relative", preposition="by", period="day", time_point="noon", hour=12)
    add_deadline("by afternoon", "by afternoon", deadline_type="relative", preposition="by", period="day", time_point="afternoon")
    add_deadline("by evening", "by evening", deadline_type="relative", preposition="by", period="day", time_point="evening")
    add_deadline("by night", "by night", deadline_type="relative", preposition="by", period="day", time_point="night")
    add_deadline("by midnight", "by midnight", deadline_type="relative", preposition="by", period="day", time_point="midnight", hour=0)
    
    add_deadline("before morning", "before morning", deadline_type="relative", preposition="before", period="day", time_point="morning")
    add_deadline("before noon", "before noon", deadline_type="relative", preposition="before", period="day", time_point="noon", hour=12)
    add_deadline("before afternoon", "before afternoon", deadline_type="relative", preposition="before", period="day", time_point="afternoon")
    add_deadline("before evening", "before evening", deadline_type="relative", preposition="before", period="day", time_point="evening")
    add_deadline("before night", "before night", deadline_type="relative", preposition="before", period="day", time_point="night")
    add_deadline("before midnight", "before midnight", deadline_type="relative", preposition="before", period="day", time_point="midnight", hour=0)
    
    # Day-based deadlines with "by"
    add_deadline("by today", "by today", deadline_type="relative", preposition="by", day="today")
    add_deadline("by tomorrow", "by tomorrow", deadline_type="relative", preposition="by", day="tomorrow")
    add_deadline("by Monday", "by Monday", deadline_type="specific_day", preposition="by", day="Monday")
    add_deadline("by Tuesday", "by Tuesday", deadline_type="specific_day", preposition="by", day="Tuesday")
    add_deadline("by Wednesday", "by Wednesday", deadline_type="specific_day", preposition="by", day="Wednesday")
    add_deadline("by Thursday", "by Thursday", deadline_type="specific_day", preposition="by", day="Thursday")
    add_deadline("by Friday", "by Friday", deadline_type="specific_day", preposition="by", day="Friday")
    add_deadline("by Saturday", "by Saturday", deadline_type="specific_day", preposition="by", day="Saturday")
    add_deadline("by Sunday", "by Sunday", deadline_type="specific_day", preposition="by", day="Sunday")
    
    add_deadline("by next week", "by next week", deadline_type="relative", preposition="by", week="next")
    add_deadline("by next month", "by next month", deadline_type="relative", preposition="by", month="next")
    add_deadline("by next year", "by next year", deadline_type="relative", preposition="by", year="next")
    
    # Day-based deadlines with "due"
    add_deadline("due today", "due today", deadline_type="relative", preposition="due", day="today")
    add_deadline("due tomorrow", "due tomorrow", deadline_type="relative", preposition="due", day="tomorrow")
    add_deadline("due Monday", "due Monday", deadline_type="specific_day", preposition="due", day="Monday")
    add_deadline("due Tuesday", "due Tuesday", deadline_type="specific_day", preposition="due", day="Tuesday")
    add_deadline("due Wednesday", "due Wednesday", deadline_type="specific_day", preposition="due", day="Wednesday")
    add_deadline("due Thursday", "due Thursday", deadline_type="specific_day", preposition="due", day="Thursday")
    add_deadline("due Friday", "due Friday", deadline_type="specific_day", preposition="due", day="Friday")
    add_deadline("due Saturday", "due Saturday", deadline_type="specific_day", preposition="due", day="Saturday")
    add_deadline("due Sunday", "due Sunday", deadline_type="specific_day", preposition="due", day="Sunday")
    
    add_deadline("due next week", "due next week", deadline_type="relative", preposition="due", week="next")
    add_deadline("due next month", "due next month", deadline_type="relative", preposition="due", month="next")
    
    # End of period expressions
    add_deadline("end of day", "end of day", deadline_type="relative", period="day", time_point="end")
    add_deadline("end of business", "end of business", deadline_type="relative", period="day", time_point="end")
    add_deadline("close of business", "close of business", deadline_type="relative", period="day", time_point="end")
    add_deadline("end of week", "end of week", deadline_type="relative", period="week", time_point="end")
    add_deadline("end of month", "end of month", deadline_type="relative", period="month", time_point="end")
    add_deadline("end of quarter", "end of quarter", deadline_type="relative", period="quarter", time_point="end")
    add_deadline("end of year", "end of year", deadline_type="relative", period="year", time_point="end")
    
    add_deadline("by the end of day", "end of day", deadline_type="relative", preposition="by", period="day", time_point="end")
    add_deadline("by the end of business", "end of business", deadline_type="relative", preposition="by", period="day", time_point="end")
    add_deadline("by the end of the week", "end of week", deadline_type="relative", preposition="by", period="week", time_point="end")
    add_deadline("by the end of the month", "end of month", deadline_type="relative", preposition="by", period="month", time_point="end")
    add_deadline("by the end of the quarter", "end of quarter", deadline_type="relative", preposition="by", period="quarter", time_point="end")
    add_deadline("by the end of the year", "end of year", deadline_type="relative", preposition="by", period="year", time_point="end")
    
    # Urgency expressions
    add_deadline("as soon as possible", "as soon as possible", deadline_type="relative", urgency="high")
    add_deadline("immediately", "immediately", deadline_type="relative", urgency="very high")
    add_deadline("right away", "immediately", deadline_type="relative", urgency="very high")
    add_deadline("right now", "immediately", deadline_type="relative", urgency="very high")
    add_deadline("at once", "immediately", deadline_type="relative", urgency="very high")
    add_deadline("without delay", "immediately", deadline_type="relative", urgency="high")
    add_deadline("STAT", "immediately", deadline_type="relative", urgency="very high")
    add_deadline("urgent", "urgent", deadline_type="relative", urgency="high")
    add_deadline("top priority", "urgent", deadline_type="relative", urgency="high")
    add_deadline("high priority", "urgent", deadline_type="relative", urgency="high")
    add_deadline("rush", "urgent", deadline_type="relative", urgency="high")
    
    # Specific time expressions
    add_deadline("by 5 PM", "by specific time", deadline_type="specific_time", preposition="by", hour=17)
    add_deadline("by 5:00", "by specific time", deadline_type="specific_time", preposition="by", hour=17, minute=0)
    add_deadline("by 5 o'clock", "by specific time", deadline_type="specific_time", preposition="by", hour=17)
    
    add_deadline("due at 5 PM", "by specific time", deadline_type="specific_time", preposition="due", hour=17)
    add_deadline("due at 5:00", "by specific time", deadline_type="specific_time", preposition="due", hour=17, minute=0)
    add_deadline("due at 5 o'clock", "by specific time", deadline_type="specific_time", preposition="due", hour=17)
    
    add_deadline("no later than 5 PM", "by specific time", deadline_type="specific_time", preposition="no later than", hour=17)
    add_deadline("no later than 5:00", "by specific time", deadline_type="specific_time", preposition="no later than", hour=17, minute=0)
    
    # Within timeframe expressions
    add_deadline("within 24 hours", "within timeframe", deadline_type="duration", hour=24)
    add_deadline("within the hour", "within timeframe", deadline_type="duration", hour=1)
    add_deadline("within the day", "within timeframe", deadline_type="duration", day=1)
    add_deadline("within the week", "within timeframe", deadline_type="duration", week=1)
    add_deadline("within a week", "within timeframe", deadline_type="duration", week=1)
    add_deadline("within 7 days", "within timeframe", deadline_type="duration", day=7)
    add_deadline("within 30 days", "within timeframe", deadline_type="duration", day=30)
    add_deadline("within a month", "within timeframe", deadline_type="duration", month=1)
    
    # No later than expressions
    add_deadline("no later than today", "no later than today", deadline_type="relative", preposition="no later than", day="today")
    add_deadline("no later than tomorrow", "no later than tomorrow", deadline_type="relative", preposition="no later than", day="tomorrow")
    add_deadline("no later than Monday", "no later than Monday", deadline_type="specific_day", preposition="no later than", day="Monday")
    add_deadline("no later than Tuesday", "no later than Tuesday", deadline_type="specific_day", preposition="no later than", day="Tuesday")
    add_deadline("no later than Wednesday", "no later than Wednesday", deadline_type="specific_day", preposition="no later than", day="Wednesday")
    add_deadline("no later than Thursday", "no later than Thursday", deadline_type="specific_day", preposition="no later than", day="Thursday")
    add_deadline("no later than Friday", "no later than Friday", deadline_type="specific_day", preposition="no later than", day="Friday")
    add_deadline("no later than Saturday", "no later than Saturday", deadline_type="specific_day", preposition="no later than", day="Saturday")
    add_deadline("no later than Sunday", "no later than Sunday", deadline_type="specific_day", preposition="no later than", day="Sunday")
    
    # Other common deadline phrases
    add_deadline("on my desk by morning", "by morning", deadline_type="relative", preposition="by", period="day", time_point="morning")
    add_deadline("first thing tomorrow", "by morning tomorrow", deadline_type="relative", preposition="by", day="tomorrow", time_point="morning")
    add_deadline("first thing Monday", "by morning Monday", deadline_type="specific_day", preposition="by", day="Monday", time_point="morning")
    add_deadline("before you leave today", "end of day", deadline_type="relative", preposition="before", day="today", time_point="end")
    add_deadline("before the weekend", "end of week", deadline_type="relative", preposition="before", period="week", time_point="end")
    
    # Informal deadline expressions
    add_deadline("yesterday", "overdue", deadline_type="overdue", day="yesterday")
    add_deadline("needed it yesterday", "overdue", deadline_type="overdue", day="yesterday", urgency="high")
    add_deadline("already late", "overdue", deadline_type="overdue", urgency="high")
    add_deadline("past due", "overdue", deadline_type="overdue")
    add_deadline("overdue", "overdue", deadline_type="overdue")
    add_deadline("behind schedule", "overdue", deadline_type="overdue")
    add_deadline("running late", "urgent", deadline_type="relative", urgency="high")
    add_deadline("crunch time", "urgent", deadline_type="relative", urgency="high")
    add_deadline("down to the wire", "urgent", deadline_type="relative", urgency="high")
    add_deadline("eleventh hour", "urgent", deadline_type="relative", urgency="high")
    add_deadline("last minute", "urgent", deadline_type="relative", urgency="high")
    
    # Flexible/vague deadlines
    add_deadline("when you can", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("when you get a chance", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("when you have time", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("at your convenience", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("no rush", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("take your time", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("whenever", "flexible", deadline_type="flexible", urgency="low")
    add_deadline("soon", "soon", deadline_type="relative", urgency="medium")
    add_deadline("in the near future", "soon", deadline_type="relative", urgency="medium")
    add_deadline("shortly", "soon", deadline_type="relative", urgency="medium")
    add_deadline("in due course", "eventual", deadline_type="flexible", urgency="low")
    add_deadline("in good time", "eventual", deadline_type="flexible", urgency="low")
    
    # Create the final JSON object
    deadlines_json = {
        "description": "Time limits for completion as commonly expressed in conversation",
        "examples": ["by Friday", "due tomorrow", "before noon", "deadline", "EOD", "ASAP"],
        "values": deadlines,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return deadlines_json

# Generate the JSON data
json_data = generate_deadlines_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/deadlines/vocabulary/deadlines.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} deadline expressions and saved to deadlines.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["ASAP", "by Friday", "due tomorrow", "EOD", "within a week", "by 5 PM"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')