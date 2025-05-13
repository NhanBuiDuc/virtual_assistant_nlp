import json
import os
import random
from datetime import datetime, timedelta

def load_json_file(file_path):
    """Load a JSON file and return its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        return f"Error loading {file_path}: {str(e)}"

# Base path for JSON files
base_path = "data/english/meta/keyword_taxonomy"

# Define file categories and paths
file_categories = {
    "tasks": [
        f"{base_path}/event_types/work_events/administrative/vocabulary/administrative_tasks.json",
        f"{base_path}/event_types/personal_events/errands/vocabulary/errands.json",
        f"{base_path}/event_types/personal_events/chores/vocabulary/household_chores.json"
    ],
    "events": [
        f"{base_path}/event_types/work_events/meetings/vocabulary/work_meetings.json",
        f"{base_path}/event_types/personal_events/celebrations/vocabulary/celebrations.json"
    ],
    "time_elements": [
        f"{base_path}/time_elements/frequency/vocabulary/frequency.json",
        f"{base_path}/time_elements/durations/vocabulary/durations.json",
        f"{base_path}/time_elements/time_periods/vocabulary/time_periods.json"
    ],
    "date_elements": [
        f"{base_path}/time_elements/dates/special_days/vocabulary/special_days.json",
        f"{base_path}/time_elements/dates/relative_dates/vocabulary/relative_dates.json",
        f"{base_path}/time_elements/dates/months/vocabulary/months.json",
        f"{base_path}/time_elements/dates/days_of_week/vocabulary/days_of_week.json"
    ],
    "specific_times": [
        f"{base_path}/time_elements/specific_times/vocabulary/specific_time.json"
    ]
}

# Load all JSON files
loaded_data = {}
for category, file_paths in file_categories.items():
    loaded_data[category] = {}
    for file_path in file_paths:
        file_name = os.path.basename(file_path).split('.')[0]
        loaded_data[category][file_name] = load_json_file(file_path)

def generate_labeled_combinations(num_combinations=100, combinations_file="combinations.json", labels_file="labels.json"):
    """
    Generate random combinations of tasks, times, dates, etc. with structured labels.
    Output to two separate files: combinations and labels.
    """
    combinations = []  # For text combinations
    labels = []  # For structured labels
    combination_id = 1
    
    for _ in range(num_combinations):
        # Choose a primary element (task or event)
        primary_category = random.choice(["tasks", "events"])
        primary_subcategory = random.choice(list(loaded_data[primary_category].keys()))
        primary_data = loaded_data[primary_category][primary_subcategory]
        
        # Get a random key from the primary element
        primary_keys = list(primary_data["values"].keys())
        primary_key = random.choice(primary_keys)
        primary_value = primary_data["values"][primary_key]
        
        # Decide how many additional elements to include (1-3)
        num_additional_elements = random.randint(1, 3)
        
        # Choose which additional categories to include
        available_categories = ["time_elements", "date_elements", "specific_times"]
        selected_categories = random.sample(available_categories, min(num_additional_elements, len(available_categories)))
        
        # Build the combination
        combination_texts = [primary_key]
        combination_labels = {
            "task": extract_task_labels(primary_value, primary_category, primary_subcategory),
            "time": {
                "minute": 0,
                "hour": 0,
                "day": 0,
                "week": 0,
                "month": 0,
                "year": 0,
                "period": None,
                "frequency": None,
                "duration": None,
                "specific_time": None,
                "second": 0
            },
            "detail": {
                "priority": primary_value.get("priority", None),
                "importance": primary_value.get("importance", None),
                "urgency": primary_value.get("urgency", None),
                "complexity": None,
                "is_recurring": primary_value.get("is_recurring", False)
            }
        }
        
        # Add additional elements
        for category in selected_categories:
            subcategory = random.choice(list(loaded_data[category].keys()))
            data = loaded_data[category][subcategory]
            
            # Get a random key
            keys = list(data["values"].keys())
            key = random.choice(keys)
            value = data["values"][key]
            
            # Add to combination
            combination_texts.append(key)
            
            # Extract relevant labels
            if category == "time_elements":
                if subcategory == "frequency":
                    update_frequency_labels(combination_labels, value)
                elif subcategory == "durations":
                    update_duration_labels(combination_labels, value)
                elif subcategory == "time_periods":
                    update_time_period_labels(combination_labels, value)
            elif category == "date_elements":
                if subcategory == "special_days":
                    update_special_day_labels(combination_labels, value)
                elif subcategory == "relative_dates":
                    update_relative_date_labels(combination_labels, value)
                elif subcategory == "months":
                    update_month_labels(combination_labels, value)
                elif subcategory == "days_of_week":
                    update_days_of_week_labels(combination_labels, value)
            elif category == "specific_times":
                update_specific_time_labels(combination_labels, value)
        
        # Add to our separate lists with the same ID
        combinations.append({
            "id": combination_id,
            "combination": combination_texts
        })
        
        labels.append({
            "id": combination_id,
            "label": combination_labels
        })
        
        combination_id += 1
    
    # Write combinations to file
    with open(combinations_file, 'w', encoding='utf-8') as f:
        json.dump({
            "description": "Generated combinations of tasks, times, dates for language model training",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "combinations": combinations
        }, f, indent=2)
    
    # Write labels to file
    with open(labels_file, 'w', encoding='utf-8') as f:
        json.dump({
            "description": "Structured labels for task combinations",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "labels": labels
        }, f, indent=2)
    
    return combinations, labels

def extract_task_labels(task_value, category, subcategory):
    """Extract task-specific labels from a task or event."""
    task_labels = {
        "id": task_value.get("id", None),
        "title": task_value.get("title", None),
        "description": task_value.get("description", None),
        "category": task_value.get("category", category),
        "event_type": task_value.get("event_type", subcategory)
    }
    return task_labels

def update_frequency_labels(labels, frequency_value):
    """Update time labels with frequency information."""
    labels["time"]["frequency"] = frequency_value.get("standard_form", None)
    
    # Set recurring flag if frequency is specified
    labels["detail"]["is_recurring"] = True
    
    # Extract time components
    for unit in ["second", "minute", "hour", "day", "week", "month", "year"]:
        if frequency_value.get(unit) is not None:
            labels["time"][unit] = frequency_value.get(unit, 0)

def update_duration_labels(labels, duration_value):
    """Update time labels with duration information."""
    labels["time"]["duration"] = duration_value.get("standard_form", None)
    
    # Extract time components
    for unit in ["second", "minute", "hour", "day", "week", "month", "year"]:
        if duration_value.get(unit) is not None:
            labels["time"][unit] = duration_value.get(unit, 0)
    
    # Update period if specified
    if duration_value.get("time_period") is not None:
        labels["time"]["period"] = duration_value.get("time_period", None)

def update_time_period_labels(labels, period_value):
    """Update time labels with time period information."""
    labels["time"]["period"] = period_value.get("standard_form", None)
    
    # Add information about start and end hours to the period field
    if period_value.get("start_hour") is not None and period_value.get("end_hour") is not None:
        start_hour = period_value.get("start_hour", 0)
        end_hour = period_value.get("end_hour", 0)
        if labels["time"]["period"]:
            labels["time"]["period"] += f" ({start_hour}:00-{end_hour}:00)"
    
    # Set hour if available (use start_hour as a reference)
    if period_value.get("start_hour") is not None:
        labels["time"]["hour"] = period_value.get("start_hour", 0)

def update_special_day_labels(labels, special_day_value):
    """Update time labels with special day information."""
    # Set date to special day
    if special_day_value.get("standard_form") is not None:
        labels["time"]["period"] = special_day_value.get("standard_form", None)
    
    # Set month if available
    if special_day_value.get("month_of_year") is not None:
        labels["time"]["month"] = special_day_value.get("month_of_year", 0)
    
    # Set day if available
    if special_day_value.get("date") is not None:
        labels["time"]["day"] = special_day_value.get("date", 0)

def update_relative_date_labels(labels, relative_date_value):
    """Update time labels with relative date information."""
    # Extract time components
    for unit in ["second", "minute", "hour", "day", "week", "month", "year"]:
        if relative_date_value.get(unit) is not None:
            labels["time"][unit] = relative_date_value.get(unit, 0)
    
    # Add to period if available
    if relative_date_value.get("standard_form") is not None:
        labels["time"]["period"] = relative_date_value.get("standard_form", None)

def update_month_labels(labels, month_value):
    """Update time labels with month information."""
    labels["time"]["month"] = month_value.get("month_in_year", 0)

def update_days_of_week_labels(labels, day_value):
    """Update time labels with day of week information."""
    # Set day of week as period
    if day_value.get("standard_form") is not None:
        labels["time"]["period"] = day_value.get("standard_form", None)

def update_specific_time_labels(labels, specific_time_value):
    """Update time labels with specific time information."""
    # Set specific_time to the standard form
    labels["time"]["specific_time"] = specific_time_value.get("standard_form", None)
    
    # Set day and month if available
    if specific_time_value.get("day") is not None:
        labels["time"]["day"] = specific_time_value.get("day", 0)
    
    if specific_time_value.get("month") is not None:
        labels["time"]["month"] = specific_time_value.get("month", 0)

# Generate and save combinations and labels to separate files
combinations, labels = generate_labeled_combinations(10000, "combinations.json", "labels.json")

# Print a sample to show the split files
print("\nSample generated combination:")
print(json.dumps(combinations[0], indent=2))

print("\nCorresponding labels (same ID):")
print(json.dumps(labels[0], indent=2))