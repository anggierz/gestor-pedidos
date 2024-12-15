import os
import json
from bst import BST


def save_to_json(filename: str, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json(filename: str):
    with open(filename, 'r') as file:
        data = json.load(file)
        
    return data