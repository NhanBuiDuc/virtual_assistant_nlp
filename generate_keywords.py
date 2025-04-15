# import json
# import random
# import datetime
# import os
# import glob
# from itertools import product
# import re

# def load_json_file(filepath):
#     """Load content from a JSON file."""
#     try:
#         with open(filepath, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except Exception as e:
#         print(f"Error loading {filepath}: {e}")
#         return {}

# def generate_times():
#     """Generate various time expressions."""
#     # Generate specific times (24-hour and 12-hour format)
#     hours_24 = [f"{h:02d}:00" for h in range(0, 24)]
#     hours_12_am = [f"{h if h > 0 else 12}am" for h in range(0, 12)]
#     hours_12_pm = [f"{h if h > 0 else 12}pm" for h in range(0, 12)]
    
#     # Combine all time formats
#     all_times = hours_24 + hours_12_am + hours_12_pm
    
#     # Add some variations with minutes
#     minute_variations = [f"{h:02d}:{m:02d}" for h in range(0, 24) for m in [15, 30, 45]]
#     random.shuffle(minute_variations)
#     minute_variations = minute_variations[:20]  # Take a subset to avoid too many
    
#     all_times.extend(minute_variations)
#     return all_times

# def generate_dates(num_dates=30):
#     """Generate various date expressions."""
#     today = datetime.datetime.now()
    
#     # Generate absolute dates
#     dates = []
    
#     # Named days (today, tomorrow, etc.)
#     dates.extend(["today", "tomorrow", "the day after tomorrow", "next week", 
#                   "this weekend", "next weekend", "this month", "next month"])
    
#     # Days of week
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     dates.extend(days_of_week)
#     dates.extend([f"next {day}" for day in days_of_week])
#     dates.extend([f"this {day}" for day in days_of_week])
    
#     # Specific dates in different formats
#     for i in range(1, num_dates):
#         future_date = today + datetime.timedelta(days=i)
#         dates.append(future_date.strftime("%B %d"))  # e.g., "April 15"
#         dates.append(future_date.strftime("%m/%d/%Y"))  # e.g., "04/15/2025"
#         dates.append(future_date.strftime("%Y-%m-%d"))  # e.g., "2025-04-15"
    
#     return dates

# def get_vocabulary_file_paths():
#     """Get list of all vocabulary JSON file paths."""
#     vocab_paths = [
#         "data/english/meta/keyword_taxonomy/event_types/work_events/administrative/vocabulary/administrative_tasks.json",
#         "data/english/meta/keyword_taxonomy/event_types/work_events/deadlines/vocabulary/work_deadlines.json",
#         "data/english/meta/keyword_taxonomy/event_types/work_events/meetings/vocabulary/work_meetings_extended.json",
#         "data/english/meta/keyword_taxonomy/event_types/personal_events/errands/vocabulary/errands.json",
#         "data/english/meta/keyword_taxonomy/event_types/personal_events/celebrations/vocabulary/celebrations.json",
#         "data/english/meta/keyword_taxonomy/event_types/personal_events/chores/vocabulary/household_chores.json",
#         "data/english/meta/keyword_taxonomy/time_elements/frequency/vocabulary/frequency.json",
#         "data/english/meta/keyword_taxonomy/time_elements/durations/vocabulary/durations.json",
#         "data/english/meta/keyword_taxonomy/time_elements/time_periods/vocabulary/time_periods.json",
#         "data/english/meta/keyword_taxonomy/time_elements/deadlines/vocabulary/deadlines.json",
#         "data/english/meta/keyword_taxonomy/time_elements/dates/special_days/vocabulary/special_days.json",
#         "data/english/meta/keyword_taxonomy/time_elements/dates/relative_dates/vocabulary/relative_dates.json",
#         "data/english/meta/keyword_taxonomy/time_elements/dates/months/vocabulary/months.json",
#         "data/english/meta/keyword_taxonomy/time_elements/dates/days_of_week/vocabulary/days_of_week.json"
#     ]
    
#     # Filter to only include files that actually exist
#     existing_paths = []
#     for path in vocab_paths:
#         if os.path.exists(path):
#             existing_paths.append(path)
#         else:
#             print(f"Warning: File does not exist: {path}")
    
