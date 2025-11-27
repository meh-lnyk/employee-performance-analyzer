from src.reports.base_report import BaseReport


class PerformanceReport(BaseReport):
    def generate(self, rows):
        if not rows:
            return []

        return [{"total_rows": len(rows)}]
