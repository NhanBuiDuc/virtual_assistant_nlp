import random
import json
from utils import *


# Your original data (keeping for fallback)
LANGUAGE = "english"
DATA_DIR = "data"

# Define paths
opening_path = f"{DATA_DIR}/{LANGUAGE}/meta/opening.json"
ms_latte_path = f"{DATA_DIR}/{LANGUAGE}/MS-LaTTE.json"

# Randomly select components
with open(opening_path, "r", encoding="utf-8") as f:
    openings = json.load(f)

openings = sum(openings.values(), [])  # Flatten all categories into a single list


# Original task templates (keeping for variety)
tasks = {
    "homework": ["math homework", "coding assignment", "essay", "project"],
    "meeting": ["meeting with {person}", "team sync", "client call"],
    "errand": ["grocery shopping", "doctor's appointment", "pick up {item}"]
}

connectors = ["due", "at", "by", "on", "before", "around", "starting"]

time_refs = [
    "tomorrow", "next {day}", "tonight", "in {n} days", 
    "this {time}", "{hour}:{minute} {ampm}", "noon", "midnight"
]

# Fillers for naturalness
fillers = {
    "person": ["John", "Alice", "the team", "HR"],
    "day": ["Monday", "Friday", "week", "month"],
    "time": ["morning", "afternoon", "evening"],
    "hour": [9, 10, 2, 3, 6],
    "minute": ["00", "15", "30", "45"],
    "ampm": ["AM", "PM"],
    "item": ["milk", "package", "dry cleaning"],
    "n": [1, 2, 3, 5]
}

# Example usage
def main(ms_latte_source=None):

    """Generate sample tasks using either MS-LaTTE data or original method.
    
    Args:
        ms_latte_source: Path to MS-LaTTE JSON file or JSON string
    """

    count=100

    use_ms_latte_ratio=0.0
    
    # Try to load data from the source
    ms_latte_data = []

    if ms_latte_source:
        ms_latte_data = load_ms_latte_data(file_path=ms_latte_source)
    
    task_list = []

    for _ in range(count):

        random_entry = ms_latte_data.pop(random.randrange(len(ms_latte_data)))

        if random_entry and random.random() < use_ms_latte_ratio:
            task = generate_task_from_ms_latte(random_entry, openings, tasks, connectors, time_refs, fillers)
        else:
            task = generate_task_original(openings, tasks, connectors, time_refs, fillers)

        task_list.append(task)
    
    # Print the tasks
    print("=== Generated Tasks ===")

    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":

    # Run with MS-LaTTE data file path
    # You can modify this to your actual file path
    
    main(ms_latte_path)
    