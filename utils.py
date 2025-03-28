import json
import random

# Time mapping from MS-LaTTE format to human-readable
time_mapping = {
    "WD-morning": "weekday morning",
    "WD-afternoon": "weekday afternoon",
    "WD-evening": "weekday evening",
    "WD-night": "weekday night",
    "WD-anytime": "anytime on weekdays",
    "WE-morning": "weekend morning",
    "WE-afternoon": "weekend afternoon",
    "WE-evening": "weekend evening",
    "WE-night": "weekend night",
    "WE-anytime": "anytime on weekends"
}

# Load the MS-LaTTE data
def load_ms_latte_data(file_path=None):
    """Load and parse MS-LaTTE data from a file path or JSON string.
    
    Args:
        file_path: Path to the MS-LaTTE JSON file
        json_str: JSON string containing MS-LaTTE data
        
    Returns:
        List of tasks or empty list if loading fails
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def generate_task_original(openings, tasks, connectors, time_refs, fillers):
    """The original task generation function as fallback."""
    
    opening = random.choice(openings)
    task_type = random.choice(list(tasks.keys()))
    task = random.choice(tasks[task_type])
    connector = random.choice(connectors)
    time_ref = random.choice(time_refs)
    
    # Fill placeholders (e.g., "{person}" → "John")
    for placeholder, options in fillers.items():
        if f"{{{placeholder}}}" in task:
            task = task.replace(f"{{{placeholder}}}", random.choice(options))
        if f"{{{placeholder}}}" in time_ref:
            time_ref = time_ref.replace(f"{{{placeholder}}}", str(random.choice(options)))
            
    if "{task}" in opening:
        opening = opening.replace(f"{{task}}", task)
        sentence = f"{opening}{connector} {time_ref}".capitalize()
        return sentence       
    else:
        # Combine into a sentence
        sentence = f"{opening} {task} {connector} {time_ref}".capitalize()
        return sentence

def generate_task_from_ms_latte(task_entry, openings, tasks, connectors, time_refs, fillers):
    """Generate a task using the MS-LaTTE data."""
    if not task_entry:
        return generate_task_original(openings, tasks, connectors, time_refs, fillers)  # Fallback to original method
    
    task_title = task_entry.get("TaskTitle", "do something")
    list_title = task_entry.get("ListTitle", "")
    
    # Get location information if available
    location = ""
    if task_entry.get("LocJudgements"):
        # Filter judgements where Known is "yes"
        known_judgements = [j for j in task_entry["LocJudgements"] if j.get("Known") == "yes"]
        if known_judgements:
            loc_judgment = random.choice(known_judgements)
            locations = loc_judgment.get("Locations", "").split(",")
            public_locations = loc_judgment.get("PublicLocations", "").split(",")
            
            # Filter out empty strings
            locations = [loc for loc in locations if loc]
            public_locations = [loc for loc in public_locations if loc]
            
            if public_locations and random.random() > 0.3:  # 70% chance to mention public location if available
                location = f" at the {random.choice(public_locations)}"
            elif locations and random.random() > 0.5:  # 50% chance to include general location
                location = f" at {random.choice(locations)}"
    
    # Get time information if available
    time_info = ""
    if task_entry.get("TimeJudgements"):
        # Filter judgements where Known is "yes"
        known_judgements = [j for j in task_entry["TimeJudgements"] if j.get("Known") == "yes"]
        if known_judgements:
            time_judgment = random.choice(known_judgements)
            times = time_judgment.get("Times", "").split(",")
            if times and times[0]:  # Ensure there's at least one non-empty time
                selected_time = random.choice(times)
                readable_time = time_mapping.get(selected_time, selected_time)
                
                # Sometimes use the time mapping, sometimes use more specific time references
                if random.random() > 0.5:
                    connector = random.choice(connectors)
                    time_info = f" {connector} {readable_time}"
                else:
                    # Use more specific time references based on the time period
                    if "morning" in selected_time:
                        specific_time = random.choice(["9:00 AM", "10:30 AM", "tomorrow morning", "in the morning"])
                    elif "afternoon" in selected_time:
                        specific_time = random.choice(["2:00 PM", "3:30 PM", "tomorrow afternoon", "in the afternoon"])
                    elif "evening" in selected_time:
                        specific_time = random.choice(["6:00 PM", "7:30 PM", "tonight", "this evening"])
                    elif "night" in selected_time:
                        specific_time = random.choice(["9:00 PM", "10:00 PM", "tonight", "before bed"])
                    else:
                        # For "anytime" or other cases, use general time reference
                        specific_time = random.choice(time_refs)
                        for placeholder, options in fillers.items():
                            if f"{{{placeholder}}}" in specific_time:
                                specific_time = specific_time.replace(f"{{{placeholder}}}", str(random.choice(options)))
                    
                    connector = random.choice(connectors)
                    time_info = f" {connector} {specific_time}"
    
    # Generate the sentence
    opening = random.choice(openings)
    sentence = f"{opening} {task_title}{location}{time_info}"
    
    # Add list context sometimes
    if list_title and list_title != "default list" and random.random() > 0.7:  # 30% chance to include list context
        sentence += f" (from {list_title} list)"
        
    return sentence.capitalize()