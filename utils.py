import json
import random

def load_artwork_details(json_path='sources.json'):
    with open(json_path, 'r', encoding='utf-8') as file:
        sources = json.load(file)
    return {source['title']: {'file_path': source['file_path'], 'position': source['position']} for source in sources}

def random_position():
    x = random.randint(1, 3)
    y = random.randint(1, 4)
    return x, y