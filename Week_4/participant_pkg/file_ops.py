import csv
from pathlib import Path


def save_participant(path:Path, participant_dict: dict):
    try:
        with open(path, 'a', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(participant_dict)
            headers = ['name', 'age', 'phone', 'track']

            if not path.exists():
                writer.writeheader(headers)
            writer.writerows(participant_dict)
        return True
    except Exception as e:
        return False


def load_participants(path: Path):
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)

        for row_number, row in  enumerate (reader):
            if row_number == 0:    
                print(f"Headers: {' | '. join(row)}")
                print("-" * 40)
            else:
                name, age, phone, track = row
                print(f"{name} ({age} years) - {phone} {track}")