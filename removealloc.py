import json

def remove_alloc_field(obj):
    """
    Recursively removes all 'alloc' fields from a JSON object.
    """
    if isinstance(obj, dict):
        return {key: remove_alloc_field(value) for key, value in obj.items() if key != 'alloc'}
    elif isinstance(obj, list):
        return [remove_alloc_field(element) for element in obj]
    else:
        return obj

def process_json_file(input_path, output_path):
    """
    Reads a JSON file, removes all 'alloc' fields, and saves the result to another file.
    """
    with open(input_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    data = remove_alloc_field(data)
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

input_file_path = './el-cl-genesis-data/custom_config_data/genesis.json'  # Replace with your input file path
output_file_path = './el-cl-genesis-data/custom_config_data/genesis_noalloc.json'  # Replace with your output file path

process_json_file(input_file_path, output_file_path)
