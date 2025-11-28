from src.reports.base_report import BaseReport
from collections import defaultdict


class PerformanceReport(BaseReport):
    def generate(self, rows):
        if not rows:
            return []

        perf_map = defaultdict(list)

        for row in rows:
            pos_name = row.get("position")
            perf_num = row.get("performance")

            if not pos_name or not perf_num:
                continue

            try:
                perf_num = float(perf_num)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            perf_map[pos_name].append(perf_num)

        result = []

        for position, values in perf_map.items():
            avg = sum(values) / len(values)
            result.append({
                "position": position,
                "average_performance": round(avg, 2),
            })

        return result
