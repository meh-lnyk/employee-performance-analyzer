from src.reports.performance_report import PerformanceReport

REPORTS = {
    "performance": PerformanceReport,
}

def run_report(report_name, rows):
    if report_name not in REPORTS:
        raise ValueError(f"Unknown report: {report_name}")

    report_class = REPORTS[report_name]
    report = report_class()
    return report.generate(rows)
