import os

# Generate 1000 keyword combinations
def print_all_file_paths(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

print_all_file_paths("task_parser_final")