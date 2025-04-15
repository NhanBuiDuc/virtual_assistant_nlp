import json

def generate_special_days_json():
    """
    Generate a JSON file with holidays and special occasions commonly observed in Western cultures.
    """
    special_days = {
        # Major holidays
        "New Year's": "New Year's",
        "New Year's Day": "New Year's Day",
        "New Year's Eve": "New Year's Eve",
        "Valentine's Day": "Valentine's Day",
        "St. Patrick's Day": "St. Patrick's Day",
        "Saint Patrick's Day": "St. Patrick's Day",
        "Easter": "Easter",
        "Easter Sunday": "Easter",
        "Good Friday": "Good Friday",
        "Easter Monday": "Easter Monday",
        "April Fools' Day": "April Fools' Day",
        "April Fool's Day": "April Fools' Day",
        "Mother's Day": "Mother's Day",
        "Mothers Day": "Mother's Day",
        "Memorial Day": "Memorial Day",
        "Father's Day": "Father's Day",
        "Fathers Day": "Father's Day",
        "Independence Day": "Independence Day",
        "Fourth of July": "Independence Day",
        "4th of July": "Independence Day",
        "Labor Day": "Labor Day",
        "Columbus Day": "Columbus Day",
        "Indigenous Peoples' Day": "Indigenous Peoples' Day",
        "Halloween": "Halloween",
        "All Saints' Day": "All Saints' Day",
        "Veterans Day": "Veterans Day",
        "Veteran's Day": "Veterans Day",
        "Thanksgiving": "Thanksgiving",
        "Thanksgiving Day": "Thanksgiving",
        "Black Friday": "Black Friday",
        "Cyber Monday": "Cyber Monday",
        "Christmas": "Christmas",
        "Christmas Eve": "Christmas Eve",
        "Christmas Day": "Christmas Day",
        "Boxing Day": "Boxing Day",
        "Kwanzaa": "Kwanzaa",
        
        # Religious holidays
        "Ash Wednesday": "Ash Wednesday",
        "Palm Sunday": "Palm Sunday",
        "Maundy Thursday": "Maundy Thursday",
        "Holy Saturday": "Holy Saturday",
        "Pentecost": "Pentecost",
        "Advent": "Advent",
        "Epiphany": "Epiphany",
        "Hanukkah": "Hanukkah",
        "Chanukah": "Hanukkah",
        "Passover": "Passover",
        "Rosh Hashanah": "Rosh Hashanah",
        "Yom Kippur": "Yom Kippur",
        "Ramadan": "Ramadan",
        "Eid al-Fitr": "Eid al-Fitr",
        "Eid al-Adha": "Eid al-Adha",
        
        # Secular observances
        "Groundhog Day": "Groundhog Day",
        "Super Bowl Sunday": "Super Bowl Sunday",
        "Super Bowl": "Super Bowl",
        "Presidents' Day": "Presidents' Day",
        "Presidents Day": "Presidents' Day",
        "Earth Day": "Earth Day",
        "Cinco de Mayo": "Cinco de Mayo",
        "Juneteenth": "Juneteenth",
        "Summer Solstice": "Summer Solstice",
        "Winter Solstice": "Winter Solstice",
        "Tax Day": "Tax Day",
        "Daylight Saving Time": "Daylight Saving Time",
        "Election Day": "Election Day",
        
        # Personal occasions
        "birthday": "birthday",
        "Birthday": "birthday",
        "anniversary": "anniversary",
        "Anniversary": "anniversary",
        "wedding": "wedding",
        "Wedding": "wedding",
        "graduation": "graduation",
        "Graduation": "graduation",
        "retirement": "retirement",
        "Retirement": "retirement",
        "baby shower": "baby shower",
        "Baby shower": "baby shower",
        "bridal shower": "bridal shower",
        "Bridal shower": "bridal shower",
        "funeral": "funeral",
        "Funeral": "funeral",
        "reunion": "reunion",
        "Reunion": "reunion",
        
        # Other special days
        "Martin Luther King Jr. Day": "Martin Luther King Jr. Day",
        "MLK Day": "Martin Luther King Jr. Day",
        "Arbor Day": "Arbor Day",
        "Flag Day": "Flag Day",
        "Mardi Gras": "Mardi Gras",
        "Fat Tuesday": "Mardi Gras",
        "St. Valentine's Day": "Valentine's Day",
        "Saint Valentine's Day": "Valentine's Day",
        "May Day": "May Day",
        
        # International observances
        "International Women's Day": "International Women's Day",
        "World Health Day": "World Health Day",
        "World Environment Day": "World Environment Day",
        "International Children's Day": "International Children's Day",
        "International Youth Day": "International Youth Day",
        "World Peace Day": "World Peace Day",
        "International Day of Peace": "International Day of Peace",
        "Human Rights Day": "Human Rights Day",
        
        # Cultural/national holidays from various Western countries
        "Bastille Day": "Bastille Day",
        "Guy Fawkes Night": "Guy Fawkes Night",
        "Bonfire Night": "Guy Fawkes Night",
        "Remembrance Day": "Remembrance Day",
        "Anzac Day": "Anzac Day",
        "Australia Day": "Australia Day",
        "Canada Day": "Canada Day",
        "Victoria Day": "Victoria Day",
        "Oktoberfest": "Oktoberfest",
        "Burns Night": "Burns Night",
        "St. George's Day": "St. George's Day",
        "Saint George's Day": "St. George's Day",
        
        # Seasonal markers
        "First day of Spring": "First day of Spring",
        "First day of Summer": "First day of Summer",
        "First day of Autumn": "First day of Autumn",
        "First day of Fall": "First day of Fall",
        "First day of Winter": "First day of Winter"
    }
    
    # Create the final JSON object
    special_days_json = {
        "description": "Holidays and special occasions in Western cultures",
        "examples": ["Christmas", "New Year's", "birthday", "anniversary", "Valentine's Day"],
        "values": special_days
    }
    
    return special_days_json

# Generate the JSON data
json_data = generate_special_days_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/dates/special_days/vocabulary/special_days.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} special days and saved to special_days.json")