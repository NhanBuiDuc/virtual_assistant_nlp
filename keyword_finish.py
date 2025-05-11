import json
from transformers import pipeline, set_seed
import random

# Set seed for reproducibility
set_seed(42)
random.seed(42)

# Load the combinations file
with open('combinations.json', 'r', encoding='utf-8') as f:
    combinations_data = json.load(f)

# Initialize the text generation pipeline using a pre-trained model
generator = pipeline('text-generation', model='gpt2-medium')

def generate_coherent_sentence(combination_elements):
    """
    Generate a coherent sentence that incorporates all elements in the combination.
    Uses a pre-trained model to ensure fluency and naturalness.
    """
    # Create a prompt that encourages the model to use all elements in a single sentence
    prompt = f"Create a single sentence using these phrases: {', '.join(combination_elements)}. Sentence:"
    
    # Generate text using the model
    result = generator(prompt, max_length=100, num_return_sequences=1, temperature=0.7, 
                      top_p=0.9, do_sample=True)
    
    # Extract the generated text and clean it up
    generated_text = result[0]['generated_text']
    
    # Extract just the sentence part (after "Sentence:")
    try:
        sentence = generated_text.split("Sentence:")[1].strip()
        # Remove any extra sentences if the model generated more than one
        if "." in sentence:
            sentence = sentence.split(".")[0] + "."
    except:
        # Fallback if the splitting didn't work as expected
        sentence = manual_sentence_construction(combination_elements)
    
    # Make sure all elements are included
    if not all(element.lower() in sentence.lower() for element in combination_elements):
        sentence = manual_sentence_construction(combination_elements)
        
    return sentence

def manual_sentence_construction(elements):
    """Fallback function to manually construct a sentence if the model fails."""
    # For task/event elements (usually the first one)
    task = elements[0]
    
    # Initialize sentence parts
    time_parts = []
    
    # Add remaining elements as time/date/deadline specifications
    for element in elements[1:]:
        time_parts.append(element)
    
    # Construct the sentence
    if time_parts:
        time_phrase = " ".join(time_parts)
        sentence = f"I need to {task} {time_phrase}."
    else:
        sentence = f"I need to {task}."
    
    return sentence

# Process each combination and add a sentence
for combination in combinations_data["combinations"]:
    elements = combination["combination"]
    sentence = generate_coherent_sentence(elements)
    combination["sentence"] = sentence

# Save the updated data
with open('combinations_with_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(combinations_data, f, indent=2)

# Print some examples of the generated sentences
print("Sample generated sentences:")
for i in range(min(5, len(combinations_data["combinations"]))):
    combo = combinations_data["combinations"][i]
    print(f"ID {combo['id']}: {combo['sentence']}")
    print(f"  Original elements: {', '.join(combo['combination'])}\n")