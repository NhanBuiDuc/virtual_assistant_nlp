import json
import random
import time
from tqdm import tqdm
from transformers import pipeline, set_seed
import torch

# Set seed for reproducibility
set_seed(42)
random.seed(42)

# Define batch size for processing
BATCH_SIZE = 32  # Process this many examples at once
MAX_COMBINATIONS = None  # Set to a number for testing, None for all combinations

def load_combinations(file_path='combinations.json', limit=None):
    """Load combinations from file with optional limit for testing"""
    print(f"Loading combinations from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    combinations = data["combinations"]
    if limit:
        combinations = combinations[:limit]
        print(f"Limited to {limit} combinations for testing")
    else:
        print(f"Loaded {len(combinations)} combinations")
    
    return data, combinations

def initialize_generator():
    """Initialize the text generation pipeline with optimizations"""
    print("Initializing transformer model...")
    
    # Check if GPU is available
    device = 'cuda:3'
    
    # Initialize with optimized settings
    generator = pipeline(
        'text-generation', 
        model='gpt2-medium',
        device=device,
        framework="pt"  # Use PyTorch
    )
    
    return generator

def generate_coherent_sentence(element_list, generator):
    """Generate a coherent sentence using a transformer model"""
    # Create a prompt that encourages the model to use all elements
    prompt = f"Create a single sentence using these phrases: {', '.join(element_list)}. Sentence:"
    
    # Generate text using the model
    result = generator(
        prompt, 
        max_length=100, 
        num_return_sequences=1, 
        temperature=0.7,
        top_p=0.9, 
        do_sample=True,
        return_full_text=False  # Only return the newly generated text
    )
    
    # Extract the generated text
    generated_text = result[0]["generated_text"]
    
    # Try to extract just the sentence
    try:
        # First try to get text after "Sentence:"
        if "Sentence:" in prompt + generated_text:
            sentence = (prompt + generated_text).split("Sentence:")[1].strip()
        else:
            sentence = generated_text.strip()
        
        # Clean up the sentence
        if "." in sentence:
            sentence = sentence.split(".")[0] + "."
        if sentence.startswith('"') and sentence.endswith('"'):
            sentence = sentence[1:-1]
    except:
        # Fallback if extraction fails
        sentence = manual_sentence_construction(element_list)
    
    # Verify all elements are included, fall back if not
    if not all(element.lower() in sentence.lower() for element in element_list):
        sentence = manual_sentence_construction(element_list)
    
    return sentence

def manual_sentence_construction(elements):
    """Fallback function to manually construct a sentence"""
    task = elements[0]
    time_parts = elements[1:]
    
    if time_parts:
        time_phrase = " ".join(time_parts)
        sentence = f"I need to {task} {time_phrase}."
    else:
        sentence = f"I need to {task}."
    
    return sentence

def batch_process_combinations(combinations, generator, batch_size=32):
    """Process combinations in batches for efficiency"""
    total = len(combinations)
    processed = []
    
    # Create a progress bar
    with tqdm(total=total, desc="Generating sentences") as pbar:
        for i in range(0, total, batch_size):
            # Get the current batch
            batch = combinations[i:min(i+batch_size, total)]
            
            # Process each item in the batch
            for combination in batch:
                elements = combination["combination"]
                sentence = generate_coherent_sentence(elements, generator)
                combination["sentence"] = sentence
                processed.append(combination)
                pbar.update(1)
            
            # Optional: Add a small delay to prevent GPU overheating on long runs
            # time.sleep(0.1)
    
    return processed

def main():
    start_time = time.time()
    
    # Load combinations
    data, combinations = load_combinations(limit=MAX_COMBINATIONS)
    
    # Initialize the transformer model
    generator = initialize_generator()
    
    # Process combinations in batches
    processed_combinations = batch_process_combinations(
        combinations, generator, batch_size=BATCH_SIZE
    )
    
    # Update the data object
    data["combinations"] = processed_combinations
    
    # Save the updated data
    output_file = 'combinations_with_sentences.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    # Print some examples
    print("\nSample generated sentences:")
    for i in range(min(5, len(processed_combinations))):
        combo = processed_combinations[i]
        print(f"ID {combo['id']}: {combo['sentence']}")
        print(f"  Original elements: {', '.join(combo['combination'])}\n")
    
    # Report total processing time
    elapsed_time = time.time() - start_time
    print(f"Total processing time: {elapsed_time:.2f} seconds")
    print(f"Processed {len(processed_combinations)} combinations")
    print(f"Average time per combination: {elapsed_time/len(processed_combinations):.2f} seconds")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()