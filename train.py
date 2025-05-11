import json
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer
from sklearn.model_selection import train_test_split
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"  # or "1" for the second GPU, etc.

# Step 1: Load the JSON files
def load_data(combinations_file, labels_file):
    """Load and merge the combinations and labels JSON files."""
    with open(combinations_file, 'r', encoding='utf-8') as f:
        combinations_data = json.load(f)
    
    with open(labels_file, 'r', encoding='utf-8') as f:
        labels_data = json.load(f)
    
    # Create a dictionary to map IDs to labels
    id_to_label = {item["id"]: item["label"] for item in labels_data["labels"]}
    
    # Merge the data
    merged_data = []
    for combo in combinations_data["combinations"]:
        if "sentence" in combo and combo["id"] in id_to_label:
            merged_data.append({
                "id": combo["id"],
                "sentence": combo["sentence"],
                "combination": combo["combination"],
                "label": id_to_label[combo["id"]]
            })
    
    return merged_data

# Step 2: Transform labels into special token format
def transform_label_to_tokens(label):
    """Transform a structured label into a special token format."""
    tokens = []
    
    # Time tokens
    tokens.append("[time]")
    time_data = label["time"]
    for time_key in ["minute", "hour", "day", "week", "month", "year"]:
        if time_key in time_data and time_data[time_key] is not None:
            tokens.append(f"[{time_key}]{time_data[time_key]}")
    
    # Period
    if "period" in time_data and time_data["period"]:
        tokens.append(f"[period]{time_data['period']}")
    
    # Frequency
    if "frequency" in time_data and time_data["frequency"]:
        tokens.append(f"[frequency]{time_data['frequency']}")
    
    # Duration
    if "duration" in time_data and time_data["duration"]:
        tokens.append(f"[duration]{time_data['duration']}")
    
    # Deadline
    if "deadline" in time_data and time_data["deadline"]:
        tokens.append(f"[deadline]{time_data['deadline']}")
    
    # Special date information
    if "date" in time_data and time_data["date"]:
        tokens.append(f"[date]{time_data['date']}")
    
    if "day_of_week" in time_data and time_data["day_of_week"]:
        tokens.append(f"[day_of_week]{time_data['day_of_week']}")
    
    tokens.append("[/time]")
    
    # Task tokens
    tokens.append("[task]")
    task_data = label["task"]
    
    if "description" in task_data and task_data["description"]:
        tokens.append(f"[description]{task_data['description']}")
    
    if "category" in task_data and task_data["category"]:
        tokens.append(f"[category]{task_data['category']}")
    
    if "event_type" in task_data and task_data["event_type"]:
        tokens.append(f"[event_type]{task_data['event_type']}")
    
    # Detail tokens
    detail_data = label["detail"]
    
    if "priority" in detail_data and detail_data["priority"]:
        tokens.append(f"[priority]{detail_data['priority']}")
    
    if "importance" in detail_data and detail_data["importance"]:
        tokens.append(f"[importance]{detail_data['importance']}")
    
    if "urgency" in detail_data and detail_data["urgency"]:
        tokens.append(f"[urgency]{detail_data['urgency']}")
    
    if "is_recurring" in detail_data and detail_data["is_recurring"]:
        tokens.append(f"[is_recurring]{str(detail_data['is_recurring']).lower()}")
    
    tokens.append("[/task]")
    tokens.append("[eos]")
    
    return " ".join(tokens)

