import os
import json

def create_taxonomy_directories(taxonomy_file, output_dir):
    """
    Create a directory structure based on the taxonomy file, with a 'vocabulary' folder
    inside each leaf category.
    
    Args:
        taxonomy_file (str): Path to the taxonomy JSON file
        output_dir (str): Base directory for the taxonomy structure
    """
    # Load taxonomy file
    try:
        with open(taxonomy_file, 'r') as f:
            taxonomy_data = json.load(f)
        print(f"Successfully loaded taxonomy from {taxonomy_file}")
    except Exception as e:
        print(f"Error loading taxonomy file: {e}")
        return
    
    # Create the base directory if it doesn't exist
    base_dir = os.path.join(output_dir, "keyword_taxonomy")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")
    
    # Process the taxonomy structure
    process_taxonomy(taxonomy_data, base_dir)
    
    print("\nDirectory structure created successfully!")

def process_taxonomy(data, current_path):
    """
    Recursively process the taxonomy and create category directories.
    
    Args:
        data (dict): Current level of taxonomy data
        current_path (str): Current directory path
    """
    if isinstance(data, dict):
        # Check if this is a leaf category (has description, examples, vocab)
        is_leaf = any(key in ["description", "examples", "vocab"] for key in data.keys())
        
        # Process all subcategories
        has_subcategories = False
        for key, value in data.items():
            # Skip metadata keys
            if key in ["description", "examples", "vocab"]:
                continue
                
            # Create directory for this category
            if isinstance(value, dict):
                has_subcategories = True
                category_path = os.path.join(current_path, key)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                    print(f"Created directory: {category_path}")
                
                # Recursively process subcategories
                process_taxonomy(value, category_path)
        
        # If this is a leaf category (no subcategories) or has vocab key, create a vocabulary folder
        if (is_leaf and not has_subcategories) or "vocab" in data:
            vocab_dir = os.path.join(current_path, "vocabulary")
            if not os.path.exists(vocab_dir):
                os.makedirs(vocab_dir)
                print(f"Created vocabulary directory: {vocab_dir}")

def main():
    create_taxonomy_directories("data/english/meta/keyword_taxonomy.json", "data/english/meta")

if __name__ == "__main__":
    main()