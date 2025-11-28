import csv


def load_files(paths):
    rows = []
    for path in paths:
        try:
            with open(path, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                rows.extend(reader)
        except FileNotFoundError as e:
            print(f"Error: {e}")
    return rows
