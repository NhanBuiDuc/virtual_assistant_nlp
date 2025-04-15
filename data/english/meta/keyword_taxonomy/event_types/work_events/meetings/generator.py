import json

def generate_work_meetings_json():
    """
    Generate a JSON file with work meeting expressions as commonly spoken.
    Each key is a longer verbal reference to a work meeting, and the value is an object
    containing a description (shorter standardized term) and a priority level.
    """
    meeting_types = {
        # General meetings
        "general business meeting": {"description": "meeting", "priority": 3},
        "meeting with team members": {"description": "team meeting", "priority": 4},
        "meeting with staff": {"description": "staff meeting", "priority": 4},
        "meeting with department": {"description": "department meeting", "priority": 4},
        "meeting with entire company": {"description": "company meeting", "priority": 5},
        "meeting with internal stakeholders": {"description": "internal meeting", "priority": 4},
        "meeting with external parties": {"description": "external meeting", "priority": 5},
        "meeting with clients": {"description": "client meeting", "priority": 5},
        "meeting with vendors": {"description": "vendor meeting", "priority": 3},
        "meeting with business partners": {"description": "partner meeting", "priority": 4},
        "formal professional meeting": {"description": "business meeting", "priority": 3},
        "meeting with project stakeholders": {"description": "stakeholder meeting", "priority": 5},
        
        # Meeting actions
        "participate in a meeting": {"description": "attend", "priority": 3},
        "be present at a meeting": {"description": "attend", "priority": 3},
        "lead or facilitate a meeting": {"description": "run", "priority": 4},
        "organize and lead a meeting": {"description": "host", "priority": 4},
        "direct and guide a meeting": {"description": "lead", "priority": 4},
        "become a participant in a meeting": {"description": "join", "priority": 3},
        "arrange a time for a meeting": {"description": "schedule", "priority": 2},
        "reserve time for a meeting": {"description": "book", "priority": 2},
        "arrange and prepare for a meeting": {"description": "set up", "priority": 3},
        "plan and coordinate a meeting": {"description": "organize", "priority": 3},
        "help a meeting run smoothly": {"description": "facilitate", "priority": 4},
        "preside over a formal meeting": {"description": "chair", "priority": 5},
        "control the flow of a meeting": {"description": "moderate", "priority": 4},
        "change the time of a planned meeting": {"description": "reschedule", "priority": 2},
        "call off a planned meeting": {"description": "cancel", "priority": 2},
        "delay a planned meeting": {"description": "postpone", "priority": 2},
        
        # Conference calls
        "multi-person phone meeting": {"description": "conference call", "priority": 3},
        "participate in a multi-person phone meeting": {"description": "join call", "priority": 3},
        "connect to a multi-person phone meeting": {"description": "dial in", "priority": 3},
        "organize and lead a multi-person phone meeting": {"description": "host call", "priority": 4},
        "arrange a multi-person phone meeting": {"description": "set up call", "priority": 3},
        "connect to a multi-person phone meeting remotely": {"description": "call in", "priority": 3},
        
        # Video meetings
        "meeting via video conferencing": {"description": "video call", "priority": 3},
        "formal meeting via video technology": {"description": "video conference", "priority": 4},
        "meeting conducted through video technology": {"description": "video meeting", "priority": 3},
        "meeting held online rather than in person": {"description": "virtual meeting", "priority": 3},
        "meeting using Zoom video conferencing platform": {"description": "Zoom", "priority": 3},
        "meeting using Microsoft Teams platform": {"description": "Teams", "priority": 3},
        "meeting using Google Meet platform": {"description": "Meet", "priority": 3},
        "meeting using Cisco Webex platform": {"description": "Webex", "priority": 3},
        "participate in a video conference": {"description": "join video", "priority": 3},
        "connect to a video-based meeting": {"description": "join video", "priority": 3},
        "organize and lead an online meeting": {"description": "host video", "priority": 4},
        
        # Presentations
        "formal display of information to an audience": {"description": "presentation", "priority": 4},
        "deliver information to an audience": {"description": "present", "priority": 4},
        "present information formally to a group": {"description": "present", "priority": 4},
        "create and deliver a presentation": {"description": "present", "priority": 4},
        "deliver information to a specific audience": {"description": "present", "priority": 4},
        "perform a formal information delivery": {"description": "present", "priority": 4},
        "presentation to sell an idea or product": {"description": "pitch", "priority": 5},
        "deliver a persuasive presentation": {"description": "pitch", "priority": 5},
        "present a persuasive proposal": {"description": "pitch", "priority": 5},
        "presentation to sell products or services": {"description": "sales pitch", "priority": 5},
        "presentation to potential investors": {"description": "investor pitch", "priority": 5},
        "presentation to potential clients": {"description": "client pitch", "priority": 5},
        
        # Workshops
        "interactive learning or planning session": {"description": "workshop", "priority": 4},
        "lead an interactive learning session": {"description": "run workshop", "priority": 4},
        "facilitate an interactive group session": {"description": "run workshop", "priority": 4},
        "organize and lead a workshop": {"description": "host workshop", "priority": 4},
        "take part in an interactive learning session": {"description": "attend workshop", "priority": 3},
        "be present at an interactive learning session": {"description": "attend workshop", "priority": 3},
        "interactive session focused on skill development": {"description": "training", "priority": 4},
        "interactive session focused on creating plans": {"description": "planning session", "priority": 4},
        "interactive session focused on developing strategy": {"description": "strategy session", "priority": 5},
        
        # Interviews
        "formal meeting to assess a candidate": {"description": "interview", "priority": 5},
        "evaluate a candidate through questioning": {"description": "conduct interview", "priority": 5},
        "participate in an evaluation meeting as a candidate": {"description": "interview", "priority": 5},
        "attend a meeting where one will be evaluated": {"description": "interview", "priority": 5},
        "candidate evaluation conducted by telephone": {"description": "phone interview", "priority": 4},
        "candidate evaluation conducted by video call": {"description": "video interview", "priority": 5},
        "preliminary candidate evaluation": {"description": "screening", "priority": 4},
        "candidate evaluation by multiple interviewers": {"description": "panel interview", "priority": 5},
        "evaluation of multiple candidates simultaneously": {"description": "group interview", "priority": 5},
        "meeting to evaluate a candidate for employment": {"description": "job interview", "priority": 5},
        "meeting to gather career or industry information": {"description": "informational interview", "priority": 3},
        
        # Other professional gatherings
        "meeting focused on generating ideas": {"description": "brainstorm", "priority": 4},
        "collaborative idea generation meeting": {"description": "brainstorm", "priority": 4},
        "participate in idea generation": {"description": "brainstorm", "priority": 4},
        "meeting to develop plans": {"description": "planning", "priority": 4},
        "meeting to develop strategic direction": {"description": "strategy session", "priority": 5},
        "meeting between two individuals": {"description": "one-on-one", "priority": 4},
        "individual meeting between two people": {"description": "1:1", "priority": 4},
        "meet individually with someone": {"description": "one-on-one", "priority": 4},
        "brief alignment meeting": {"description": "sync", "priority": 3},
        "short alignment meeting": {"description": "quick sync", "priority": 2},
        "participate in an alignment meeting": {"description": "sync", "priority": 3},
        "brief status update meeting": {"description": "check-in", "priority": 3},
        "participate in a status update meeting": {"description": "check-in", "priority": 3},
        "meeting to update on progress": {"description": "status meeting", "priority": 3},
        "meeting to review advancement of work": {"description": "progress meeting", "priority": 3},
        "initial meeting to start a project": {"description": "kickoff", "priority": 5},
        "hold an initial project meeting": {"description": "kickoff", "priority": 5},
        "meeting to review completed activities": {"description": "debrief", "priority": 3},
        "participate in a review of completed activities": {"description": "debrief", "priority": 3},
        "meeting to analyze a completed project": {"description": "post-mortem", "priority": 4},
        "meeting to evaluate work": {"description": "review", "priority": 4},
        "meeting with all staff or team members": {"description": "all-hands", "priority": 5},
        "large informational meeting for all employees": {"description": "town hall", "priority": 5},
        
        # Formal meetings
        "formal meeting of board members": {"description": "board meeting", "priority": 5},
        "meeting of a designated committee": {"description": "committee meeting", "priority": 4},
        "meeting of a special group assigned to a specific task": {"description": "task force", "priority": 5},
        "meeting of company executives": {"description": "executive meeting", "priority": 5},
        "meeting of organizational leaders": {"description": "leadership meeting", "priority": 5},
        "yearly formal meeting of shareholders": {"description": "AGM", "priority": 5},
        "annual general meeting of shareholders": {"description": "AGM", "priority": 5},
        "special shareholder meeting": {"description": "EGM", "priority": 5},
        "extraordinary general meeting": {"description": "EGM", "priority": 5}
    }
    
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
        }
    }
    
    return work_meetings_json

