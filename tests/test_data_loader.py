import csv
from src.data_loader import load_files


def test_load_single_file(tmp_path):
    file = tmp_path / "data.csv"

    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["position", "performance"])
        writer.writerow(["Backend", "5"])

    rows = load_files([str(file)])

    assert len(rows) == 1
    assert rows[0]["position"] == "Backend"
    assert rows[0]["performance"] == "5"

def test_load_multiple_files(tmp_path):
    file1 = tmp_path / "f1.csv"
    file2 = tmp_path / "f2.csv"

    with open(file1, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["position", "performance"])
        writer.writerow(["Backend", "5"])

    with open(file2, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["position", "performance"])
        writer.writerow(["Frontend", "4"])

    rows = load_files([str(file1), str(file2)])

    assert len(rows) == 2
    assert rows[0]["position"] == "Backend"
    assert rows[1]["position"] == "Frontend"
