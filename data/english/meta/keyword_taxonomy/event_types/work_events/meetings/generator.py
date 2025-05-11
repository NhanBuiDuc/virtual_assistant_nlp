import json
import os
from datetime import datetime

def generate_work_meetings_json():
    """
    Generate a JSON file with work meeting expressions as commonly spoken.
    Each key is a longer verbal reference to a work meeting, and the value is an object
    containing the primary task attributes requested.
    """
    # Counter for simple ID generation
    id_counter = 1
    
    meeting_types = {}
    
    # Helper function to add an item with incremented ID
    def add_meeting(key, title, description, category, event_type, is_recurring, frequency, priority, importance, urgency):
        nonlocal id_counter
        meeting_types[key] = {
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
    
    # General meetings
    add_meeting(
        "general business meeting",
        "Business Meeting",
        "Standard professional meeting for business purposes",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "meeting with team members",
        "Team Meeting",
        "Meeting with immediate team or workgroup",
        "work",
        "meeting",
        True,
        "weekly",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting with staff",
        "Staff Meeting",
        "Meeting with staff members reporting to you",
        "work",
        "meeting",
        True,
        "weekly",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting with department",
        "Department Meeting",
        "Meeting involving all members of a department",
        "work",
        "meeting",
        True,
        "monthly",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting with entire company",
        "Company Meeting",
        "Meeting including all company employees",
        "work",
        "meeting",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "meeting with clients",
        "Client Meeting",
        "Meeting with external clients or customers",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "meeting with vendors",
        "Vendor Meeting",
        "Meeting with suppliers or service providers",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "meeting with project stakeholders",
        "Stakeholder Meeting",
        "Meeting with all parties interested in a project",
        "work",
        "meeting",
        True,
        "biweekly",
        5,
        "very high",
        "high"
    )
    
    # Conference calls
    add_meeting(
        "multi-person phone meeting",
        "Conference Call",
        "Meeting conducted via telephone with multiple participants",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "participate in a multi-person phone meeting",
        "Join Conference Call",
        "Connect to and attend a telephone meeting",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "organize and lead a multi-person phone meeting",
        "Host Conference Call",
        "Set up and facilitate a telephone meeting",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    # Video meetings
    add_meeting(
        "meeting via video conferencing",
        "Video Call",
        "Meeting conducted through video technology",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "formal meeting via video technology",
        "Video Conference",
        "Formal meeting conducted through video platform",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting held online rather than in person",
        "Virtual Meeting",
        "Remote meeting conducted through digital means",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "medium"
    )
    
    # Presentations
    add_meeting(
        "formal display of information to an audience",
        "Presentation",
        "Delivery of prepared information to a group",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "high"
    )
    
    add_meeting(
        "presentation to sell an idea or product",
        "Pitch",
        "Persuasive presentation to gain support or sales",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "presentation to potential investors",
        "Investor Pitch",
        "Presentation seeking financial investment",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "very high"
    )
    
    # Workshops
    add_meeting(
        "interactive learning or planning session",
        "Workshop",
        "Collaborative session focused on learning or creating",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "lead an interactive learning session",
        "Run Workshop",
        "Facilitate a collaborative learning experience",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "interactive session focused on developing strategy",
        "Strategy Session",
        "Collaborative meeting to develop strategic plans",
        "work",
        "meeting",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    # Interviews
    add_meeting(
        "formal meeting to assess a candidate",
        "Interview",
        "Meeting to evaluate a person for a position",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "candidate evaluation conducted by video call",
        "Video Interview",
        "Remote candidate assessment using video technology",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "meeting to evaluate a candidate for employment",
        "Job Interview",
        "Assessment of potential employee's qualifications",
        "work",
        "meeting",
        False,
        "as needed",
        5,
        "very high",
        "high"
    )
    
    # Other professional gatherings
    add_meeting(
        "meeting focused on generating ideas",
        "Brainstorm",
        "Collaborative session to develop new ideas",
        "work",
        "meeting",
        False,
        "as needed",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting between two individuals",
        "One-on-One",
        "Private meeting between two people",
        "work",
        "meeting",
        True,
        "weekly",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "brief alignment meeting",
        "Sync",
        "Short meeting to align on priorities or status",
        "work",
        "meeting",
        True,
        "daily",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "brief status update meeting",
        "Check-in",
        "Short meeting to provide progress updates",
        "work",
        "meeting",
        True,
        "daily",
        3,
        "medium",
        "medium"
    )
    
    add_meeting(
        "initial meeting to start a project",
        "Kickoff",
        "First meeting to launch a project or initiative",
        "work",
        "meeting",
        False,
        "project start",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "meeting to review completed activities",
        "Debrief",
        "Post-activity discussion to review outcomes",
        "work",
        "meeting",
        False,
        "as needed",
        3,
        "medium",
        "low"
    )
    
    add_meeting(
        "meeting to analyze a completed project",
        "Post-mortem",
        "Analysis of a completed project to identify learnings",
        "work",
        "meeting",
        False,
        "project end",
        4,
        "high",
        "low"
    )
    
    add_meeting(
        "meeting with all staff or team members",
        "All-hands",
        "Meeting including all employees in an organization",
        "work",
        "meeting",
        True,
        "quarterly",
        5,
        "very high",
        "high"
    )
    
    # Formal meetings
    add_meeting(
        "formal meeting of board members",
        "Board Meeting",
        "Official meeting of company board of directors",
        "work",
        "meeting",
        True,
        "quarterly",
        5,
        "very high",
        "very high"
    )
    
    add_meeting(
        "meeting of a designated committee",
        "Committee Meeting",
        "Meeting of a specific working group or committee",
        "work",
        "meeting",
        True,
        "monthly",
        4,
        "high",
        "medium"
    )
    
    add_meeting(
        "meeting of company executives",
        "Executive Meeting",
        "Meeting of organization's leadership team",
        "work",
        "meeting",
        True,
        "weekly",
        5,
        "very high",
        "high"
    )
    
    add_meeting(
        "yearly formal meeting of shareholders",
        "AGM",
        "Annual General Meeting for company shareholders",
        "work",
        "meeting",
        True,
        "annually",
        5,
        "very high",
        "very high"
    )
    
    # Create the final JSON object
    work_meetings_json = {
        "description": "Professional gatherings as commonly expressed in conversation",
        "examples": ["meeting", "conference call", "presentation", "workshop", "interview"],
        "values": meeting_types,
        "priority_scale": {
            "1": "Very Low - Minimal impact on work",
            "2": "Low - Limited impact on day-to-day work",
            "3": "Medium - Standard business activity",
            "4": "High - Important for project success",
            "5": "Very High - Critical for business outcomes"
        },
        "schema_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return work_meetings_json

# Generate the JSON data
json_data = generate_work_meetings_json()

# Write to a file
output_path = 'data/english/meta/keyword_taxonomy/event_types/work_events/meetings/vocabulary/work_meetings.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create directories if they don't exist
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} work meeting expressions and saved to work_meetings.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["multi-person phone meeting", "interactive learning or planning session", "formal display of information to an audience", 
               "meeting between two individuals", "brief alignment meeting"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')