import json

def generate_celebrations_json():
    """
    Generate a JSON file with celebration expressions as commonly spoken.
    Each key is a longer verbal reference to a celebration, and the value is an object
    containing a description (shorter standardized term) and a priority level.
    """
    celebrations = {
        # Birthday Celebrations
        "host a birthday party": {"description": "birthday party", "priority": 4},
        "organize a surprise birthday": {"description": "surprise birthday", "priority": 4},
        "attend a friend's birthday celebration": {"description": "birthday attendance", "priority": 3},
        "plan a child's birthday party": {"description": "kids birthday", "priority": 4},
        "arrange a birthday dinner": {"description": "birthday dinner", "priority": 3},
        "celebrate a milestone birthday": {"description": "milestone birthday", "priority": 4},
        "send birthday wishes": {"description": "birthday wishes", "priority": 2},
        "have a small birthday gathering": {"description": "birthday gathering", "priority": 3},
        "organize a virtual birthday celebration": {"description": "virtual birthday", "priority": 3},
        
        # Anniversary Celebrations
        "celebrate wedding anniversary": {"description": "wedding anniversary", "priority": 4},
        "plan an anniversary trip": {"description": "anniversary trip", "priority": 4},
        "organize anniversary dinner": {"description": "anniversary dinner", "priority": 4},
        "attend parents' anniversary": {"description": "parents anniversary", "priority": 3},
        "recognize work anniversary": {"description": "work anniversary", "priority": 2},
        "celebrate relationship milestone": {"description": "relationship milestone", "priority": 3},
        "plan surprise anniversary gift": {"description": "anniversary surprise", "priority": 3},
        "celebrate business anniversary": {"description": "business anniversary", "priority": 3},
        "commemorate house anniversary": {"description": "home anniversary", "priority": 2},
        
        # Graduation Celebrations
        "attend graduation ceremony": {"description": "graduation attendance", "priority": 4},
        "host graduation party": {"description": "graduation party", "priority": 4},
        "organize graduation dinner": {"description": "graduation dinner", "priority": 4},
        "plan post-graduation trip": {"description": "graduation trip", "priority": 3},
        "celebrate academic achievement": {"description": "academic celebration", "priority": 3},
        "recognize educational milestone": {"description": "education milestone", "priority": 4},
        "attend commencement exercises": {"description": "commencement", "priority": 4},
        "host graduation open house": {"description": "graduation open house", "priority": 3},
        
        # Holiday Celebrations
        "host Christmas gathering": {"description": "Christmas celebration", "priority": 4},
        "celebrate New Year's Eve": {"description": "New Year's party", "priority": 3},
        "organize Thanksgiving dinner": {"description": "Thanksgiving dinner", "priority": 4},
        "celebrate Halloween with friends": {"description": "Halloween party", "priority": 3},
        "host Easter celebration": {"description": "Easter celebration", "priority": 3},
        "organize Fourth of July barbecue": {"description": "Independence Day BBQ", "priority": 3},
        "celebrate Valentine's Day": {"description": "Valentine's celebration", "priority": 3},
        "host St. Patrick's Day party": {"description": "St. Patrick's party", "priority": 2},
        "celebrate Diwali with family": {"description": "Diwali celebration", "priority": 4},
        "host Hanukkah gathering": {"description": "Hanukkah celebration", "priority": 4},
        "organize Eid celebration": {"description": "Eid celebration", "priority": 4},
        "celebrate Lunar New Year": {"description": "Lunar New Year", "priority": 4},
        
        # Life Event Celebrations
        "host baby shower": {"description": "baby shower", "priority": 4},
        "organize bridal shower": {"description": "bridal shower", "priority": 4},
        "attend engagement party": {"description": "engagement party", "priority": 4},
        "plan wedding celebration": {"description": "wedding celebration", "priority": 5},
        "host housewarming party": {"description": "housewarming", "priority": 3},
        "celebrate new job or promotion": {"description": "career celebration", "priority": 3},
        "organize retirement party": {"description": "retirement party", "priority": 4},
        "host going-away celebration": {"description": "farewell party", "priority": 3},
        "celebrate adoption finalization": {"description": "adoption celebration", "priority": 5},
        "plan gender reveal party": {"description": "gender reveal", "priority": 3},
        "celebrate citizenship ceremony": {"description": "citizenship celebration", "priority": 5},
        
        # Achievement Celebrations
        "celebrate job promotion": {"description": "promotion celebration", "priority": 3},
        "recognize sports championship": {"description": "sports celebration", "priority": 3},
        "celebrate competition win": {"description": "victory celebration", "priority": 3},
        "honor award recipient": {"description": "award celebration", "priority": 4},
        "recognize artistic achievement": {"description": "artistic recognition", "priority": 3},
        "celebrate publishing success": {"description": "publication celebration", "priority": 3},
        "honor volunteer recognition": {"description": "volunteer recognition", "priority": 3},
        "celebrate business milestone": {"description": "business milestone", "priority": 3},
        "recognize weight loss achievement": {"description": "fitness milestone", "priority": 2},
        
        # Cultural and Religious Celebrations
        "attend baptism or christening": {"description": "baptism celebration", "priority": 4},
        "celebrate bar or bat mitzvah": {"description": "bar/bat mitzvah", "priority": 5},
        "attend confirmation ceremony": {"description": "confirmation", "priority": 4},
        "celebrate quinceañera": {"description": "quinceañera", "priority": 5},
        "attend religious holiday service": {"description": "religious celebration", "priority": 4},
        "celebrate cultural festival": {"description": "cultural festival", "priority": 3},
        "organize family reunion": {"description": "family reunion", "priority": 4},
        "attend heritage celebration": {"description": "heritage celebration", "priority": 3},
        "celebrate religious milestone": {"description": "religious milestone", "priority": 4},
        
        # Personal Milestones
        "celebrate sobriety anniversary": {"description": "sobriety milestone", "priority": 5},
        "recognize health recovery": {"description": "recovery celebration", "priority": 4},
        "celebrate debt payoff": {"description": "financial milestone", "priority": 3},
        "recognize personal growth milestone": {"description": "personal milestone", "priority": 3},
        "celebrate relationship milestone": {"description": "relationship milestone", "priority": 4},
        "honor memory of loved one": {"description": "memorial gathering", "priority": 4},
        "celebrate moving to new place": {"description": "moving celebration", "priority": 3},
        "recognize travel achievement": {"description": "travel milestone", "priority": 2},
        
        # General Celebration Activities
        "organize dinner party": {"description": "dinner party", "priority": 3},
        "host cocktail reception": {"description": "cocktail party", "priority": 2},
        "plan celebratory vacation": {"description": "celebration trip", "priority": 3},
        "have celebration lunch": {"description": "celebration lunch", "priority": 2},
        "organize celebratory gathering": {"description": "celebration gathering", "priority": 3},
        "host backyard barbecue": {"description": "backyard BBQ", "priority": 2},
        "plan weekend getaway": {"description": "weekend celebration", "priority": 3},
        "organize potluck celebration": {"description": "celebration potluck", "priority": 2},
        "host game night celebration": {"description": "celebration game night", "priority": 2}
    }
    
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
        }
    }
    
    return celebrations_json

# Generate the JSON data
json_data = generate_celebrations_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/event_types/personal_events/celebrations/vocabulary/ celebrations.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} celebration expressions and saved to celebrations.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["host a birthday party", "celebrate wedding anniversary", "attend graduation ceremony", 
               "plan wedding celebration", "celebrate sobriety anniversary"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')

# If you want to see the raw JSON output
print("\nFull JSON structure:")
print(json.dumps({"celebrations": {
    "description": "Special personal occasions",
    "examples": ["birthday party", "anniversary dinner", "graduation celebration"],
    "vocab": "celebrations.json"
}}, indent=2))