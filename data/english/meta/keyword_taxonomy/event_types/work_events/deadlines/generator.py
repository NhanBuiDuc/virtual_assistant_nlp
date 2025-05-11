import json
import os
from datetime import datetime

def generate_work_deadlines_json():
    """
    Generate a JSON file with work deadline expressions as commonly spoken.
    Each key is a longer verbal reference to a work deadline, and the value is an object
    containing the primary task attributes requested.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    deadline_types = {}
    
    # Helper function to add an item with incremented ID
    def add_deadline(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        deadline_types[key] = {
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
    
    # Project deadlines
    add_deadline(
        "final date for project completion",
        "Project Deadline",
        "Date by which all project deliverables must be completed",
        "work",
        "deadline",
        False,
        "project-based",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "last day to submit project deliverables",
        "Project Submission",
        "Final day for submitting completed project work",
        "work",
        "deadline",
        False,
        "project-based",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "cutoff date for project submission",
        "Project Cutoff",
        "Final acceptable date for project completion",
        "work",
        "deadline",
        False,
        "project-based",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "target date for finishing project",
        "Project Target",
        "Desired completion date for project work",
        "work",
        "deadline",
        False,
        "project-based",
        4,
        "high",
        "high"
    )
    
    add_deadline(
        "approaching project completion date",
        "Upcoming Deadline",
        "Project deadline that is coming up soon",
        "work",
        "deadline",
        False,
        "project-based",
        4,
        "high",
        "high"
    )
    
    # Delivery deadlines
    add_deadline(
        "last date for client deliverable",
        "Delivery Deadline",
        "Final date for providing deliverables to client",
        "work",
        "deadline",
        False,
        "project-based",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "date promised to deliver work",
        "Promised Delivery",
        "Date committed to client for work completion",
        "work",
        "deadline",
        False,
        "project-based",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "contractual date for delivery",
        "Contractual Deadline",
        "Legally binding date for work completion",
        "work",
        "deadline",
        False,
        "contract-based",
        5,
        "very high",
        "very high"
    )
    
    # Review deadlines
    add_deadline(
        "end of quarterly review period",
        "Quarterly Review",
        "Deadline for quarterly performance or business evaluation",
        "work",
        "deadline",
        True,
        "quarterly",
        4,
        "high",
        "medium"
    )
    
    add_deadline(
        "annual review submission deadline",
        "Annual Review",
        "Deadline for yearly performance review documentation",
        "work",
        "deadline",
        True,
        "annually",
        4,
        "high",
        "medium"
    )
    
    add_deadline(
        "performance review due date",
        "Performance Review",
        "Date for completing employee performance evaluation",
        "work",
        "deadline",
        True,
        "annually",
        4,
        "high",
        "medium"
    )
    
    add_deadline(
        "deadline for peer reviews",
        "Peer Review Deadline",
        "Final date to submit peer evaluation feedback",
        "work",
        "deadline",
        True,
        "quarterly",
        3,
        "medium",
        "medium"
    )
    
    # Application deadlines
    add_deadline(
        "final date for job application",
        "Application Deadline",
        "Last day to submit job application materials",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "grant proposal submission date",
        "Grant Deadline",
        "Due date for submitting grant application",
        "work",
        "deadline",
        False,
        "grant cycle",
        5,
        "very high",
        "high"
    )
    
    # Financial deadlines
    add_deadline(
        "tax filing due date",
        "Tax Deadline",
        "Required date for tax document submission",
        "work",
        "deadline",
        True,
        "annually",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "invoice payment due date",
        "Payment Due",
        "Date by which payment must be received",
        "work",
        "deadline",
        True,
        "monthly",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "expense report submission deadline",
        "Expense Deadline",
        "Final date to submit expense documentation",
        "work",
        "deadline",
        True,
        "monthly",
        4,
        "high",
        "medium"
    )
    
    add_deadline(
        "fiscal year close date",
        "Fiscal Close",
        "End of financial reporting year",
        "work",
        "deadline",
        True,
        "annually",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "quarterly financial report due",
        "Quarterly Filing",
        "Due date for quarterly financial statements",
        "work",
        "deadline",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    # Administrative deadlines
    add_deadline(
        "timesheet submission deadline",
        "Timesheet Due",
        "Date by which work hours must be reported",
        "work",
        "deadline",
        True,
        "weekly",
        3,
        "medium",
        "high"
    )
    
    add_deadline(
        "vacation request deadline",
        "Vacation Request",
        "Last day to submit time-off requests",
        "work",
        "deadline",
        False,
        "as needed",
        2,
        "low",
        "low"
    )
    
    add_deadline(
        "benefits enrollment deadline",
        "Benefits Enrollment",
        "Final date to select employee benefits options",
        "work",
        "deadline",
        True,
        "annually",
        4,
        "high",
        "high"
    )
    
    add_deadline(
        "certification renewal deadline",
        "Certification Deadline",
        "Date by which professional certification must be renewed",
        "work",
        "deadline",
        True,
        "annually",
        5,
        "very high",
        "high"
    )
    
    # Publication deadlines
    add_deadline(
        "publication submission deadline",
        "Submission Deadline",
        "Final date for submitting content for publication",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "conference paper deadline",
        "Conference Deadline",
        "Due date for academic conference submission",
        "work",
        "deadline",
        False,
        "annual conference",
        5,
        "very high",
        "high"
    )
    
    # Time-related expressions
    add_deadline(
        "fast approaching deadline",
        "Urgent Deadline",
        "Any deadline requiring immediate attention",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "time-sensitive deliverable",
        "Time-Sensitive",
        "Task with tight time constraints",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "work due as soon as possible",
        "ASAP",
        "Task requiring immediate completion",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "work needed by end of day",
        "EOD",
        "Task that must be completed by day's end",
        "work",
        "deadline",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    add_deadline(
        "deadline extended by one week",
        "Extended Deadline",
        "Task with deadline pushed to a later date",
        "work",
        "deadline",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_deadline(
        "hard deadline with no extensions",
        "Hard Deadline",
        "Absolutely final date with no possibility of extension",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    add_deadline(
        "flexible completion date",
        "Soft Deadline",
        "Target date that can be adjusted if needed",
        "work",
        "deadline",
        False,
        "as needed",
        2,
        "low",
        "low"
    )
    
    # Group deadlines
    add_deadline(
        "team submission deadline",
        "Team Deadline",
        "Due date for work from an entire team",
        "work",
        "deadline",
        False,
        "project-based",
        4,
        "high",
        "high"
    )
    
    add_deadline(
        "organization-wide deadline",
        "Company Deadline",
        "Deadline affecting the entire organization",
        "work",
        "deadline",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "client-imposed deadline",
        "Client Deadline",
        "Due date set by client requirements",
        "work",
        "deadline",
        False,
        "client-determined",
        5,
        "very high",
        "high"
    )
    
    add_deadline(
        "regulatory compliance deadline",
        "Regulatory Deadline",
        "Due date mandated by law or regulation",
        "work",
        "deadline",
        True,
        "varies",
        5,
        "very high",
        "very high"
    )
    
    # Create the final JSON object
    work_deadlines_json = {
        "description": "Work due dates and deadlines as commonly expressed in conversation",
        "examples": ["project deadline", "submission due date", "quarterly review"],
        "values": deadline_types,
        "priority_scale": {
            "1": "Very Low - Minimal consequences if missed",
            "2": "Low - Minor implications if not met",
            "3": "Medium - Noticeable impact if missed",
            "4": "High - Significant consequences if not met",
            "5": "Very High - Critical, must not be missed"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return work_deadlines_json

# Generate the JSON data
json_data = generate_work_deadlines_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/work_events/deadlines/vocabulary/work_deadlines.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} work deadline expressions and saved to work_deadlines.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["final date for project completion", "work needed by end of day", "tax filing due date", 
               "deadline extended by one week", "time-sensitive deliverable"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')