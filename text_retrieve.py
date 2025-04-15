import json
import spacy
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define noun categories dictionary
noun_categories = {
    "Common Nouns": [
        "assignment", "application", "report", "presentation", "contract",
        "task", "project", "document", "review", "analysis", "work",
        "meeting", "call", "email", "message", "notification", "reminder",
        "deadline", "timeframe", "schedule"
    ],
    "Proper Nouns": [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday", "January", "February", "March",
        "April", "May", "June", "July", "August", "September",
        "October", "November", "December"
    ],
    "Countable Nouns": [
        "assignment", "application", "report", "presentation", "contract",
        "task", "project", "document", "review", "hour", "day", "week",
        "month", "meeting", "call", "email", "message"
    ],
    "Uncountable Nouns": [
        "work", "information", "progress", "content", "feedback",
        "time", "research", "knowledge"
    ],
    "Abstract Nouns": [
        "deadline", "progress", "completion", "success", "failure",
        "importance", "priority", "urgency", "quality", "efficiency"
    ],
    "Concrete Nouns": [
        "document", "report", "application", "contract", "presentation",
        "computer", "phone", "paper", "file", "folder", "office"
    ],
    "Collective Nouns": [
        "team", "group", "staff", "committee", "department", "board",
        "faculty", "management", "personnel", "workforce"
    ]
}

# Function to save the dictionary as a JSON file
def save_noun_dictionary(filename="noun_categories.json"):
    with open(filename, 'w') as f:
        json.dump(noun_categories, f, indent=4)
    print(f"Dictionary saved to {filename}")

# Function to load the dictionary from a JSON file
def load_noun_dictionary(filename="noun_categories.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found. Using default dictionary.")
        return noun_categories

# Function to categorize a noun into its types
def categorize_noun(noun, categories_dict=noun_categories):
    noun_lower = noun.lower()
    categories = []
    
    for category, words in categories_dict.items():
        if noun in words or noun_lower in [w.lower() for w in words]:
            categories.append(category)
    
    return categories

# Function to extract task-related nouns from a sentence
def extract_task_nouns(sentence):
    doc = nlp(sentence)
    
    # Dictionary to store extracted nouns and their categories
    extracted_nouns = {}
    
    # Extract nouns and categorize them
    for token in doc:
        # Check if token is a noun
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            # Get the categories for this noun
            noun_categories = categorize_noun(token.text)
            
            # If the noun belongs to at least one category, add it to the result
            if noun_categories:
                extracted_nouns[token.text] = {
                    "categories": noun_categories,
                    "position": token.i,
                    "is_subject": any(token.dep_ == dep for dep in ["nsubj", "nsubjpass"]),
                    "is_object": any(token.dep_ == dep for dep in ["dobj", "pobj"])
                }
                
    return extracted_nouns

# Function to analyze task deadlines in a sentence
def analyze_task_deadline(sentence):
    doc = nlp(sentence)
    
    # Look for time-related entities
    deadline_info = {
        "task_nouns": [],
        "deadline": None,
        "specific_time": None
    }
    
    # Extract task nouns
    task_nouns = extract_task_nouns(sentence)
    deadline_info["task_nouns"] = list(task_nouns.keys())
    
    # Look for time patterns
    time_pattern = re.compile(r'\d{1,2}(?::\d{2})?\s*(?:AM|PM|am|pm)?', re.IGNORECASE)
    time_matches = time_pattern.findall(sentence)
    if time_matches:
        deadline_info["specific_time"] = time_matches[0]
    
    # Look for deadline indicators
    for token in doc:
        if token.text.lower() in ["by", "before", "until"]:
            deadline_phrase = []
            # Get the tokens that follow the deadline indicator
            for t in token.rights:
                deadline_phrase.append(t.text)
                
            if deadline_phrase:
                deadline_info["deadline"] = " ".join(deadline_phrase)
    
    return deadline_info

# Example usage
if __name__ == "__main__":
    # Save the dictionary to a JSON file
    save_noun_dictionary()
    
    # Example sentences
    task_sentences = [
        "I must complete this assignment by Friday",
        "I must submit this application by noon",
        "I must finish this report by tomorrow",
        "I must deliver this presentation by 3 PM",
        "I must review this contract by end of day"
    ]
    
    print("ANALYSIS OF TASK SENTENCES:\n")
    
    for sentence in task_sentences:
        print(f"Sentence: {sentence}")
        
        # Extract task nouns
        nouns = extract_task_nouns(sentence)
        print("Task-related nouns:")
        for noun, details in nouns.items():
            print(f"  - {noun}: {details['categories']}")
        
        # Analyze deadline
        deadline_info = analyze_task_deadline(sentence)
        print(f"Deadline: {deadline_info['deadline']}")
        if deadline_info['specific_time']:
            print(f"Specific time: {deadline_info['specific_time']}")
        
        print()