#     return existing_paths

# def extract_tasks_from_json(json_data):
#     """Extract tasks from JSON data structure."""
#     tasks = []
    
#     # Check if this is a vocabulary file with 'values' field
#     if 'values' in json_data and isinstance(json_data['values'], dict):
#         # Extract keys from the values dictionary
#         tasks.extend(list(json_data['values'].keys()))
    
#     return tasks

# def clean_task(task):
#     """Clean up task text for better readability."""
#     # Replace underscores with spaces
#     task = re.sub(r'_', ' ', task)
    
#     # Make sure first letter is capitalized
#     if task and len(task) > 0:
#         task = task[0].upper() + task[1:]
    
#     return task

# def generate_keyword_combinations(num_combinations=1000):
#     """Generate keyword combinations based on the requested format."""
#     # Get vocabulary file paths
#     vocab_paths = get_vocabulary_file_paths()
    
#     print(f"Found {len(vocab_paths)} vocabulary JSON files")
    
#     # Initialize task lists
#     all_tasks = []
    
#     # Load tasks from each vocabulary file
#     for filepath in vocab_paths:
#         json_data = load_json_file(filepath)
#         if json_data:
#             tasks = extract_tasks_from_json(json_data)
#             all_tasks.extend(tasks)
#             print(f"Extracted {len(tasks)} tasks from {os.path.basename(filepath)}")
    
#     # If we couldn't extract enough tasks, add some default ones
#     if len(all_tasks) < 20:
#         print("Adding default tasks since not enough were found in JSON files")
#         all_tasks.extend([
#             "check email", "attend meeting", "call client", "write report",
#             "prepare presentation", "review document", "send invoice",
#             "organize files", "update website", "create backup",
#             "order supplies", "schedule appointment", "book flight",
#             "reserve hotel", "plan event", "update calendar"
#         ])
    
#     # Clean and deduplicate tasks
#     all_tasks = [clean_task(task) for task in all_tasks]
#     all_tasks = list(set(all_tasks))  # Remove duplicates
#     print(f"Total unique tasks after processing: {len(all_tasks)}")
    
#     # Generate time components
#     times = generate_times()
#     print(f"Generated {len(times)} time expressions")
    
#     dates = generate_dates()
#     print(f"Generated {len(dates)} date expressions")
    
#     # Load time periods
#     time_periods_path = "data/english/meta/keyword_taxonomy/time_elements/time_periods/vocabulary/time_periods.json"
#     time_periods = []
#     if os.path.exists(time_periods_path):
#         time_periods_json = load_json_file(time_periods_path)
#         if time_periods_json and 'values' in time_periods_json:
#             time_periods = list(time_periods_json['values'].keys())
    
#     # Use default time periods if loading fails
#     if not time_periods:
#         time_periods = ["morning", "afternoon", "evening", "night", "dawn", "dusk", 
#                        "early morning", "late morning", "noon", "midnight"]
    
#     print(f"Loaded {len(time_periods)} time periods")
    
#     # Generate intents/action phrases
#     intents = [
#         "I need to", "I want to", "I have to", "Remember to", "Don't forget to",
#         "Need to", "Planning to", "Going to", "Must", "Should"
#     ]
    
#     # Generate combinations
#     combinations = []
    
#     # Format 1: "Today", "I want to", task meeting
#     for date, intent, task in product(
#         dates[:min(20, len(dates))],  # Limit to prevent too many combinations
#         intents[:min(5, len(intents))],
#         random.sample(all_tasks, min(50, len(all_tasks)))
#     ):
#         combination = [f'"{date}"', f'"{intent}"', f'"{task}"']
#         combinations.append(", ".join(combination))
        
#         # Stop if we have enough combinations
#         if len(combinations) >= num_combinations:
#             break
    