# Custom dataset class for sequence-to-sequence tasks
class TaskSeq2SeqDataset(Dataset):
    def __init__(self, sentences, token_labels, tokenizer, max_input_length=64, max_target_length=128):
        # Reduced max lengths to save memory
        self.sentences = sentences
        self.token_labels = token_labels
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
        self.max_target_length = max_target_length
    
    def __len__(self):
        return len(self.sentences)
    
    def __getitem__(self, idx):
        # Process input
        inputs = self.tokenizer.encode_plus(
            self.sentences[idx],
            max_length=self.max_input_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        
        # Process target (as a simple encoder, not using as_target_tokenizer())
        with torch.no_grad():
            target_encoding = self.tokenizer.encode_plus(
                self.token_labels[idx],
                max_length=self.max_target_length,
                padding="max_length",
                truncation=True,
                return_tensors="pt"
            )
            
            # Get the input IDs and create attention mask
            labels = target_encoding["input_ids"].squeeze(0)
            
            # Replace padding token id's with -100 so they are ignored in the loss
            labels[labels == self.tokenizer.pad_token_id] = -100
        
        return {
            "input_ids": inputs["input_ids"].squeeze(0),
            "attention_mask": inputs["attention_mask"].squeeze(0),
            "labels": labels
        }

# Main training function
def train_task_model():
    # 1. Load and prepare data
    data = load_data("combinations_with_sentences.json", "labels.json")
    print(f"Loaded {len(data)} examples")
    
    # Display sample data
    print("\nSample data:")
    sample = data[0] if data else {"sentence": "No data", "label": {"time": {}, "task": {}, "detail": {}}}
    print(f"Sentence: {sample['sentence']}")
    if 'label' in sample:
        print(f"Label tokens: {transform_label_to_tokens(sample['label'])}")
    
    # 2. Split data
    train_data, eval_data = train_test_split(data, test_size=0.2, random_state=42)
    
    # 3. Initialize tokenizer and model - using smallest T5 variant
    model_name = "t5-small"  # T5-small is already quite small
    tokenizer = T5Tokenizer.from_pretrained(model_name, use_fast=False)
    
    # Add special tokens for our task
    special_tokens = ["[time]", "[/time]", "[task]", "[/task]", "[eos]", 
                     "[minute]", "[hour]", "[day]", "[week]", "[month]", "[year]",
                     "[period]", "[frequency]", "[duration]", "[deadline]", 
                     "[description]", "[category]", "[event_type]", 
                     "[priority]", "[importance]", "[urgency]", "[is_recurring]",
                     "[date]", "[day_of_week]"]
    
    # Add the special tokens to the tokenizer
    special_tokens_dict = {"additional_special_tokens": special_tokens}
    tokenizer.add_special_tokens(special_tokens_dict)
    
    # Prepare datasets using the custom dataset class
    train_sentences = [item["sentence"] for item in train_data]
    train_labels = [transform_label_to_tokens(item["label"]) for item in train_data]
    
    eval_sentences = [item["sentence"] for item in eval_data]
    eval_labels = [transform_label_to_tokens(item["label"]) for item in eval_data]
    
    train_dataset = TaskSeq2SeqDataset(train_sentences, train_labels, tokenizer)
    eval_dataset = TaskSeq2SeqDataset(eval_sentences, eval_labels, tokenizer)
    
    # 4. Initialize model with smaller configuration
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    model.resize_token_embeddings(len(tokenizer))
    
    # 5. Define training arguments with reduced batch size
    training_args = Seq2SeqTrainingArguments(
        output_dir="./task_parser_model",
        num_train_epochs=100,
        per_device_train_batch_size=16,  # Reduced from 8 to 2
        per_device_eval_batch_size=16,   # Reduced from 8 to 2
        gradient_accumulation_steps=4,  # Added gradient accumulation to maintain effective batch size
        warmup_steps=100,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=50,
        save_steps=500,
        save_total_limit=2,
        prediction_loss_only=True,
        remove_unused_columns=False,
        fp16=False,  # Disable mixed precision to save memory if needed
    )
    
    # 6. Initialize Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )
    
    # 7. Train model
    print("\nStarting training...")
    trainer.train()
    
    # 8. Save model
    trainer.save_model("./task_parser_final")
    print("\nTraining complete. Model saved to './task_parser_final'")
    
    return model, tokenizer, trainer

# Test inference function
def test_inference(model, tokenizer, sentence):
    input_ids = tokenizer(sentence, return_tensors="pt").input_ids
    
    outputs = model.generate(input_ids, max_length=128)  # Reduced max_length
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=False)
    
    print("\nTest inference:")
    print(f"Input: {sentence}")
    print(f"Output: {decoded_output}")

# Run the training
if __name__ == "__main__":
    try:
        model, tokenizer, trainer = train_task_model()
        
        # Test inference on a sample sentence
        test_sentence = "I need to do laundry tomorrow evening."
        test_inference(model, tokenizer, test_sentence)
        
    except Exception as e:
        print(f"An error occurred: {e}")