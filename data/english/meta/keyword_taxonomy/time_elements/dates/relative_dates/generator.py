import json

def generate_relative_dates_with_minutes():
    """
    Generate a JSON dictionary with relative date expressions as keys
    and approximate number of minutes relative to today as values.
    Positive values represent future dates, negative values represent past dates.
    """
    relative_dates_dict = {}
    
    # Constants for time calculations
    MINUTES_PER_DAY = 24 * 60  # 1440 minutes in a day
    MINUTES_PER_WEEK = 7 * MINUTES_PER_DAY  # 10080 minutes in a week
    MINUTES_PER_MONTH = 30 * MINUTES_PER_DAY  # ~43200 minutes in a month (approximation)
    MINUTES_PER_YEAR = 365 * MINUTES_PER_DAY  # ~525600 minutes in a year (approximation)
    
    # Basic date units with their minute values
    date_unit_minutes = {
        "day": MINUTES_PER_DAY,
        "week": MINUTES_PER_WEEK,
        "month": MINUTES_PER_MONTH,
        "year": MINUTES_PER_YEAR,
        "days": MINUTES_PER_DAY,
        "weeks": MINUTES_PER_WEEK,
        "months": MINUTES_PER_MONTH,
        "years": MINUTES_PER_YEAR
    }
    
    # Number words with their numeric values
    number_word_values = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
        "a": 1, "an": 1
    }
    
    # Common specific relative dates
    specific_dates = {
        "today": 0,
        "tomorrow": MINUTES_PER_DAY,
        "yesterday": -MINUTES_PER_DAY,
        "day after tomorrow": 2 * MINUTES_PER_DAY,
        "day before yesterday": -2 * MINUTES_PER_DAY,
        "this week": 0,
        "this month": 0,
        "this year": 0,
        "next week": MINUTES_PER_WEEK,
        "next month": MINUTES_PER_MONTH,
        "next year": MINUTES_PER_YEAR,
        "last week": -MINUTES_PER_WEEK,
        "last month": -MINUTES_PER_MONTH,
        "last year": -MINUTES_PER_YEAR,
        "beginning of the week": -MINUTES_PER_DAY * 3,  # Approximation (middle of week to beginning)
        "end of the week": MINUTES_PER_DAY * 3,  # Approximation (middle of week to end)
        "beginning of the month": -MINUTES_PER_DAY * 15,  # Approximation
        "end of the month": MINUTES_PER_DAY * 15,  # Approximation
        "beginning of the year": -MINUTES_PER_DAY * 182,  # Approximation
        "end of the year": MINUTES_PER_DAY * 182,  # Approximation
        "earlier this week": -MINUTES_PER_DAY * 2,  # Approximation
        "later this week": MINUTES_PER_DAY * 2,  # Approximation
        "earlier this month": -MINUTES_PER_DAY * 10,  # Approximation
        "later this month": MINUTES_PER_DAY * 10,  # Approximation
        "earlier this year": -MINUTES_PER_DAY * 90,  # Approximation
        "later this year": MINUTES_PER_DAY * 90,  # Approximation
        "the day after": MINUTES_PER_DAY,
        "the day before": -MINUTES_PER_DAY,
        "the following day": MINUTES_PER_DAY,
        "the previous day": -MINUTES_PER_DAY
    }
    relative_dates_dict.update(specific_dates)
    
    # Weekday references (approximation - assume the middle of the week is "today")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_offsets = {
        "Monday": -3, "Tuesday": -2, "Wednesday": -1, 
        "Thursday": 0, "Friday": 1, "Saturday": 2, "Sunday": 3
    }
    
    for day in weekdays:
        offset_days = weekday_offsets[day]
        relative_dates_dict[f"next {day}"] = (offset_days + 7) * MINUTES_PER_DAY
        relative_dates_dict[f"last {day}"] = (offset_days - 7) * MINUTES_PER_DAY
        relative_dates_dict[f"this {day}"] = offset_days * MINUTES_PER_DAY
        relative_dates_dict[f"coming {day}"] = (offset_days + 7) * MINUTES_PER_DAY
        relative_dates_dict[f"previous {day}"] = (offset_days - 7) * MINUTES_PER_DAY
    
    # Generate expressions with numbers and date units
    # Format: "X [date unit] ago", "X [date unit] from now", "in X [date unit]"
    for unit, minutes in date_unit_minutes.items():
        # Using number words
        for word, value in number_word_values.items():
            unit_value = minutes * value
            relative_dates_dict[f"{word} {unit} ago"] = -unit_value
            relative_dates_dict[f"{word} {unit} from now"] = unit_value
            relative_dates_dict[f"in {word} {unit}"] = unit_value
        
        # Using digits
        for digit in range(1, 101):
            if digit <= 20 or digit % 10 == 0:  # Keep the set reasonable
                unit_value = minutes * digit
                relative_dates_dict[f"{digit} {unit} ago"] = -unit_value
                relative_dates_dict[f"{digit} {unit} from now"] = unit_value
                relative_dates_dict[f"in {digit} {unit}"] = unit_value
        
        # Add with direction indicators
        if not unit.endswith('s'):  # Singular forms
            relative_dates_dict[f"last {unit}"] = -minutes
            relative_dates_dict[f"next {unit}"] = minutes
            relative_dates_dict[f"this {unit}"] = 0
            relative_dates_dict[f"coming {unit}"] = minutes
            relative_dates_dict[f"previous {unit}"] = -minutes
            relative_dates_dict[f"following {unit}"] = minutes
            relative_dates_dict[f"upcoming {unit}"] = minutes
            relative_dates_dict[f"past {unit}"] = -minutes
    
    # Add expressions with "few" (approximate as 3)
    for unit, minutes in date_unit_minutes.items():
        if unit.endswith('s'):  # Only use plural forms
            few_value = minutes * 3
            relative_dates_dict[f"a few {unit} ago"] = -few_value
            relative_dates_dict[f"a few {unit} from now"] = few_value
            relative_dates_dict[f"in a few {unit}"] = few_value
    
    # Add expressions with "couple" (approximate as 2)
    for unit, minutes in date_unit_minutes.items():
        if unit.endswith('s'):  # Only use plural forms
            couple_value = minutes * 2
            relative_dates_dict[f"a couple of {unit} ago"] = -couple_value
            relative_dates_dict[f"a couple of {unit} from now"] = couple_value
            relative_dates_dict[f"in a couple of {unit}"] = couple_value
            relative_dates_dict[f"couple of {unit} ago"] = -couple_value
            relative_dates_dict[f"couple of {unit} from now"] = couple_value
            relative_dates_dict[f"in couple of {unit}"] = couple_value
    
    # More complex expressions for singular units
    for unit, minutes in date_unit_minutes.items():
        if not unit.endswith('s'):  # Only use singular forms
            # Approximation: earlier/later in a period means about 1/3 of the period
            period_third = minutes // 3
            relative_dates_dict[f"earlier this {unit}"] = -period_third
            relative_dates_dict[f"later this {unit}"] = period_third
            relative_dates_dict[f"beginning of this {unit}"] = -(minutes // 2)
            relative_dates_dict[f"end of this {unit}"] = (minutes // 2)
            relative_dates_dict[f"middle of this {unit}"] = 0
            relative_dates_dict[f"start of the {unit}"] = -(minutes // 2)
            relative_dates_dict[f"end of the {unit}"] = (minutes // 2)
    
    # Add some date range expressions (using approximations)
    relative_dates_dict["over the next few days"] = MINUTES_PER_DAY * 3
    relative_dates_dict["over the past few days"] = -MINUTES_PER_DAY * 3
    relative_dates_dict["over the next few weeks"] = MINUTES_PER_WEEK * 3
    relative_dates_dict["over the past few weeks"] = -MINUTES_PER_WEEK * 3
    relative_dates_dict["over the coming months"] = MINUTES_PER_MONTH * 3
    relative_dates_dict["over the past months"] = -MINUTES_PER_MONTH * 3
    relative_dates_dict["in the coming days"] = MINUTES_PER_DAY * 3
    relative_dates_dict["in the past days"] = -MINUTES_PER_DAY * 3
    relative_dates_dict["within the next week"] = MINUTES_PER_WEEK // 2
    relative_dates_dict["within the past week"] = -MINUTES_PER_WEEK // 2
    
    # Create the final JSON object
    relative_dates_json = {
        "description": "Dates relative to today, with keys as the verbal and values are number in minutes",
        "examples": {
            "tomorrow": MINUTES_PER_DAY,
            "yesterday": -MINUTES_PER_DAY,
            "next week": MINUTES_PER_WEEK,
            "in two days": MINUTES_PER_DAY * 2,
            "last month": -MINUTES_PER_MONTH
        },
        "values": relative_dates_dict
    }
    
    return relative_dates_json

# Generate the JSON data
json_data = generate_relative_dates_with_minutes()

# Write to a file
with open('data/english/meta/keyword_taxonomy/time_elements/dates/relative_dates/vocabulary/relative_dates.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} relative date expressions with minute values and saved to relative_dates.json")

# If you want to see the output in the console as well
# print(json.dumps(json_data, indent=2))