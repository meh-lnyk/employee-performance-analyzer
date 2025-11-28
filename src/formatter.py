from tabulate import tabulate

def format_table(rows: list[dict]) -> str:
    if not rows:
        return "No data available"

    return tabulate(rows, headers="keys", tablefmt="github")
