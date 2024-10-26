

import json
import os

DATABASE_FILE = 'data/rules.json'

def load_rules():
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, 'r') as f:
        return json.load(f)

def save_rules(rules):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(rules, f, indent=4)