#     # Format 2: "Today", "I want to", daily task, "at 14pm"
#     if len(combinations) < num_combinations:
#         for date, intent, task, time in product(
#             dates[:min(10, len(dates))],  # Further limit to prevent too many combinations
#             intents[:min(3, len(intents))],
#             random.sample(all_tasks, min(30, len(all_tasks))),
#             times[:min(10, len(times))]
#         ):
#             combination = [f'"{date}"', f'"{intent}"', f'"{task}"', f'"at {time}"']
#             combinations.append(", ".join(combination))
            
#             # Stop if we have enough combinations
#             if len(combinations) >= num_combinations:
#                 break
    
#     # Format 3: Time period + task
#     if len(combinations) < num_combinations:
#         for period, intent, task in product(
#             time_periods[:min(10, len(time_periods))],
#             intents[:min(3, len(intents))],
#             random.sample(all_tasks, min(20, len(all_tasks)))
#         ):
#             combination = [f'"{period}"', f'"{intent}"', f'"{task}"']
#             combinations.append(", ".join(combination))
            
#             # Stop if we have enough combinations
#             if len(combinations) >= num_combinations:
#                 break
    
#     # Shuffle the combinations
#     random.shuffle(combinations)
    
#     # Return only the requested number
#     return combinations[:num_combinations]

# def save_combinations_to_file(combinations, filename="keyword_combinations.txt", format_type="numbered"):
#     """Save generated combinations to a file with the specified format."""
#     os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
    
#     with open(filename, 'w', encoding='utf-8') as f:
#         if format_type == "numbered":
#             for i, combo in enumerate(combinations, 1):
#                 f.write(f"{i}. {combo}\n")
#         elif format_type == "csv":
#             f.write("index,combination\n")
#             for i, combo in enumerate(combinations, 1):
#                 f.write(f"{i},{combo}\n")
#         elif format_type == "json":
#             import json
#             combo_dict = {i: combo for i, combo in enumerate(combinations, 1)}
#             f.write(json.dumps(combo_dict, indent=2))
#         else:  # plain
#             for combo in combinations:
#                 f.write(f"{combo}\n")
    
#     print(f"Saved {len(combinations)} combinations to {filename}")

# def main():
#     # Create output directory
#     output_dir = "data/english/meta/keyword_combinations"
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Generate 1000 keyword combinations
#     print("Generating keyword combinations...")
#     combinations = generate_keyword_combinations(1000)
    
#     # Save to a file
#     output_file = os.path.join(output_dir, 'keyword_combinations.txt')
#     save_combinations_to_file(combinations, output_file)
    
#     # Also save in other formats
#     save_combinations_to_file(combinations, os.path.join(output_dir, 'keyword_combinations.csv'), "csv")
#     save_combinations_to_file(combinations, os.path.join(output_dir, 'keyword_combinations.json'), "json")
    
#     # Print a sample
#     print(f"\nGenerated {len(combinations)} keyword combinations.")
#     print("\nSample combinations:")
#     for combo in combinations[:10]:
#         print(combo)
#     print(f"\nAll combinations saved to {output_dir}")

# if __name__ == "__main__":
#     main()



import json
import random
import datetime
import os
import glob
from itertools import product
import re

