from src.reports.performance_report import PerformanceReport


def test_average_calculation():
    rows = [
        {"position": "Backend", "performance": "5"},
        {"position": "Backend", "performance": "3"},
        {"position": "Frontend", "performance": "4"},
    ]

    report = PerformanceReport()
    result = report.generate(rows)

    assert len(result) == 2

    # Backend avg = (5 + 3) / 2 = 4.0
    backend = next(r for r in result if r["position"] == "Backend")
    assert backend["average_performance"] == 4.0

    # Frontend avg = 4
    frontend = next(r for r in result if r["position"] == "Frontend")
    assert frontend["average_performance"] == 4.0
