import json
import os

DATA_FILE = "numbers.json"

def persist_and_sum(new_number: int) -> int:
    numbers = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                numbers = json.load(f)
            except json.JSONDecodeError:
                numbers = []

    numbers.append(new_number)

    with open(DATA_FILE, "w") as f:
        json.dump(numbers, f)

    return sum(numbers)
