import json

# Load user data from JSON file
def load_user_data(target_file='user_data.json'):
    try:
        with open(target_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
# Save user data to JSON file
def save_user_data(data,target_file='user_data.json'):
    with open(target_file, 'w') as file:
        json.dump(data, file, indent=4)

