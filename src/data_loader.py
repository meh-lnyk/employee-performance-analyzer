import csv


def load_files(paths):
    rows = []
    for path in paths:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows.extend(reader)
    return rows
