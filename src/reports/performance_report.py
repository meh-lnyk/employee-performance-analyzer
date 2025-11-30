from src.reports.base_report import BaseReport
from collections import defaultdict


class PerformanceReport(BaseReport):
    def generate(self, rows):
        if not rows:
            return []

        perf_map = defaultdict(list)

        for row in rows:
            pos_name = row.get("position")
            perf_str = row.get("performance")

            if not pos_name or not perf_str:
                continue

            perf_num = float(perf_str)

            perf_map[pos_name].append(perf_num)

        result = []

        for position, values in perf_map.items():
            avg = sum(values) / len(values)
            result.append({
                "position": position,
                "average_performance": round(avg, 2),
            })

        result.sort(key=lambda x: x["average_performance"], reverse=True)

        return result