def add_transformer_priority_prediction(json_data):
    """
    A placeholder function that would use a transformer model to predict priorities.
    This is where you would integrate a model like BERT, GPT, etc.
    """
    try:
        # This is a placeholder - you would add actual transformer code here
        from transformers import pipeline
        
        # Example: Setup a text classification pipeline
        classifier = pipeline("text-classification", 
                             model="distilbert-base-uncased-finetuned-sst-2-english")
        
        # For each meeting type, predict priority based on description
        for key in json_data["values"]:
            # This is just a placeholder - in reality, you'd use a model trained for priority prediction
            # Here we're just using sentiment as a dummy example (not actually useful for priority)
            result = classifier(key)
            
            # This is where you'd map the model output to a priority score
            # For now, we'll keep the manually assigned priorities
            print(f"Would predict priority for: {key}")
            
        print("Transformer-based priority prediction complete (simulated)")
        
    except ImportError:
        print("Note: Transformers library not available. Using preset priorities.")
        print("To use transformer-based prediction, install with: pip install transformers")
    
    return json_data

# Generate the JSON data
json_data = generate_work_meetings_json()

# Uncomment the next line to implement transformer-based priority prediction
# json_data = add_transformer_priority_prediction(json_data)

# Write to a file
with open('data/english/meta/keyword_taxonomy/event_types/work_events/meetings/vocabulary/work_meetings.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

print(f"Generated {len(json_data['values'])} work meeting expressions and saved to work_meetings.json")

# Print some examples
print("\nSample entries:")
sample_keys = ["multi-person phone meeting", "organize and lead a workshop", "deliver information to an audience", 
               "meeting between two individuals", "be present at a meeting"]
for key in sample_keys:
    if key in json_data["values"]:
        print(f'"{key}": {json.dumps(json_data["values"][key], indent=2)}')