def load_json_file(filepath):
    """Load content from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return {}

def extract_tasks_from_json(json_data):
    """Extract tasks from JSON data structure."""
    tasks = []
    
    # Check if this is a vocabulary file with 'values' field
    if 'values' in json_data and isinstance(json_data['values'], dict):
        # Extract keys from the values dictionary
        tasks.extend(list(json_data['values'].keys()))
    
    return tasks

def clean_task(task):
    """Clean up task text for better readability."""
    # Replace underscores with spaces
    task = re.sub(r'_', ' ', task)
    
    # Make sure first letter is capitalized
    if task and len(task) > 0:
        task = task[0].upper() + task[1:]
    
    return task

def find_all_json_files():
    """Find all relevant JSON files in the data directory structure."""
    # All possible paths where vocabulary files might be found
    base_dir = "data/english/meta/keyword_taxonomy"
    
    json_files = {}
    
    # Look for specific category files first
    categories = {
        "days_of_week": "time_elements/dates/days_of_week/vocabulary/days_of_week.json",
        "dates_months": "time_elements/dates/months/vocabulary/months.json",
        "dates_relative": "time_elements/dates/relative_dates/vocabulary/relative_dates.json",
        "dates_special": "time_elements/dates/special_days/vocabulary/special_days.json",
        "deadlines": "time_elements/deadlines/vocabulary/deadlines.json",
        "durations": "time_elements/durations/vocabulary/durations.json",
        "frequency": "time_elements/frequency/vocabulary/frequency.json",
        "time_periods": "time_elements/time_periods/vocabulary/time_periods.json",
        "work_administrative": "event_types/work_events/administrative/vocabulary/administrative_tasks.json",
        "work_deadlines": "event_types/work_events/deadlines/vocabulary/work_deadlines.json",
        "work_meetings": "event_types/work_events/meetings/vocabulary/work_meetings.json",
        "personal_errands": "event_types/personal_events/errands/vocabulary/errands.json",
        "personal_chores": "event_types/personal_events/chores/vocabulary/household_chores.json",
        "personal_celebrations": "event_types/personal_events/celebrations/vocabulary/celebrations.json",
    }
    
    # Check for each specific file
    for category, rel_path in categories.items():
        full_path = os.path.join(base_dir, rel_path)
        if os.path.exists(full_path):
            json_files[category] = full_path
            print(f"Found {category} vocabulary: {full_path}")
        else:
            print(f"Warning: Could not find {category} vocabulary at {full_path}")
    
    # Add any additional files found
    json_files["common_names"] = "data/english/meta/temp/common_name.json"
    
    return json_files

def load_all_data():
    """Load all data from JSON files."""
    # Find all relevant JSON files
    json_files = find_all_json_files()
    
    # Initialize data structures
    data = {
        "common_names": {
            "Male Names": [],
            "Female Names": [],
            "Unisex Names": [],
            "Organizations": []
        },
        "dates": [],
        "times": [],
        "time_periods": [],
        "durations": [],
        "frequency": [],
        "deadlines": [],
        "special_days": [],
        "tasks": []
    }
    
    # Load names
    if "common_names" in json_files:
        names_data = load_json_file(json_files["common_names"])
        if names_data:
            for category, names in names_data.items():
                if isinstance(names, list):
                    if "Male" in category:
                        data["common_names"]["Male Names"].extend(names)
                    elif "Female" in category:
                        data["common_names"]["Female Names"].extend(names)
                    elif "Unisex" in category:
                        data["common_names"]["Unisex Names"].extend(names)
                elif isinstance(names, dict) and category == "Names by Origin":
                    # Flatten the dictionary
                    for origin, origin_names in names.items():
                        if isinstance(origin_names, list):
                            data["common_names"]["Male Names"].extend(origin_names[:len(origin_names)//2])
                            data["common_names"]["Female Names"].extend(origin_names[len(origin_names)//2:])
    
    # Add organizations
    data["common_names"]["Organizations"] = [
        "Google", "Microsoft", "Apple", "Amazon", "Facebook", "Twitter", 
        "Netflix", "Adobe", "Tesla", "IBM", "Salesforce", "Oracle", "Zoom", 
        "Slack", "Uber", "Airbnb", "Spotify", "Dropbox", "Intel", "Samsung"
    ]
    
    # If no names were loaded, use defaults
    if not data["common_names"]["Male Names"]:
        data["common_names"]["Male Names"] = [
            "James", "John", "Robert", "Michael", "William", "David", "Richard", 
            "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew"
        ]
        
    if not data["common_names"]["Female Names"]:
        data["common_names"]["Female Names"] = [
            "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", 
            "Susan", "Jessica", "Sarah", "Karen", "Lisa", "Nancy", "Betty"
        ]
        
    if not data["common_names"]["Unisex Names"]:
        data["common_names"]["Unisex Names"] = [
            "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", 
            "Jamie", "Cameron", "Blake", "Dakota", "Hayden", "Logan"
        ]
    
    # Load months
    if "dates_months" in json_files:
        months_data = load_json_file(json_files["dates_months"])
        if months_data and "values" in months_data:
            months = list(months_data["values"].keys())
            data["dates"].extend(months)
    
    # Load relative dates
    if "dates_relative" in json_files:
        rel_dates_data = load_json_file(json_files["dates_relative"])
        if rel_dates_data and "values" in rel_dates_data:
            rel_dates = list(rel_dates_data["values"].keys())
            data["dates"].extend(rel_dates)
    
    # Load special days
    if "dates_special" in json_files:
        special_days_data = load_json_file(json_files["dates_special"])
        if special_days_data and "values" in special_days_data:
            special_days = list(special_days_data["values"].keys())
            data["special_days"].extend(special_days)
            data["dates"].extend(special_days)
    
    # Load days of week
    if "days_of_week" in json_files:
        days_data = load_json_file(json_files["days_of_week"])
        if days_data and "values" in days_data:
            days = list(days_data["values"].keys())
            data["dates"].extend(days)
    
    # Load time periods
    if "time_periods" in json_files:
        periods_data = load_json_file(json_files["time_periods"])
        if periods_data and "values" in periods_data:
            periods = list(periods_data["values"].keys())
            data["time_periods"].extend(periods)
    
    # Load durations
    if "durations" in json_files:
        durations_data = load_json_file(json_files["durations"])
        if durations_data and "values" in durations_data:
            durations = list(durations_data["values"].keys())
            data["durations"].extend(durations)
    
    # Load frequency
    if "frequency" in json_files:
        frequency_data = load_json_file(json_files["frequency"])
        if frequency_data and "values" in frequency_data:
            frequency = list(frequency_data["values"].keys())
            data["frequency"].extend(frequency)
    
    # Load deadlines
    if "deadlines" in json_files:
        deadlines_data = load_json_file(json_files["deadlines"])
        if deadlines_data and "values" in deadlines_data:
            deadlines = list(deadlines_data["values"].keys())
            data["deadlines"].extend(deadlines)
    
    # Load tasks from work and personal vocabulary files
    task_files = []
    if "work_administrative" in json_files:
        task_files.append(json_files["work_administrative"])
    if "work_meetings" in json_files:
        task_files.append(json_files["work_meetings"])
    if "personal_errands" in json_files:
        task_files.append(json_files["personal_errands"])
    if "personal_chores" in json_files:
        task_files.append(json_files["personal_chores"])
    
    # Add any additional files that might contain tasks
    if "additional" in json_files:
        task_files.extend(json_files["additional"])
    
    # Load tasks from all relevant files
    for file_path in task_files:
        try:
            task_data = load_json_file(file_path)
            if task_data and "values" in task_data:
                tasks = extract_tasks_from_json(task_data)
                data["tasks"].extend(tasks)
                print(f"Loaded {len(tasks)} tasks from {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error loading tasks from {file_path}: {e}")
    
    # Clean and deduplicate tasks
    data["tasks"] = [clean_task(task) for task in data["tasks"]]
    data["tasks"] = list(set(data["tasks"]))
    
    # Generate times if not loaded from JSON
    data["times"] = generate_times()
    
    # Generate additional dates if needed
    if len(data["dates"]) < 20:
        data["dates"].extend(generate_dates())
    
    # Add default values if needed for any missing categories
    add_default_values(data)
    
    # Print summary of loaded data
    print("\nLoaded Data Summary:")
    print(f"Names: {sum(len(names) for names in data['names'].values())} (Male: {len(data['names']['Male Names'])}, Female: {len(data['names']['Female Names'])}, Unisex: {len(data['names']['Unisex Names'])}, Orgs: {len(data['names']['Organizations'])})")
    print(f"Dates: {len(data['dates'])}")
    print(f"Times: {len(data['times'])}")
    print(f"Time Periods: {len(data['time_periods'])}")
    print(f"Durations: {len(data['durations'])}")
    print(f"Frequency: {len(data['frequency'])}")
    print(f"Deadlines: {len(data['deadlines'])}")
    print(f"Special Days: {len(data['special_days'])}")
    print(f"Tasks: {len(data['tasks'])}")
    
    return data

def add_default_values(data):
    """Add default values for any missing categories."""
    # Default intents
    data["intents"] = [
        "I need to", "I want to", "I have to", "Remember to", "Don't forget to",
        "Need to", "Planning to", "Going to", "Must", "Should", "Supposed to",
        "Committed to", "Scheduled to", "Agreed to", "Promised to", "Expected to"
    ]
    
    # Default time periods if none were loaded
    if not data["time_periods"]:
        data["time_periods"] = [
            "morning", "afternoon", "evening", "night", "dawn", "dusk",
            "early morning", "late morning", "noon", "midnight",
            "early afternoon", "late afternoon", "early evening", "late evening"
        ]
    
    # Default deadlines if none were loaded
    if not data["deadlines"]:
        data["deadlines"] = [
            "by", "before", "due", "deadline", "EOD", "ASAP", "by the end of",
            "no later than", "before the end of", "due by", "prior to", "in advance of"
        ]
    
    # Default durations if none were loaded
    if not data["durations"]:
        data["durations"] = [
            "for an hour", "for 30 minutes", "all day", "overnight", "for a week",
            "for the morning", "for the afternoon", "for the whole day", 
            "until tomorrow", "until noon", "for 45 minutes", "for two hours"
        ]
    
    # Default frequency if none were loaded
    if not data["frequency"]:
        data["frequency"] = [
            "daily", "weekly", "every Monday", "twice a month", "annually", "frequently",
            "every day", "every week", "every month", "twice a week", "every other day"
        ]
    
    # Default tasks if none were loaded
    if not data["tasks"]:
        data["tasks"] = [
            "Send invoice", "Attend meeting", "Schedule appointment", "Reserve hotel",
            "Update website", "Prepare presentation", "Create backup", "Update calendar",
            "Plan event", "Review document", "Book flight", "Organize files", "Call client",
            "Submit report", "Check email", "Finish project", "Follow up with", "Write proposal"
        ]

def generate_times():
    """Generate various time expressions with consistent formatting."""
    # Generate specific times (24-hour and 12-hour format)
    times = []
    
    # 12-hour format with AM/PM
    for hour in range(1, 13):
        for minute in [0, 15, 30, 45]:
            # AM
            if minute == 0:
                times.append(f"{hour}:00 AM")
                times.append(f"{hour} AM")
            else:
                times.append(f"{hour}:{minute:02d} AM")
            
            # PM
            if minute == 0:
                times.append(f"{hour}:00 PM")
                times.append(f"{hour} PM")
            else:
                times.append(f"{hour}:{minute:02d} PM")
    
    # 24-hour format
    for hour in range(0, 24):
        for minute in [0, 15, 30, 45]:
            if minute == 0:
                times.append(f"{hour:02d}:00")
            else:
                times.append(f"{hour:02d}:{minute:02d}")
    
    return times

def generate_dates(num_dates=30):
    """Generate various date expressions with consistent formatting."""
    today = datetime.datetime.now()
    
    # Generate absolute dates
    dates = []
    
    # Named days (today, tomorrow, etc.)
    dates.extend(["today", "tomorrow", "the day after tomorrow", "next week", 
                 "this weekend", "next weekend", "this month", "next month"])
    
    # Days of week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dates.extend(days_of_week)
    dates.extend([f"next {day}" for day in days_of_week])
    dates.extend([f"this {day}" for day in days_of_week])
    
    # Specific dates in different formats
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Add ordinal suffix to day numbers
    def get_ordinal_suffix(day):
        if 10 <= day % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return f"{day}{suffix}"
    
    # Create date formats like "January 15th"
    for month in months:
        for day in [1, 5, 10, 15, 20, 25]:
            dates.append(f"{month} {get_ordinal_suffix(day)}")
    
    # Add more conventional formats (mm/dd/yyyy)
    for i in range(1, num_dates):
        future_date = today + datetime.timedelta(days=i)
        dates.append(future_date.strftime("%m/%d/%Y"))
    
    return dates

def generate_keyword_combinations(data, num_combinations=1000):
    """Generate enhanced keyword combinations with names, times, etc."""
    # Define the different combination patterns
    patterns = [
        # Pattern 1: [DATE] at [TIME], [INTENT], [TASK] with [PERSON]
        lambda: {
            "date": random.choice(data["dates"]),
            "time": random.choice(data["times"]) if random.random() < 0.7 else None,
            "intent": random.choice(data["intents"]),
            "task": random.choice(data["tasks"]),
            "person": get_random_person(data["common_names"])
        },
        
        # Pattern 2: [PERSON] asked me to [TASK] [DEADLINE] [DATE] at [TIME]
        lambda: {
            "person": get_random_person(data["common_names"]),
            "task": random.choice(data["tasks"]),
            "deadline": random.choice(data["deadlines"]),
            "date": random.choice(data["dates"]),
            "time": random.choice(data["times"]) if random.random() < 0.5 else None
        },
        
        # Pattern 3: [FREQUENCY] [TASK] with [PERSON] in the [TIME_PERIOD]
        lambda: {
            "frequency": random.choice(data["frequency"]),
            "task": random.choice(data["tasks"]),
            "person": get_random_person(data["common_names"]),
            "time_period": random.choice(data["time_periods"])
        },
        
        # Pattern 4: [TASK] [DURATION] with [PERSON] on [DATE] at [TIME]
        lambda: {
            "task": random.choice(data["tasks"]),
            "duration": random.choice(data["durations"]),
            "person": get_random_person(data["common_names"]),
            "date": random.choice(data["dates"]),
            "time": random.choice(data["times"]) if random.random() < 0.4 else None
        },
        
        # Pattern 5: [DATE] [TIME_PERIOD], [INTENT] [TASK] with [PERSON]
        lambda: {
            "date": random.choice(data["dates"]),
            "time_period": random.choice(data["time_periods"]),
            "intent": random.choice(data["intents"]),
            "task": random.choice(data["tasks"]),
            "person": get_random_person(data["common_names"])
        },
        
        # Pattern 6: [DEADLINE] [DATE] at [TIME], [PERSON] expects me to [TASK]
        lambda: {
            "deadline": random.choice(data["deadlines"]),
            "date": random.choice(data["dates"]),
            "time": random.choice(data["times"]) if random.random() < 0.6 else None,
            "person": get_random_person(data["common_names"]),
            "task": random.choice(data["tasks"])
        }
    ]
    
    # Function to format a data dictionary based on its pattern
    def format_pattern(pattern_index, data_dict):
        if pattern_index == 0:
            # Pattern 1: [DATE] at [TIME], [INTENT], [TASK] with [PERSON]
            time_part = f" at {data_dict['time']}" if data_dict['time'] else ""
            parts = [f'"{data_dict["date"]}{time_part}"',
                    f'"{data_dict["intent"]}"',
                    f'"{data_dict["task"]} with {data_dict["person"]}"']
            return ", ".join(parts)
            
        elif pattern_index == 1:
            # Pattern 2: [PERSON] asked me to [TASK] [DEADLINE] [DATE] at [TIME]
            time_part = f" at {data_dict['time']}" if data_dict['time'] else ""
            parts = [f'"{data_dict["person"]} asked me to {data_dict["task"]}"',
                    f'"{data_dict["deadline"]}"',
                    f'"{data_dict["date"]}{time_part}"']
            return ", ".join(parts)
            
        elif pattern_index == 2:
            # Pattern 3: [FREQUENCY] [TASK] with [PERSON] in the [TIME_PERIOD]
            parts = [f'"{data_dict["frequency"]}"',
                    f'"{data_dict["task"]} with {data_dict["person"]}"',
                    f'"in the {data_dict["time_period"]}"']
            return ", ".join(parts)
            
        elif pattern_index == 3:
            # Pattern 4: [TASK] [DURATION] with [PERSON] on [DATE] at [TIME]
            time_part = f" at {data_dict['time']}" if data_dict['time'] else ""
            parts = [f'"{data_dict["task"]}"',
                    f'"{data_dict["duration"]}"',
                    f'"with {data_dict["person"]} on {data_dict["date"]}{time_part}"']
            return ", ".join(parts)
            
        elif pattern_index == 4:
            # Pattern 5: [DATE] [TIME_PERIOD], [INTENT] [TASK] with [PERSON]
            parts = [f'"{data_dict["date"]} {data_dict["time_period"]}"',
                    f'"{data_dict["intent"]}"',
                    f'"{data_dict["task"]} with {data_dict["person"]}"']
            return ", ".join(parts)
            
        elif pattern_index == 5:
            # Pattern 6: [DEADLINE] [DATE] at [TIME], [PERSON] expects me to [TASK]
            time_part = f" at {data_dict['time']}" if data_dict['time'] else ""
            parts = [f'"{data_dict["deadline"]} {data_dict["date"]}{time_part}"',
                    f'"{data_dict["person"]} expects me to"',
                    f'"{data_dict["task"]}"']
            return ", ".join(parts)
    
    # Generate combinations
    combinations = []
    
    # Ensure an equal distribution of patterns
    pattern_count = len(patterns)
    patterns_per_combination = num_combinations // pattern_count
    extra_patterns = num_combinations % pattern_count
    
    # Generate combinations from each pattern
    for i in range(pattern_count):
        # Calculate how many combinations to generate with this pattern
        count = patterns_per_combination + (1 if i < extra_patterns else 0)
        
        for _ in range(count):
            # Get data from the pattern generator
            pattern_data = patterns[i]()
            # Format the combination based on the pattern
            combination = format_pattern(i, pattern_data)
            combinations.append(combination)
    
    # Shuffle the combinations to mix up the patterns
    random.shuffle(combinations)
    
    return combinations

def get_random_person(people_data):
    """Get a random person or organization name."""
    # Randomly choose a category
    categories = list(people_data.keys())
    category = random.choice(categories)
    
    # Get a random name from that category
    if people_data[category]:
        return random.choice(people_data[category])
    else:
        # Fallback if the category is empty
        all_names = []
        for names in people_data.values():
            all_names.extend(names)
        return random.choice(all_names) if all_names else "Someone"

def save_combinations_to_file(combinations, filename="keyword_combinations.txt", format_type="numbered"):
    """Save generated combinations to a file with the specified format."""
    os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        if format_type == "numbered":
            for i, combo in enumerate(combinations, 1):
                f.write(f"{i}. {combo}\n")
        elif format_type == "csv":
            f.write("index,combination\n")
            for i, combo in enumerate(combinations, 1):
                # Escape quotes in the combination for CSV format
                escaped_combo = combo.replace('"', '""')
                f.write(f"{i},\"{escaped_combo}\"\n")
        elif format_type == "json":
            combo_dict = {i: combo for i, combo in enumerate(combinations, 1)}
            f.write(json.dumps(combo_dict, indent=2))
        else:  # plain
            for combo in combinations:
                f.write(f"{combo}\n")
    
    print(f"Saved {len(combinations)} combinations to {filename}")

def main():
    # Create output directory
    output_dir = "data/english/meta/keyword_combinations"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get number of combinations to generate (default 1000)
    num_combinations = 1000
    
    # Load all data from JSON files
    print("Loading data from JSON files...")
    all_data = load_all_data()
    
    # Generate keyword combinations
    print(f"Generating {num_combinations} enhanced keyword combinations...")
    combinations = generate_keyword_combinations(all_data, num_combinations)
    
    # Save to various file formats
    output_file = os.path.join(output_dir, 'enhanced_keyword_combinations.txt')
    save_combinations_to_file(combinations, output_file)
    print(f"Saved combinations to {output_file}")
    
    # Also save in other formats
    csv_file = os.path.join(output_dir, 'enhanced_keyword_combinations.csv')
    save_combinations_to_file(combinations, csv_file, "csv")
    print(f"Saved combinations to {csv_file}")
    
    json_file = os.path.join(output_dir, 'enhanced_keyword_combinations.json')
    save_combinations_to_file(combinations, json_file, "json")
    print(f"Saved combinations to {json_file}")
    
    # Print a sample
    print(f"\nGenerated {len(combinations)} enhanced keyword combinations.")
    print("\nSample combinations:")
    for i, combo in enumerate(combinations[:20]):
        print(f"{i + 1}. {combo}")
    print(f"\nAll combinations saved to {output_dir}")

if __name__ == "__main__":
    main()