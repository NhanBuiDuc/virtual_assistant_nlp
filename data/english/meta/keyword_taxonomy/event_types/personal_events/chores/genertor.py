import json
import os
from datetime import datetime

def generate_household_chores_json():
    """
    Generate a JSON file with household chore expressions as commonly spoken.
    Each key is a longer verbal reference to a household chore, and the value is an object
    containing the primary task attributes requested.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    household_chores = {}
    
    # Helper function to add an item with incremented ID
    def add_chore(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        household_chores[key] = {
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
    
    # Cleaning
    add_chore(
        "vacuum the floors and carpets",
        "Vacuum Floors and Carpets",
        "Clean floors and carpets using a vacuum cleaner",
        "personal",
        "chore",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "sweep the floors",
        "Sweep Floors",
        "Clean hard floor surfaces using a broom",
        "personal",
        "chore",
        True,
        "biweekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "mop the floor surfaces",
        "Mop Floors",
        "Clean hard floor surfaces using a mop and cleaning solution",
        "personal",
        "chore",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "dust the furniture and surfaces",
        "Dust Furniture",
        "Remove dust from furniture and household surfaces",
        "personal",
        "chore",
        True,
        "weekly",
        2,
        "low",
        "low"
    )
    
    add_chore(
        "clean the bathroom toilet",
        "Clean Toilet",
        "Sanitize and clean the bathroom toilet",
        "personal",
        "chore",
        True,
        "weekly",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "deep clean the entire house",
        "Deep Clean House",
        "Thoroughly clean all areas of the house",
        "personal",
        "chore",
        True,
        "monthly",
        4,
        "high",
        "medium"
    )
    
    add_chore(
        "sanitize high-touch surfaces",
        "Sanitize Surfaces",
        "Clean and disinfect frequently touched surfaces",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    # Laundry
    add_chore(
        "wash dirty clothes",
        "Wash Clothes",
        "Wash clothing in washing machine or by hand",
        "personal",
        "chore",
        True,
        "weekly",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "fold clean clothes",
        "Fold Laundry",
        "Fold clean clothes and prepare for storage",
        "personal",
        "chore",
        True,
        "weekly",
        2,
        "medium",
        "low"
    )
    
    add_chore(
        "iron wrinkled clothing",
        "Iron Clothes",
        "Remove wrinkles from clothing using an iron",
        "personal",
        "chore",
        True,
        "weekly",
        2,
        "low",
        "low"
    )
    
    add_chore(
        "wash bed sheets and linens",
        "Wash Bedding",
        "Launder bed sheets, pillowcases, and other bedding",
        "personal",
        "chore",
        True,
        "biweekly",
        3,
        "medium",
        "medium"
    )
    
    # Kitchen Tasks
    add_chore(
        "wash dirty dishes",
        "Wash Dishes",
        "Clean dirty dishes, utensils, and cookware",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "prepare meals for the family",
        "Cook Meals",
        "Prepare and cook food for household members",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "meal prep for the week",
        "Meal Prep",
        "Prepare portions of meals in advance for the week",
        "personal",
        "chore",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "clean out expired food",
        "Clean Refrigerator",
        "Remove and dispose of expired food items",
        "personal",
        "chore",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "take out kitchen garbage",
        "Take Out Trash",
        "Remove and dispose of kitchen garbage",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    # Shopping
    add_chore(
        "buy groceries for the week",
        "Grocery Shopping",
        "Purchase food and household essentials",
        "personal",
        "chore",
        True,
        "weekly",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "pick up household essentials",
        "Buy Household Items",
        "Purchase necessary household supplies",
        "personal",
        "chore",
        True,
        "monthly",
        4,
        "high",
        "medium"
    )
    
    # Yard and Outdoor
    add_chore(
        "mow the lawn",
        "Mow Lawn",
        "Cut grass in yard using lawn mower",
        "personal",
        "chore",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "shovel snow from walkways",
        "Shovel Snow",
        "Clear snow from walkways and driveway",
        "personal",
        "chore",
        True,
        "as needed",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "water plants and garden",
        "Water Plants",
        "Provide water to indoor and outdoor plants",
        "personal",
        "chore",
        True,
        "biweekly",
        3,
        "medium",
        "medium"
    )
    
    # Pet Care
    add_chore(
        "feed household pets",
        "Feed Pets",
        "Provide food and water to household pets",
        "personal",
        "chore",
        True,
        "daily",
        5,
        "very high",
        "very high"
    )
    
    add_chore(
        "walk the dog",
        "Walk Dog",
        "Take dog outside for exercise and bathroom needs",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    add_chore(
        "clean litter box",
        "Clean Litter Box",
        "Remove waste and replace litter in cat litter box",
        "personal",
        "chore",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    # Home Maintenance
    add_chore(
        "change air filters",
        "Change Air Filters",
        "Replace HVAC system air filters",
        "personal",
        "chore",
        True,
        "monthly",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "replace light bulbs",
        "Replace Light Bulbs",
        "Change burned-out light bulbs",
        "personal",
        "chore",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_chore(
        "change smoke detector batteries",
        "Replace Smoke Detector Batteries",
        "Change batteries in smoke and carbon monoxide detectors",
        "personal",
        "chore",
        True,
        "annually",
        4,
        "high",
        "medium"
    )
    
    # Create the final JSON object
    household_chores_json = {
        "description": "Routine household tasks as commonly expressed in conversation",
        "examples": ["cleaning", "laundry", "grocery shopping", "cooking"],
        "values": household_chores,
        "priority_scale": {
            "1": "Very Low - Optional tasks that improve quality of life",
            "2": "Low - Regular maintenance tasks that can be delayed",
            "3": "Medium - Normal recurring household tasks",
            "4": "High - Essential tasks for health and daily functioning",
            "5": "Very High - Critical tasks that affect health and safety"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return household_chores_json

# Generate the JSON data
json_data = generate_household_chores_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/personal_events/chores/vocabulary/household_chores.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} household chore expressions and saved to household_chores.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["vacuum the floors and carpets", "wash dirty clothes", "buy groceries for the week", 
               "feed household pets", "take out kitchen garbage"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')