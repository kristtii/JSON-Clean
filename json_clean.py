import json

def process_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
        
    new_data = replace_field_names(data)
    
    with open(output_file, 'w') as f:
        json.dump(new_data, f, indent=4)

def replace_field_names(data):
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_key = key.replace(',', '').replace('-', ' ').replace('(', '').replace(')', '').replace('$', '').replace(' ', '_').lower()
            new_data[new_key] = replace_field_names(value)
        return new_data
    elif isinstance(data, list):
        return [replace_field_names(item) for item in data]
    else:
        return data

# Usage example
input_file = '/Documents/file1.json'
output_file = '/Documents/clean_file1.json'

process_json(input_file, output_file)