import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def predict(sentence, model_path="./task_parser_final"):
    """Load model and make a prediction for a given sentence."""
    # Recreate the tokenizer the same way as during training
    base_tokenizer_name = "t5-small"  # This was the base model used
    tokenizer = T5Tokenizer.from_pretrained(base_tokenizer_name, use_fast=False)
    
    # Add the same special tokens you used during training
    special_tokens = ["[time]", "[/time]", "[task]", "[/task]", "[eos]", 
                     "[minute]", "[hour]", "[day]", "[week]", "[month]", "[year]",
                     "[period]", "[frequency]", "[duration]", "[deadline]", 
                     "[description]", "[category]", "[event_type]", 
                     "[priority]", "[importance]", "[urgency]", "[is_recurring]",
                     "[date]", "[day_of_week]"]
    
    special_tokens_dict = {"additional_special_tokens": special_tokens}
    tokenizer.add_special_tokens(special_tokens_dict)
    
    # Load the model
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    
    # Make sure the model is using the same size embeddings as the tokenizer
    if model.config.vocab_size != len(tokenizer):
        model.resize_token_embeddings(len(tokenizer))
    
    # Move model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    # Tokenize the input sentence
    inputs = tokenizer(sentence, return_tensors="pt").to(device)
    
    # Generate output
    with torch.no_grad():
        output_ids = model.generate(
            inputs["input_ids"],
            max_length=128,
            num_beams=4,
            early_stopping=True
        )
    
    # Decode the output
    prediction = tokenizer.decode(output_ids[0], skip_special_tokens=False)
    
    return prediction

# Example usage
if __name__ == "__main__":
    test_sentence = "I want to take some rest tommorow"
    result = predict(test_sentence)
    print(f"Input: {test_sentence}")
    print(f"Output: {result}")