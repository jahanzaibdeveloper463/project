import json
import os

def get_mobile_data():
    # File path 'data.json' set kar diya hai
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            mobiles_list = json.load(file)
            return mobiles_list
    except Exception as e:
        print(f"Error loading data.json file: {e}")
        return []

if __name__ == "__main__":
    # Scraper direct test
    data = get_mobile_data()
    print(f"Total Mobiles Loaded: {len(data)}")
    for mob in data[:5]:
        print(mob)