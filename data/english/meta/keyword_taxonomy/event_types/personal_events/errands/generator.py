import json
import os
from datetime import datetime

def generate_errands_json():
    """
    Generate a JSON file with errand expressions as commonly spoken.
    Each key is a longer verbal reference to an errand, and the value is an object
    containing the primary task attributes requested.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    errands = {}
    
    # Helper function to add an item with incremented ID
    def add_errand(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        errands[key] = {
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
    
    # Pick Up Activities
    add_errand(
        "pick up dry cleaning",
        "Pick Up Dry Cleaning",
        "Collect cleaned clothes from dry cleaner",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "pick up prescription medication",
        "Get Prescription",
        "Collect prescribed medication from pharmacy",
        "personal",
        "errand",
        True,
        "monthly",
        5,
        "very high",
        "high"
    )
    
    add_errand(
        "pick up package from post office",
        "Pick Up Package",
        "Collect package from post office or delivery center",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "pick up kids from school",
        "School Pickup",
        "Collect children from school at the end of the day",
        "personal",
        "errand",
        True,
        "weekdays",
        5,
        "very high",
        "very high"
    )
    
    add_errand(
        "pick up takeout food",
        "Takeout Pickup",
        "Collect pre-ordered food from restaurant",
        "personal",
        "errand",
        False,
        "as needed",
        2,
        "low",
        "medium"
    )
    
    # Drop Off Activities
    add_errand(
        "drop off package at post office",
        "Mail Package",
        "Send package via postal service or carrier",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "drop off library books",
        "Return Library Books",
        "Return borrowed books to the library",
        "personal",
        "errand",
        False,
        "as needed",
        2,
        "low",
        "medium"
    )
    
    add_errand(
        "drop off children at school",
        "School Dropoff",
        "Take children to school in the morning",
        "personal",
        "errand",
        True,
        "weekdays",
        5,
        "very high",
        "very high"
    )
    
    add_errand(
        "drop off car for service",
        "Car Service Dropoff",
        "Leave car at service center for maintenance or repair",
        "personal",
        "errand",
        True,
        "quarterly",
        4,
        "high",
        "medium"
    )
    
    # Return Items
    add_errand(
        "return purchased item to store",
        "Store Return",
        "Return item to retail location for refund or exchange",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "return online purchase",
        "Online Order Return",
        "Return item purchased online via shipping service",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "low"
    )
    
    add_errand(
        "return borrowed item to friend",
        "Return Borrowed Item",
        "Give back item borrowed from friend or family member",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    # Banking Activities
    add_errand(
        "deposit check at bank",
        "Bank Deposit",
        "Deposit check at bank branch or ATM",
        "personal",
        "errand",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    add_errand(
        "withdraw cash from ATM",
        "ATM Withdrawal",
        "Get cash from automated teller machine",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "meet with bank representative",
        "Bank Appointment",
        "Scheduled meeting with banking staff",
        "personal",
        "errand",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    # Shopping Errands
    add_errand(
        "purchase groceries at store",
        "Grocery Shopping",
        "Buy food and household necessities at supermarket",
        "personal",
        "errand",
        True,
        "weekly",
        4,
        "high",
        "high"
    )
    
    add_errand(
        "buy specific item at specialty store",
        "Specialty Shopping",
        "Purchase specific item from a specialized retailer",
        "personal",
        "errand",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_errand(
        "shop for clothing",
        "Clothes Shopping",
        "Purchase apparel, shoes, or accessories",
        "personal",
        "errand",
        False,
        "as needed",
        2,
        "low",
        "low"
    )
    
    # Services and Appointments
    add_errand(
        "attend medical appointment",
        "Medical Appointment",
        "Visit doctor, specialist, or healthcare provider",
        "personal",
        "errand",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    add_errand(
        "go to dental checkup",
        "Dental Appointment",
        "Visit dentist for examination or procedure",
        "personal",
        "errand",
        True,
        "biannually",
        4,
        "high",
        "medium"
    )
    
    add_errand(
        "get vehicle serviced",
        "Car Service",
        "Take vehicle for maintenance or repairs",
        "personal",
        "errand",
        True,
        "quarterly",
        4,
        "high",
        "medium"
    )
    
    # Government and Official Errands
    add_errand(
        "renew driver's license",
        "License Renewal",
        "Update driver's license at government office",
        "personal",
        "errand",
        True,
        "every few years",
        5,
        "very high",
        "high"
    )
    
    add_errand(
        "register to vote",
        "Voter Registration",
        "Complete voter registration process",
        "personal",
        "errand",
        False,
        "once",
        4,
        "high",
        "medium"
    )
    
    add_errand(
        "renew vehicle registration",
        "Vehicle Registration",
        "Update vehicle registration with government",
        "personal",
        "errand",
        True,
        "annually",
        5,
        "very high",
        "high"
    )
    
    # Miscellaneous Errands
    add_errand(
        "fill car with gas",
        "Gas Fillup",
        "Refuel vehicle at gas station",
        "personal",
        "errand",
        True,
        "weekly",
        4,
        "high",
        "high"
    )
    
    add_errand(
        "take pet to veterinarian",
        "Vet Visit",
        "Bring pet for medical examination or treatment",
        "personal",
        "errand",
        True,
        "annually",
        5,
        "very high",
        "medium"
    )
    
    add_errand(
        "attend court appearance",
        "Court Appearance",
        "Appear in court for legal proceedings",
        "personal",
        "errand",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    # Create the final JSON object
    errands_json = {
        "description": "Tasks that require going out as commonly expressed in conversation",
        "examples": ["pick up", "drop off", "return item", "banking"],
        "values": errands,
        "priority_scale": {
            "1": "Very Low - Optional errands for convenience",
            "2": "Low - Can be postponed without significant consequence",
            "3": "Medium - Should be completed in a reasonable timeframe",
            "4": "High - Important errands with potential consequences if delayed",
            "5": "Very High - Critical errands that affect health, legal status, or major responsibilities"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return errands_json

# Generate the JSON data
json_data = generate_errands_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/personal_events/errands/vocabulary/errands.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} errand expressions and saved to errands.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["pick up prescription medication", "drop off children at school", "deposit check at bank",
               "attend medical appointment", "renew driver's license"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')