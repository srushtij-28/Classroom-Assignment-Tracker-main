import json
import os


def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
