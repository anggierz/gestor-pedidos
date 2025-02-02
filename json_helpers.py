import os
import json
from bst import BST


def read_json(filepath: str):
    if not os.path.isfile(filepath):
        with open(filepath, "w") as f:
            json.dump([], f)
    with open(filepath, "r") as f:
        data = json.load(f)
    return data



def write_json(filepath: str, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
        