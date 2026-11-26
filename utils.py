
import json
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")


def load_data(file_name):
    file_path = os.path.join(DATA_FOLDER, file_name)

    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_data(file_name, data):
    file_path = os.path.join(DATA_FOLDER, file_name)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")
