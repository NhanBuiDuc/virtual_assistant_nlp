import argparse
import torch
from transformers import BertTokenizer, BertForMaskedLM, T5Tokenizer, T5ForConditionalGeneration
import numpy as np
import re
from itertools import permutations

class KeywordConnector:
    def __init__(self, bert_model="bert-base-uncased", t5_model="t5-large"):
        """Initialize the models for connecting keywords."""
        # BERT for connector words
        print("Loading BERT model...")
        self.bert_tokenizer = BertTokenizer.from_pretrained(bert_model)
        self.bert_model = BertForMaskedLM.from_pretrained(bert_model)
        self.bert_model.eval()  # Set to evaluation mode
        
        # T5 for full sentence generation (using larger model for better results)
        print("Loading T5 model...")
        self.t5_tokenizer = T5Tokenizer.from_pretrained(t5_model)
        self.t5_model = T5ForConditionalGeneration.from_pretrained(t5_model)
        self.t5_model.eval()  # Set to evaluation mode
        
        # Common sentence starters for different contexts
        self.sentence_starters = {
            'reminder': ['Remind me to', 'Don\'t forget to', 'Remember to', 'I need to remember to'],
            'meeting': ['I have a meeting with', 'There\'s a meeting with', 'Meeting scheduled with', 'We\'re meeting with'],
            'appointment': ['I have an appointment for', 'There\'s an appointment for', 'Appointment scheduled for'],
            'general': ['I need to', 'Remember to', 'Don\'t forget to', 'Make sure to']
        }
        
        # Common contextual templates for different situations
        self.contextual_templates = {
            'meeting': [
                "{person} at {location} on {date} at {time}",
                "meeting with {person} at {location} {date} {time}",
                "{date} {time} meeting with {person} at {location}"
            ],
            'appointment': [
                "{purpose} on {date} at {time}",
                "{purpose} appointment on {date} at {time}",
                "appointment for {purpose} on {date} at {time}"
            ],
            'reminder': [
                "{action} {object} at {location} on {date}",
                "{action} {object} on {date} at {time}",
                "{action} {object} at {location} {date} {time}"
            ]
        }
    
    def classify_intent(self, keywords):
        """Classify the intent of the keywords to select appropriate sentence starter."""
        keywords_lower = ' '.join([k.strip().lower() for k in keywords.split(',')])
        
        if re.search(r'\bremind|\breminder', keywords_lower):
            return 'reminder'
        elif re.search(r'\bmeeting|\bmeet\b', keywords_lower):
            return 'meeting'
        elif re.search(r'\bappointment|\bdoctor|\bdental|\bcheckup', keywords_lower):
            return 'appointment'
        else:
            return 'general'
    
    def predict_best_connector(self, before_context, after_context, top_k=10):
        """Predict the best connector word between two context pieces using BERT."""
        # Special cases to handle common patterns
        before_lower = before_context.lower()
        after_lower = after_context.lower()
        
        # Handle specific cases where no connector is needed
        if before_lower.endswith(('to', 'tomorrow', 'weekend', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')):
            return ""
            
        # Handle "Remember to to" duplication
        if (before_lower.endswith(('remember to', 'forget to', 'need to')) and 
            ('call' in after_lower or 'bring' in after_lower or 'pick' in after_lower or 'go' in after_lower)):
            return ""
            
        # Handle time expressions
        if re.search(r'\d+\s*(?:am|pm|:)', after_lower) or any(t in after_lower for t in ['morning', 'afternoon', 'evening']):
            return "at"
            
        # Handle dates
        if any(day in after_lower for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
            return "on"
            
        # Handle locations
        if any(place in after_lower for place in ['mall', 'shop', 'store', 'office', 'market', 'hospital']):
            return "at the"
        
        # Handle people in different contexts
        if any(name in after_lower for name in ['john', 'mary', 'sarah', 'mom', 'dad']):
            if 'meeting' in before_lower or 'meet' in before_lower:
                return "with"
            elif 'party' in before_lower:
                return "for"
            elif 'call' in before_lower:
                return ""
        
        # Create a masked sentence with multiple masks for better context awareness
        masked_text = f"{before_context} [MASK] [MASK] {after_context}"
        
        # Tokenize
        inputs = self.bert_tokenizer(masked_text, return_tensors="pt")
        mask_token_indices = torch.where(inputs["input_ids"][0] == self.bert_tokenizer.mask_token_id)[0]
        
        # Forward pass
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
        
        # Get predictions for first mask
        logits = outputs.logits
        first_mask_logits = logits[0, mask_token_indices[0], :]
        
        # Get top k predicted tokens
        top_k_tokens = torch.topk(first_mask_logits, top_k, dim=0).indices.tolist()
        
        # Convert to words
        predicted_tokens = [self.bert_tokenizer.decode([token]) for token in top_k_tokens]
        
        # Filter out punctuation and special tokens
        predicted_tokens = [token for token in predicted_tokens if re.match(r'^[a-zA-Z]+$', token)]
        
        # Define appropriate connectors for different contexts
        valid_connectors = {
            "time": ["at"],
            "date": ["on"],
            "location": ["at", "to", "in"],
            "person": ["with", "for", "to"],
            "object": ["for", "with", "about"],
            "action": ["to"]
        }
        
        # Determine entity type of after_context
        entity_type = "object"  # Default
        if re.search(r'\d+\s*(?:am|pm|:)', after_lower):
            entity_type = "time"
        elif any(day in after_lower for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
            entity_type = "date"
        elif any(place in after_lower for place in ['mall', 'shop', 'store', 'office', 'market']):
            entity_type = "location"
        elif any(name in after_lower for name in ['john', 'mary', 'sarah', 'mom', 'dad']):
            entity_type = "person"
        
        # Check for appropriate connector based on entity type
        appropriate_connectors = valid_connectors.get(entity_type, ["to", "for", "with"])
        
        for token in predicted_tokens:
            if token in appropriate_connectors:
                return token
        
        # Specific cases where an article is needed
        if entity_type == "location" and "the" not in after_lower:
            return "at the"
            
        # When nothing appropriate is found, return based on entity type
        if entity_type == "time":
            return "at"
        elif entity_type == "date":
            return "on"
        elif entity_type == "location":
            return "at"
        elif entity_type == "person":
            return "with"
        else:
            return ""  # Sometimes no connector is better
    
    def infer_entity_types(self, keywords_list):
        """Infer the entity type for each keyword using contextual clues."""
        entity_types = {}
        
        for keyword in keywords_list:
            keyword_lower = keyword.lower()
            
            # Check for time expressions
            if re.search(r'\d+\s*(?:am|pm|:)', keyword_lower) or any(t in keyword_lower for t in ['morning', 'afternoon', 'evening', 'tonight', 'tomorrow', 'yesterday']):
                entity_types[keyword] = 'time'
            
            # Check for dates
            elif any(month in keyword_lower for month in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']) or \
                 any(day in keyword_lower for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']) or \
                 re.search(r'\d+(?:st|nd|rd|th)', keyword_lower):
                entity_types[keyword] = 'date'
            
            # Check for locations
            elif any(place in keyword_lower for place in ['mall', 'shop', 'store', 'office', 'home', 'hospital', 'clinic', 'restaurant', 'cafe', 'park', 'school', 'university', 'library', 'market']):
                entity_types[keyword] = 'location'
            
            # Check for people
            elif any(name in keyword_lower for name in ['john', 'mary', 'sarah', 'mom', 'dad', 'sister', 'brother', 'wife', 'husband', 'doctor', 'dr', 'professor', 'mr', 'mrs', 'ms']):
                entity_types[keyword] = 'person'
            
            # Check for verbs/actions
            elif any(action in keyword_lower for action in ['call', 'pick up', 'get', 'buy', 'meet', 'remind', 'talk', 'discuss', 'bring', 'take', 'go']):
                entity_types[keyword] = 'action'
            
            # Check for event types
            elif any(event in keyword_lower for event in ['meeting', 'appointment', 'party', 'celebration', 'event', 'conference', 'doctor appointment', 'checkup']):
                entity_types[keyword] = 'event'
            
            # Check for objects
            elif any(obj in keyword_lower for obj in ['groceries', 'food', 'gift', 'present', 'medication', 'medicine', 'book', 'ticket', 'reservation']):
                entity_types[keyword] = 'object'
            
            # Default to object if we can't determine
            else:
                entity_types[keyword] = 'object'
        
        return entity_types
    
    def find_optimal_order(self, keywords_list):
        """Find the optimal order of keywords for a fluent sentence using entity types."""
        # Infer entity types
        entity_types = self.infer_entity_types(keywords_list)
        
        # Define priority patterns for different types of sentences
        patterns = [
            # For events: action, person, event, location, date, time
            ['action', 'person', 'event', 'object', 'location', 'date', 'time'],
            
            # For appointments: event, action, date, time, person, location
            ['event', 'action', 'date', 'time', 'person', 'location', 'object'],
            
            # For reminders: action, object, location, date, time
            ['action', 'object', 'location', 'date', 'time', 'person']
        ]
        
        # Track which entity types we have
        available_types = set(entity_types.values())
        
        # Find best pattern based on matching entity types
        best_pattern = None
        max_match = -1
        
        for pattern in patterns:
            pattern_set = set(pattern)
            matching_types = len(pattern_set.intersection(available_types))
            if matching_types > max_match:
                max_match = matching_types
                best_pattern = pattern
        
        # Special cases for better ordering
        if 'event' in available_types and 'event' in best_pattern:
            # For appointments, put appointment-related keywords first
            for keyword in keywords_list:
                if entity_types.get(keyword) == 'event' and 'appointment' in keyword.lower():
                    keywords_list = [keyword] + [k for k in keywords_list if k != keyword]
                    break
        
        # Organize keywords according to pattern
        ordered_keywords = []
        for entity_type in best_pattern:
            # Add all keywords of this type in their original order
            for keyword in keywords_list:
                if keyword in entity_types and entity_types[keyword] == entity_type and keyword not in ordered_keywords:
                    ordered_keywords.append(keyword)
        
        # Add any keywords that didn't fit the pattern
        for keyword in keywords_list:
            if keyword not in ordered_keywords:
                ordered_keywords.append(keyword)
        
        return ordered_keywords
        
    def post_process_sentence(self, sentence):
        """Post-process the generated sentence to fix common grammatical issues."""
        # Remove the T5 prompt text if it appears
        if sentence.lower().startswith("convert keywords to sentence:"):
            sentence = sentence[len("convert keywords to sentence:"):].strip()
        
        # Fix duplicate words (e.g., "to to")
        sentence = re.sub(r'\b(\w+)\s+\1\b', r'\1', sentence)
        
        # Fix "Remember to Remind me" patterns
        sentence = re.sub(r'(Remember|Don\'t forget|I need) to (Remind|Remember)', r'\1 to', sentence)
        
        # Fix "Remember to to" patterns
        sentence = re.sub(r'(emember to|orget to|eed to)\s+to', r'\1', sentence)
        
        # Fix article issues with specific nouns
        sentence = re.sub(r'at\s+(market|mall|store|office|shop|hospital)', r'at the \1', sentence)
        sentence = re.sub(r'to\s+(market|mall|store|office|shop|hospital)', r'to the \1', sentence)
        
        # Add possessive pronouns for birthday party
        sentence = re.sub(r'(Sarah|John|Mary|mom|dad)\'s?\s+birthday party', r'\1\'s birthday party', sentence)
        sentence = re.sub(r'at\s+birthday party', r'at the birthday party', sentence)
        
        # Fix time prepositions
        sentence = re.sub(r'for\s+(\d+\s*(?:am|pm))', r'at \1', sentence)
        sentence = re.sub(r'in\s+(\d+\s*(?:am|pm))', r'at \1', sentence)
        sentence = re.sub(r'for\s+(tomorrow|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)', r'on \1', sentence)
        
        # Fix "on weekend" to "on the weekend"
        sentence = re.sub(r'on\s+weekend', r'on the weekend', sentence)
        
        # Fix double prepositions
        sentence = re.sub(r'(at|in|on|to|for|with)\s+(at|in|on|to|for|with)', r'\1', sentence)
        
        # Fix redundant appointment mentions
        sentence = re.sub(r'appointment\s+for\s+doctor\s+appointment', r'doctor appointment', sentence)
        sentence = re.sub(r'appointment\s+for\s+appointment', r'appointment', sentence)
        
        # Fix redundant meeting mentions
        sentence = re.sub(r'meeting\s+with\s+meeting', r'meeting', sentence)
        
        # Fix January morning 7 pm issue
        sentence = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(morning|afternoon|evening)', r'\1', sentence)
        
        # Fix morning X pm issue
        sentence = re.sub(r'(morning)\s+(\d+\s*(?:pm))', r'\2', sentence)
        sentence = re.sub(r'(evening)\s+(\d+\s*(?:am))', r'\2', sentence)
        
        # Ensure single spacing
        sentence = re.sub(r'\s+', ' ', sentence)
        
        return sentence

    def generate_with_t5(self, keywords_list):
        """Generate a complete sentence using T5 model."""
        # Format input for T5
        input_text = "convert keywords to sentence: " + ", ".join(keywords_list)
        
        # Tokenize input
        input_ids = self.t5_tokenizer(input_text, return_tensors="pt").input_ids
        
        # Generate with more diversity to try different phrasings
        with torch.no_grad():
            outputs = self.t5_model.generate(
                input_ids,
                max_length=100,
                num_beams=10,
                do_sample=True,
                top_p=0.95,
                temperature=0.7,
                no_repeat_ngram_size=2,
                early_stopping=True
            )
        
        # Decode and return
        sentence = self.t5_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Remove the prompt if it's included in the output
        if sentence.lower().startswith("convert keywords to sentence:"):
            sentence = sentence[len("convert keywords to sentence:"):].strip()
        
        # Ensure proper capitalization and punctuation
        if not sentence.endswith(('.', '!', '?')):
            sentence += '.'
        
        # Capitalize first letter
        sentence = sentence[0].upper() + sentence[1:]
        
        # Apply post-processing
        sentence = self.post_process_sentence(sentence)
        
        return sentence
    
    def fill_template(self, template, entity_dict):
        """Fill a template with entities from the keywords."""
        # Replace placeholders with actual values
        filled = template
        for entity_type, value in entity_dict.items():
            if value:
                filled = filled.replace(f"{{{entity_type}}}", value)
        
        # Remove any remaining placeholders
        filled = re.sub(r'\{[^}]+\}', '', filled)
        
        # Clean up spaces
        filled = re.sub(r'\s+', ' ', filled).strip()
        
        return filled
    
    def generate_sentence(self, keywords):
        """Generate a complete sentence from keywords using a hybrid approach."""
        keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
       
        # Otherwise try template-based approach
        intent = self.classify_intent(keywords)
        entity_types = self.infer_entity_types(keywords_list)
        
        # Select a sentence starter
        sentence_starter = np.random.choice(self.sentence_starters[intent])
        
        # Prepare for template or fallback approach
        # Find optimal keyword order
        ordered_keywords = self.find_optimal_order(keywords_list)
        
        # Prepare a single sentence with multiple context windows
        full_context = sentence_starter
        used_keywords = []
        
        for i, keyword in enumerate(ordered_keywords):
            # Skip keywords already in the starter or already used
            if keyword.lower() in full_context.lower() or keyword in used_keywords:
                continue
            
            # Predict connector with full context
            connector = self.predict_best_connector(full_context, keyword)
            
            # Add the connector and keyword
            if connector:
                full_context += f" {connector} {keyword}"
            else:
                full_context += f" {keyword}"
            
            used_keywords.append(keyword)
        
        # Clean up and post-process the sentence
        sentence = re.sub(r'\s+', ' ', full_context).strip()
        
        # Ensure it ends with a period
        if not sentence.endswith(('.', '!', '?')):
            sentence += '.'
        
        # Apply post-processing to fix common issues
        sentence = self.post_process_sentence(sentence)
        
        return sentence

def main():
    parser = argparse.ArgumentParser(description="Generate complete sentences from keywords using neural language models")
    parser.add_argument("--keywords", type=str, default="Remind me to, go to shopping mall, 7 pm, January, morning",
                        help="Comma-separated keywords to convert into a sentence")
    args = parser.parse_args()
    
    # Create the connector model
    connector = KeywordConnector()
    
    print(f"Input keywords: {args.keywords}")
    sentence = connector.generate_sentence(args.keywords)
    print(f"Generated sentence: {sentence}")
    
    # Additional examples
    print("\nAdditional examples:")
    example_keywords = [
        "meeting, John, coffee shop, tomorrow, 3 pm",
        "birthday party, Sarah, Saturday, bring gift",
        "doctor appointment, checkup, Tuesday, 10 am",
        "pick up, groceries, weekend, market",
        "call, mom, vacation plans, Sunday afternoon"
    ]
    
    for example in example_keywords:
        print(f"Keywords: {example}")
        sentence = connector.generate_sentence(example)
        print(f"Generated sentence: {sentence}")
        print("---")

if __name__ == "__main__":
    main()
    