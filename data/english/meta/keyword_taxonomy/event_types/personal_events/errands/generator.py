import json

def generate_errands_json():
    """
    Generate a JSON file with errand expressions as commonly spoken.
    Each key is a longer verbal reference to an errand, and the value is an object
    containing a description (shorter standardized term) and a priority level.
    """
    errands = {
        # Pick Up Activities
        "pick up dry cleaning": {"description": "dry cleaning pickup", "priority": 3},
        "pick up prescription medication": {"description": "prescription pickup", "priority": 5},
        "pick up package from post office": {"description": "package pickup", "priority": 3},
        "pick up takeout food": {"description": "food pickup", "priority": 2},
        "pick up kids from school": {"description": "school pickup", "priority": 5},
        "pick up children from daycare": {"description": "daycare pickup", "priority": 5},
        "pick up children from extracurricular activities": {"description": "activity pickup", "priority": 4},
        "pick up ordered items from store": {"description": "store pickup", "priority": 3},
        "pick up party supplies": {"description": "supply pickup", "priority": 3},
        "pick up pet from groomer": {"description": "pet pickup", "priority": 3},
        "pick up gift for special occasion": {"description": "gift pickup", "priority": 3},
        
        # Drop Off Activities
        "drop off package at post office": {"description": "mail dropoff", "priority": 3},
        "drop off library books": {"description": "library return", "priority": 2},
        "drop off dry cleaning": {"description": "laundry dropoff", "priority": 2},
        "drop off children at school": {"description": "school dropoff", "priority": 5},
        "drop off kids at daycare": {"description": "daycare dropoff", "priority": 5},
        "drop off children at activities": {"description": "activity dropoff", "priority": 4},
        "drop off rental items": {"description": "rental return", "priority": 4},
        "drop off payment or check": {"description": "payment dropoff", "priority": 4},
        "drop off donation items": {"description": "donation dropoff", "priority": 2},
        "drop off recycling": {"description": "recycling dropoff", "priority": 3},
        "drop off pet at groomer": {"description": "pet dropoff", "priority": 3},
        "drop off car for service": {"description": "car service dropoff", "priority": 4},
        
        # Return Items
        "return purchased item to store": {"description": "store return", "priority": 3},
        "return online purchase": {"description": "online return", "priority": 3},
        "return borrowed item to friend": {"description": "borrowed item return", "priority": 3},
        "return rented equipment": {"description": "equipment return", "priority": 4},
        "return defective product": {"description": "defective return", "priority": 3},
        "return unwanted gift": {"description": "gift return", "priority": 2},
        "return textbooks at end of term": {"description": "textbook return", "priority": 3},
        
        # Banking Activities
        "deposit check at bank": {"description": "check deposit", "priority": 4},
        "withdraw cash from ATM": {"description": "cash withdrawal", "priority": 3},
        "meet with bank representative": {"description": "bank appointment", "priority": 4},
        "apply for loan in person": {"description": "loan application", "priority": 4},
        "make loan payment in person": {"description": "loan payment", "priority": 4},
        "get cashier's check": {"description": "cashier's check", "priority": 4},
        "exchange currency": {"description": "currency exchange", "priority": 3},
        "open new account": {"description": "account opening", "priority": 3},
        "address account issues": {"description": "account servicing", "priority": 4},
        "get documents notarized": {"description": "notary service", "priority": 4},
        "access safe deposit box": {"description": "safe deposit access", "priority": 3},
        
        # Shopping Errands
        "purchase groceries at store": {"description": "grocery run", "priority": 4},
        "buy specific item at specialty store": {"description": "specialty shopping", "priority": 3},
        "shop for clothing": {"description": "clothes shopping", "priority": 2},
        "purchase personal care items": {"description": "personal care shopping", "priority": 3},
        "buy gift for specific event": {"description": "gift shopping", "priority": 3},
        "shop for home improvement supplies": {"description": "hardware store run", "priority": 3},
        "purchase electronics or appliances": {"description": "electronics shopping", "priority": 2},
        "shop for seasonal items": {"description": "seasonal shopping", "priority": 2},
        
        # Services and Appointments
        "attend medical appointment": {"description": "medical appointment", "priority": 5},
        "go to dental checkup": {"description": "dental appointment", "priority": 4},
        "visit hair salon": {"description": "hair appointment", "priority": 2},
        "get vehicle serviced": {"description": "car service", "priority": 4},
        "meet with tax preparer": {"description": "tax appointment", "priority": 4},
        "attend legal consultation": {"description": "legal appointment", "priority": 5},
        "go to therapy session": {"description": "therapy appointment", "priority": 4},
        "attend parent-teacher conference": {"description": "school conference", "priority": 4},
        "visit government office": {"description": "government office visit", "priority": 4},
        "get car washed": {"description": "car wash", "priority": 1},
        "get vehicle emissions test": {"description": "emissions test", "priority": 4},
        
        # Government and Official Errands
        "renew driver's license": {"description": "license renewal", "priority": 5},
        "register to vote": {"description": "voter registration", "priority": 4},
        "apply for passport": {"description": "passport application", "priority": 4},
        "renew vehicle registration": {"description": "vehicle registration", "priority": 5},
        "apply for permits": {"description": "permit application", "priority": 4},
        "pay traffic ticket": {"description": "ticket payment", "priority": 4},
        "attend court appearance": {"description": "court appearance", "priority": 5},
        "file paperwork at city hall": {"description": "document filing", "priority": 4},
        
        # Miscellaneous Errands
        "fill car with gas": {"description": "gas fillup", "priority": 4},
        "take item for repair": {"description": "repair dropoff", "priority": 3},
        "mail letters or packages": {"description": "mailing items", "priority": 3},
        "purchase postage stamps": {"description": "stamp purchase", "priority": 2},
        "collect contact lenses": {"description": "contact lens pickup", "priority": 4},
        "go to gym or fitness class": {"description": "fitness visit", "priority": 2},
        "attend religious service": {"description": "religious service", "priority": 3},
        "pick up tickets for event": {"description": "ticket pickup", "priority": 3},
        "take pet to veterinarian": {"description": "vet visit", "priority": 5},
        "charge electric vehicle": {"description": "vehicle charging", "priority": 4}
    }
    
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
        }
    }
    
    return errands_json

# Generate the JSON data
json_data = generate_errands_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/event_types/personal_events/errands/vocabulary/errands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} errand expressions and saved to errands.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["pick up prescription medication", "drop off children at school", "deposit check at bank",
               "attend medical appointment", "renew driver's license"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')

# If you want to see the raw JSON output
print("\nFull JSON structure:")
print(json.dumps({"errands": {
    "description": "Tasks that require going out",
    "examples": ["pick up", "drop off", "return item", "banking"],
    "vocab": "errands.json"
}}, indent=2))