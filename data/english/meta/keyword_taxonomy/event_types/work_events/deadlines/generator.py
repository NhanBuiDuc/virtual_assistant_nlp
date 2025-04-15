import json

def generate_work_deadlines_json():
    """
    Generate a JSON file with work deadline expressions as commonly spoken.
    Each key is a longer verbal reference to a work deadline, and the value is an object
    containing a description (shorter standardized term) and a priority level.
    """
    deadline_types = {
        # Project deadlines
        "final date for project completion": {"description": "project deadline", "priority": 5},
        "last day to submit project deliverables": {"description": "project due date", "priority": 5},
        "cutoff date for project submission": {"description": "project cutoff", "priority": 5},
        "target date for finishing project": {"description": "project target", "priority": 4},
        "date by which project must be completed": {"description": "project completion date", "priority": 5},
        "end of project timeline": {"description": "project end date", "priority": 5},
        "approaching project completion date": {"description": "upcoming deadline", "priority": 4},
        "date approaching for project submission": {"description": "deadline approaching", "priority": 4},
        "time remaining until project is due": {"description": "time left", "priority": 3},
        
        # Delivery deadlines
        "last date for client deliverable": {"description": "delivery deadline", "priority": 5},
        "date promised to deliver work": {"description": "promised delivery", "priority": 5},
        "contractual date for delivery": {"description": "contractual deadline", "priority": 5},
        "final submission time for deliverable": {"description": "submission deadline", "priority": 5},
        "date work must be handed over": {"description": "handover date", "priority": 5},
        "target for client delivery": {"description": "delivery target", "priority": 4},
        "timeframe to deliver all requirements": {"description": "delivery window", "priority": 4},
        
        # Review deadlines
        "end of quarterly review period": {"description": "quarterly review", "priority": 4},
        "annual review submission deadline": {"description": "annual review", "priority": 4},
        "performance review due date": {"description": "performance review", "priority": 4},
        "deadline for peer reviews": {"description": "peer review deadline", "priority": 3},
        "last day to submit feedback": {"description": "feedback deadline", "priority": 3},
        "code review response timeframe": {"description": "code review deadline", "priority": 4},
        "document review turnaround time": {"description": "review turnaround", "priority": 3},
        
        # Application deadlines
        "final date for job application": {"description": "application deadline", "priority": 5},
        "grant proposal submission date": {"description": "grant deadline", "priority": 5},
        "last day to apply for position": {"description": "application cutoff", "priority": 5},
        "deadline to submit resume": {"description": "resume deadline", "priority": 5},
        "closing date for job posting": {"description": "posting closure", "priority": 4},
        "application window closing date": {"description": "application window", "priority": 4},
        
        # Financial deadlines
        "tax filing due date": {"description": "tax deadline", "priority": 5},
        "invoice payment due date": {"description": "payment due", "priority": 5},
        "expense report submission deadline": {"description": "expense deadline", "priority": 4},
        "budget request cutoff date": {"description": "budget deadline", "priority": 4},
        "fiscal year close date": {"description": "fiscal close", "priority": 5},
        "quarterly financial report due": {"description": "quarterly filing", "priority": 5},
        "annual financial statement deadline": {"description": "annual filing", "priority": 5},
        "reimbursement claim deadline": {"description": "reimbursement deadline", "priority": 3},
        
        # Academic deadlines
        "assignment due date": {"description": "assignment deadline", "priority": 4},
        "paper submission deadline": {"description": "paper deadline", "priority": 5},
        "research proposal due date": {"description": "proposal deadline", "priority": 5},
        "thesis submission deadline": {"description": "thesis deadline", "priority": 5},
        "coursework completion date": {"description": "coursework deadline", "priority": 4},
        "final exam date": {"description": "exam date", "priority": 5},
        "application for graduation deadline": {"description": "graduation application", "priority": 4},
        
        # Administrative deadlines
        "timesheet submission deadline": {"description": "timesheet due", "priority": 3},
        "vacation request deadline": {"description": "vacation request", "priority": 2},
        "leave application cutoff date": {"description": "leave request", "priority": 2},
        "benefits enrollment deadline": {"description": "benefits enrollment", "priority": 4},
        "form submission due date": {"description": "form deadline", "priority": 3},
        "required training completion date": {"description": "training deadline", "priority": 4},
        "certification renewal deadline": {"description": "certification deadline", "priority": 5},
        "compliance document due date": {"description": "compliance deadline", "priority": 5},
        
        # Publication deadlines
        "publication submission deadline": {"description": "submission deadline", "priority": 5},
        "abstract submission due date": {"description": "abstract deadline", "priority": 4},
        "journal article submission cutoff": {"description": "article deadline", "priority": 5},
        "book manuscript due date": {"description": "manuscript deadline", "priority": 5},
        "editorial revisions due date": {"description": "revisions deadline", "priority": 4},
        "conference paper deadline": {"description": "conference deadline", "priority": 5},
        "print material submission date": {"description": "print deadline", "priority": 5},
        
        # Time-related expressions
        "fast approaching deadline": {"description": "urgent deadline", "priority": 5},
        "immediate deliverable required": {"description": "immediate deadline", "priority": 5},
        "time-sensitive deliverable": {"description": "time-sensitive", "priority": 5},
        "work due as soon as possible": {"description": "ASAP", "priority": 5},
        "work needed by end of day": {"description": "EOD", "priority": 4},
        "due by close of business today": {"description": "COB", "priority": 4},
        "needed by end of business": {"description": "EOB", "priority": 4},
        "work required by end of week": {"description": "EOW", "priority": 3},
        "deadline extended by one week": {"description": "extended deadline", "priority": 3},
        "hard deadline with no extensions": {"description": "hard deadline", "priority": 5},
        "flexible completion date": {"description": "soft deadline", "priority": 2},
        "target date rather than deadline": {"description": "target date", "priority": 2},
        "approaching point of no return": {"description": "critical deadline", "priority": 5},
        
        # Group deadlines
        "team submission deadline": {"description": "team deadline", "priority": 4},
        "department reporting deadline": {"description": "department deadline", "priority": 4},
        "organization-wide deadline": {"description": "company deadline", "priority": 5},
        "multi-team project deadline": {"description": "cross-team deadline", "priority": 5},
        "deadline affecting all stakeholders": {"description": "stakeholder deadline", "priority": 5},
        "client-imposed deadline": {"description": "client deadline", "priority": 5},
        "regulatory compliance deadline": {"description": "regulatory deadline", "priority": 5}
    }
    
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
        }
    }
    
    return work_deadlines_json

# Generate the JSON data
json_data = generate_work_deadlines_json()

# Write to a file
with open('data/english/meta/keyword_taxonomy/event_types/work_events/deadlines/vocabulary/work_deadlines.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} work deadline expressions and saved to work_deadlines.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["final date for project completion", "work needed by end of day", "tax filing due date", 
               "deadline extended by one week", "time-sensitive deliverable"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')

# If you want to see the raw JSON output
print("\nFull JSON structure:")
print(json.dumps({"deadlines": {
    "description": "Work due dates",
    "examples": ["project deadline", "submission due date", "quarterly review"],
    "vocab": "work_deadlines.json"
}}, indent=2))