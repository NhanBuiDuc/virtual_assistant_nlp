import json
import os
from datetime import datetime

def generate_special_days_json():
    """
    Generate a JSON file with holidays and special occasions commonly observed in Western cultures.
    Each special day includes its date (day of month) and month_of_year (month number) when applicable.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    special_days = {}
    
    # Helper function to add a special day with incremented ID
    def add_special_day(key, standard_form, date=None, month_of_year=None):
        """
        Add a special day with date information.
        key: The spoken form of the special day
        standard_form: The normalized name of the special day
        date: Day of month (1-31, or null if variable)
        month_of_year: Month number (1-12, or null if variable)
        """
        nonlocal id_counter
        special_days[key] = {
            "id": id_counter,
            "standard_form": standard_form,
            "date": date,
            "month_of_year": month_of_year
        }
        id_counter += 1
    
    # Major holidays
    add_special_day("New Year's", "New Year's Day", 1, 1)
    add_special_day("New Year's Day", "New Year's Day", 1, 1)
    add_special_day("New Year's Eve", "New Year's Eve", 31, 12)
    add_special_day("Valentine's Day", "Valentine's Day", 14, 2)
    add_special_day("St. Patrick's Day", "St. Patrick's Day", 17, 3)
    add_special_day("Saint Patrick's Day", "St. Patrick's Day", 17, 3)
    add_special_day("Easter", "Easter", None, None)  # Variable date
    add_special_day("Easter Sunday", "Easter", None, None)  # Variable date
    add_special_day("Good Friday", "Good Friday", None, None)  # Variable date
    add_special_day("Easter Monday", "Easter Monday", None, None)  # Variable date
    add_special_day("April Fools' Day", "April Fools' Day", 1, 4)
    add_special_day("April Fool's Day", "April Fools' Day", 1, 4)
    add_special_day("Mother's Day", "Mother's Day", None, 5)  # Second Sunday in May
    add_special_day("Mothers Day", "Mother's Day", None, 5)
    add_special_day("Memorial Day", "Memorial Day", None, 5)  # Last Monday in May
    add_special_day("Father's Day", "Father's Day", None, 6)  # Third Sunday in June
    add_special_day("Fathers Day", "Father's Day", None, 6)
    add_special_day("Independence Day", "Independence Day", 4, 7)
    add_special_day("Fourth of July", "Independence Day", 4, 7)
    add_special_day("4th of July", "Independence Day", 4, 7)
    add_special_day("Labor Day", "Labor Day", None, 9)  # First Monday in September
    add_special_day("Columbus Day", "Columbus Day", None, 10)  # Second Monday in October
    add_special_day("Indigenous Peoples' Day", "Indigenous Peoples' Day", None, 10)
    add_special_day("Halloween", "Halloween", 31, 10)
    add_special_day("All Saints' Day", "All Saints' Day", 1, 11)
    add_special_day("Veterans Day", "Veterans Day", 11, 11)
    add_special_day("Veteran's Day", "Veterans Day", 11, 11)
    add_special_day("Thanksgiving", "Thanksgiving", None, 11)  # Fourth Thursday in November
    add_special_day("Thanksgiving Day", "Thanksgiving", None, 11)
    add_special_day("Black Friday", "Black Friday", None, 11)  # Day after Thanksgiving
    add_special_day("Cyber Monday", "Cyber Monday", None, 11)  # Monday after Thanksgiving
    add_special_day("Christmas", "Christmas", 25, 12)
    add_special_day("Christmas Eve", "Christmas Eve", 24, 12)
    add_special_day("Christmas Day", "Christmas", 25, 12)
    add_special_day("Boxing Day", "Boxing Day", 26, 12)
    add_special_day("Kwanzaa", "Kwanzaa", 26, 12)  # Starts December 26
    
    # Religious holidays
    add_special_day("Ash Wednesday", "Ash Wednesday", None, None)  # Variable date
    add_special_day("Palm Sunday", "Palm Sunday", None, None)  # Variable date
    add_special_day("Maundy Thursday", "Maundy Thursday", None, None)  # Variable date
    add_special_day("Holy Saturday", "Holy Saturday", None, None)  # Variable date
    add_special_day("Pentecost", "Pentecost", None, None)  # Variable date
    add_special_day("Advent", "Advent", None, 12)  # Starts four Sundays before Christmas
    add_special_day("Epiphany", "Epiphany", 6, 1)
    add_special_day("Hanukkah", "Hanukkah", None, None)  # Variable date
    add_special_day("Chanukah", "Hanukkah", None, None)  # Variable date
    add_special_day("Passover", "Passover", None, None)  # Variable date
    add_special_day("Rosh Hashanah", "Rosh Hashanah", None, None)  # Variable date
    add_special_day("Yom Kippur", "Yom Kippur", None, None)  # Variable date
    add_special_day("Ramadan", "Ramadan", None, None)  # Variable date
    add_special_day("Eid al-Fitr", "Eid al-Fitr", None, None)  # Variable date
    add_special_day("Eid al-Adha", "Eid al-Adha", None, None)  # Variable date
    
    # Secular observances
    add_special_day("Groundhog Day", "Groundhog Day", 2, 2)
    add_special_day("Super Bowl Sunday", "Super Bowl Sunday", None, 2)  # Variable Sunday in February
    add_special_day("Super Bowl", "Super Bowl Sunday", None, 2)
    add_special_day("Presidents' Day", "Presidents' Day", None, 2)  # Third Monday in February
    add_special_day("Presidents Day", "Presidents' Day", None, 2)
    add_special_day("Earth Day", "Earth Day", 22, 4)
    add_special_day("Cinco de Mayo", "Cinco de Mayo", 5, 5)
    add_special_day("Juneteenth", "Juneteenth", 19, 6)
    add_special_day("Summer Solstice", "Summer Solstice", None, 6)  # Around June 21
    add_special_day("Winter Solstice", "Winter Solstice", None, 12)  # Around December 21
    add_special_day("Tax Day", "Tax Day", 15, 4)  # Usually April 15
    add_special_day("Election Day", "Election Day", None, 11)  # First Tuesday after November 1
    
    # Personal occasions
    add_special_day("birthday", "Birthday", None, None)
    add_special_day("Birthday", "Birthday", None, None)
    add_special_day("anniversary", "Anniversary", None, None)
    add_special_day("Anniversary", "Anniversary", None, None)
    add_special_day("wedding", "Wedding", None, None)
    add_special_day("Wedding", "Wedding", None, None)
    add_special_day("graduation", "Graduation", None, None)
    add_special_day("Graduation", "Graduation", None, None)
    add_special_day("retirement", "Retirement", None, None)
    add_special_day("Retirement", "Retirement", None, None)
    add_special_day("baby shower", "Baby Shower", None, None)
    add_special_day("Baby shower", "Baby Shower", None, None)
    add_special_day("bridal shower", "Bridal Shower", None, None)
    add_special_day("Bridal shower", "Bridal Shower", None, None)
    add_special_day("funeral", "Funeral", None, None)
    add_special_day("Funeral", "Funeral", None, None)
    add_special_day("reunion", "Reunion", None, None)
    add_special_day("Reunion", "Reunion", None, None)
    
    # Other special days
    add_special_day("Martin Luther King Jr. Day", "Martin Luther King Jr. Day", None, 1)  # Third Monday in January
    add_special_day("MLK Day", "Martin Luther King Jr. Day", None, 1)
    add_special_day("Arbor Day", "Arbor Day", None, 4)  # Usually last Friday in April
    add_special_day("Flag Day", "Flag Day", 14, 6)
    add_special_day("Mardi Gras", "Mardi Gras", None, None)  # Variable date
    add_special_day("Fat Tuesday", "Mardi Gras", None, None)  # Variable date
    add_special_day("St. Valentine's Day", "Valentine's Day", 14, 2)
    add_special_day("Saint Valentine's Day", "Valentine's Day", 14, 2)
    add_special_day("May Day", "May Day", 1, 5)
    
    # International observances
    add_special_day("International Women's Day", "International Women's Day", 8, 3)
    add_special_day("World Health Day", "World Health Day", 7, 4)
    add_special_day("World Environment Day", "World Environment Day", 5, 6)
    add_special_day("International Children's Day", "International Children's Day", 1, 6)
    add_special_day("International Youth Day", "International Youth Day", 12, 8)
    add_special_day("World Peace Day", "International Day of Peace", 21, 9)
    add_special_day("International Day of Peace", "International Day of Peace", 21, 9)
    add_special_day("Human Rights Day", "Human Rights Day", 10, 12)
    
    # Cultural/national holidays from various Western countries
    add_special_day("Bastille Day", "Bastille Day", 14, 7)
    add_special_day("Guy Fawkes Night", "Guy Fawkes Night", 5, 11)
    add_special_day("Bonfire Night", "Guy Fawkes Night", 5, 11)
    add_special_day("Remembrance Day", "Remembrance Day", 11, 11)
    add_special_day("Anzac Day", "Anzac Day", 25, 4)
    add_special_day("Australia Day", "Australia Day", 26, 1)
    add_special_day("Canada Day", "Canada Day", 1, 7)
    add_special_day("Victoria Day", "Victoria Day", None, 5)  # Monday before May 25
    add_special_day("Oktoberfest", "Oktoberfest", None, 9)  # Starts in September
    add_special_day("Burns Night", "Burns Night", 25, 1)
    add_special_day("St. George's Day", "St. George's Day", 23, 4)
    add_special_day("Saint George's Day", "St. George's Day", 23, 4)
    
    # Seasonal markers
    add_special_day("First day of Spring", "First day of Spring", None, 3)  # Around March 20
    add_special_day("First day of Summer", "First day of Summer", None, 6)  # Around June 21
    add_special_day("First day of Autumn", "First day of Autumn", None, 9)  # Around September 22
    add_special_day("First day of Fall", "First day of Fall", None, 9)  # Around September 22
    add_special_day("First day of Winter", "First day of Winter", None, 12)  # Around December 21
    
    # Create the final JSON object
    special_days_json = {
        "description": "Holidays and special occasions in Western cultures",
        "examples": ["Christmas", "New Year's", "birthday", "anniversary", "Valentine's Day"],
        "values": special_days,
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return special_days_json

# Generate the JSON data
json_data = generate_special_days_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/time_elements/dates/special_days/vocabulary/special_days.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} special days and saved to special_days.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["Christmas", "Independence Day", "birthday", "Valentine's Day"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')