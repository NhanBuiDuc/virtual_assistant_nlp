import json
import os
from datetime import datetime

def generate_administrative_tasks_json():
    """
    Generate a JSON file with administrative task expressions as commonly spoken.
    Each key is a longer verbal reference to an administrative task, and the value is an object
    containing the primary task attributes requested.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    administrative_tasks = {}
    
    # Helper function to add an item with incremented ID
    def add_task(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        administrative_tasks[key] = {
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
    
    # Paperwork
    add_task(
        "complete required forms",
        "Complete Forms",
        "Fill out necessary forms and documentation",
        "work",
        "administrative",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "fill out necessary documentation",
        "Complete Documentation",
        "Prepare and fill out required documentation",
        "work",
        "administrative",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "process incoming documents",
        "Process Documents",
        "Review and process incoming documents and files",
        "work",
        "administrative",
        True,
        "daily",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "organize office files",
        "Organize Files",
        "Sort, label, and arrange office files and documents",
        "work",
        "administrative",
        True,
        "monthly",
        2,
        "low",
        "low"
    )
    
    add_task(
        "prepare legal documents",
        "Prepare Legal Documents",
        "Draft or complete legal forms and documentation",
        "work",
        "administrative",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    # Financial administration
    add_task(
        "submit expense report",
        "Submit Expenses",
        "Complete and submit expense report for reimbursement",
        "work",
        "administrative",
        True,
        "monthly",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "reconcile credit card statements",
        "Reconcile Credit Cards",
        "Check and verify credit card transactions against records",
        "work",
        "administrative",
        True,
        "monthly",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "create financial reports",
        "Financial Reporting",
        "Generate reports on financial performance and metrics",
        "work",
        "administrative",
        True,
        "monthly",
        4,
        "high",
        "high"
    )
    
    add_task(
        "review department budget",
        "Budget Review",
        "Analyze and evaluate departmental spending against budget",
        "work",
        "administrative",
        True,
        "quarterly",
        4,
        "high",
        "medium"
    )
    
    add_task(
        "prepare tax documentation",
        "Tax Preparation",
        "Gather and organize documents needed for tax filing",
        "work",
        "administrative",
        True,
        "annually",
        5,
        "very high",
        "high"
    )
    
    # Time tracking
    add_task(
        "submit timesheet",
        "Submit Timesheet",
        "Record and submit hours worked for payment processing",
        "work",
        "administrative",
        True,
        "weekly",
        3,
        "medium",
        "high"
    )
    
    add_task(
        "track billable hours",
        "Track Billable Hours",
        "Record time spent on client or billable project work",
        "work",
        "administrative",
        True,
        "daily",
        4,
        "high",
        "high"
    )
    
    add_task(
        "approve team timesheets",
        "Approve Timesheets",
        "Review and approve time records for team members",
        "work",
        "administrative",
        True,
        "weekly",
        3,
        "medium",
        "high"
    )
    
    # HR administration
    add_task(
        "update employee records",
        "Update Employee Records",
        "Maintain current information in employee files and systems",
        "work",
        "administrative",
        True,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    add_task(
        "process new hire paperwork",
        "Process Onboarding",
        "Complete documentation for newly hired employees",
        "work",
        "administrative",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    add_task(
        "manage benefits enrollment",
        "Manage Benefits",
        "Administer employee benefits program and enrollment",
        "work",
        "administrative",
        True,
        "annually",
        4,
        "high",
        "medium"
    )
    
    add_task(
        "document disciplinary actions",
        "Document Disciplinary Actions",
        "Record formal disciplinary measures taken with employees",
        "work",
        "administrative",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    # Office management
    add_task(
        "order office supplies",
        "Order Supplies",
        "Purchase necessary supplies for office operations",
        "work",
        "administrative",
        True,
        "monthly",
        2,
        "low",
        "low"
    )
    
    add_task(
        "coordinate office maintenance",
        "Coordinate Maintenance",
        "Schedule and oversee office repairs and maintenance",
        "work",
        "administrative",
        True,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "book meeting rooms",
        "Book Meeting Rooms",
        "Reserve appropriate spaces for meetings and events",
        "work",
        "administrative",
        True,
        "as needed",
        2,
        "low",
        "medium"
    )
    
    # Communication administration
    add_task(
        "take meeting minutes",
        "Take Minutes",
        "Record discussions and decisions during meetings",
        "work",
        "administrative",
        True,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "distribute company announcements",
        "Distribute Announcements",
        "Share important company information with employees",
        "work",
        "administrative",
        True,
        "as needed",
        3,
        "medium",
        "high"
    )
    
    # Travel administration
    add_task(
        "book business travel",
        "Book Travel",
        "Arrange transportation for business trips",
        "work",
        "administrative",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "coordinate international travel documents",
        "Coordinate Travel Documents",
        "Ensure proper documentation for international business travel",
        "work",
        "administrative",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    # Compliance and reporting
    add_task(
        "complete compliance training",
        "Complete Compliance Training",
        "Finish required regulatory or compliance education",
        "work",
        "administrative",
        True,
        "annually",
        4,
        "high",
        "medium"
    )
    
    add_task(
        "submit regulatory reports",
        "Submit Regulatory Reports",
        "File required reports with governing agencies",
        "work",
        "administrative",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    add_task(
        "maintain license renewals",
        "Maintain Licenses",
        "Ensure timely renewal of required business licenses",
        "work",
        "administrative",
        True,
        "annually",
        5,
        "very high",
        "high"
    )
    
    # Project administration
    add_task(
        "update project tracking system",
        "Update Project Tracking",
        "Maintain current information in project management tools",
        "work",
        "administrative",
        True,
        "weekly",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "prepare status reports",
        "Prepare Status Reports",
        "Create updates on project progress and metrics",
        "work",
        "administrative",
        True,
        "weekly",
        3,
        "medium",
        "high"
    )
    
    add_task(
        "track project milestones",
        "Track Milestones",
        "Monitor and record project progress against key milestones",
        "work",
        "administrative",
        True,
        "weekly",
        4,
        "high",
        "medium"
    )
    
    # IT administration
    add_task(
        "update software licenses",
        "Update Software Licenses",
        "Renew and maintain software licensing for organization",
        "work",
        "administrative",
        True,
        "annually",
        3,
        "medium",
        "medium"
    )
    
    add_task(
        "manage user accounts",
        "Manage User Accounts",
        "Create, update, or deactivate system user accounts",
        "work",
        "administrative",
        True,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    # Create the final JSON object
    administrative_tasks_json = {
        "description": "Administrative tasks as commonly expressed in workplace conversation",
        "examples": ["paperwork", "expense report", "timesheet", "budget review"],
        "values": administrative_tasks,
        "priority_scale": {
            "1": "Very Low - Optional administrative tasks",
            "2": "Low - Routine maintenance tasks",
            "3": "Medium - Regular operational administrative tasks",
            "4": "High - Important administrative requirements",
            "5": "Very High - Critical compliance or regulatory tasks"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return administrative_tasks_json

# Generate the JSON data
json_data = generate_administrative_tasks_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/work_events/administrative/vocabulary/administrative_tasks.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} administrative task expressions and saved to administrative_tasks.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["submit expense report", "update employee records", "book business travel", 
               "maintain license renewals", "submit timesheet"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')