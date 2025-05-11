import json
import os
from datetime import datetime

def generate_celebrations_json():
    """
    Generate a JSON file with celebration expressions as commonly spoken.
    Each key is a longer verbal reference to a celebration, and the value is an object
    containing the primary task attributes requested.
    """
    
    # Counter for simple ID generation
    id_counter = 1
    
    celebrations = {}
    
    # Helper function to add an item with incremented ID
    def add_celebration(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        celebrations[key] = {
            "id": id_counter,
            "title": title,
            "description": description,
            "category": category,
            "event_type": event_type,
            "is_recurring": is_recurring,
            "frequency": frequency,
            "priority": priority,
            "importance": importance,
            "urgency": urgency
        }
        id_counter += 1
    
    # Birthday Celebrations
    add_celebration(
        "host a birthday party",
        "Host Birthday Party",
        "Organize and host a birthday celebration for a friend or family member",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "organize a surprise birthday",
        "Organize Surprise Birthday",
        "Plan and execute a surprise birthday celebration",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "high"
    )
    
    add_celebration(
        "attend a friend's birthday celebration",
        "Attend Friend's Birthday",
        "Go to a friend's birthday celebration",
        "personal",
        "celebration",
        True,
        "yearly",
        3,
        "medium",
        "low"
    )
    
    add_celebration(
        "plan a child's birthday party",
        "Plan Child's Birthday Party",
        "Organize a birthday party for a child",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "arrange a birthday dinner",
        "Arrange Birthday Dinner",
        "Plan and coordinate a special dinner for someone's birthday",
        "personal",
        "celebration",
        True,
        "yearly",
        3,
        "medium",
        "medium"
    )
    
    # Anniversary Celebrations
    add_celebration(
        "celebrate wedding anniversary",
        "Celebrate Wedding Anniversary",
        "Plan and celebrate a wedding anniversary",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "plan an anniversary trip",
        "Plan Anniversary Trip",
        "Organize a special trip to celebrate an anniversary",
        "personal", 
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "organize anniversary dinner",
        "Organize Anniversary Dinner",
        "Arrange a special dinner to celebrate an anniversary",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    # Graduation Celebrations
    add_celebration(
        "attend graduation ceremony",
        "Attend Graduation Ceremony",
        "Attend a graduation ceremony for a friend or family member",
        "personal",
        "celebration",
        False,
        "",
        4,
        "high",
        "high"
    )
    
    add_celebration(
        "host graduation party",
        "Host Graduation Party",
        "Organize and host a party to celebrate a graduation",
        "personal",
        "celebration",
        False,
        "",
        4,
        "high",
        "medium"
    )
    
    # Holiday Celebrations
    add_celebration(
        "host Christmas gathering",
        "Host Christmas Gathering",
        "Organize and host a Christmas celebration with family or friends",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "celebrate New Year's Eve",
        "Celebrate New Year's Eve",
        "Plan or attend a New Year's Eve celebration",
        "personal",
        "celebration",
        True,
        "yearly",
        3,
        "medium",
        "medium"
    )
    
    add_celebration(
        "organize Thanksgiving dinner",
        "Organize Thanksgiving Dinner",
        "Plan and prepare a Thanksgiving meal with family or friends",
        "personal",
        "celebration",
        True,
        "yearly",
        4,
        "high",
        "high"
    )
    
    # Life Event Celebrations
    add_celebration(
        "host baby shower",
        "Host Baby Shower",
        "Organize and host a baby shower for an expecting parent",
        "personal",
        "celebration",
        False,
        "",
        4,
        "high",
        "medium"
    )
    
    add_celebration(
        "plan wedding celebration",
        "Plan Wedding Celebration",
        "Organize a wedding celebration or reception",
        "personal",
        "celebration",
        False,
        "",
        5,
        "very high",
        "high"
    )
    
    # Create the final JSON object
    celebrations_json = {
        "description": "Special personal occasions as commonly expressed in conversation",
        "examples": ["birthday party", "anniversary dinner", "graduation celebration"],
        "values": celebrations,
        "priority_scale": {
            "1": "Very Low - Optional social gathering",
            "2": "Low - Nice-to-have celebration",
            "3": "Medium - Standard celebration worth effort",
            "4": "High - Important life event celebration",
            "5": "Very High - Once-in-a-lifetime momentous celebration"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return celebrations_json

# Generate the JSON data
json_data = generate_celebrations_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/personal_events/celebrations/vocabulary/celebrations.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} celebration expressions and saved to celebrations.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["host a birthday party", "celebrate wedding anniversary", "attend graduation ceremony"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')