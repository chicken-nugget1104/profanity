import json

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    def clean_text(text):
        return text.replace('[', '').replace(']', '').replace('"', '').replace(',', '')
    
    def process_data(d):
        if isinstance(d, dict):
            return '\n'.join(f"{key}: {process_data(value)}" for key, value in d.items())
        elif isinstance(d, list):
            return '\n'.join(process_data(item) for item in d)
        elif isinstance(d, str):
            return clean_text(d)
        else:
            return str(d)
    
    cleaned_data = process_data(data)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_data)
        
# Output
json_to_txt('words.json', 'output2.txt')