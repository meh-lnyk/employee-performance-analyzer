from argparse import ArgumentParser
from src.data_loader import load_files
from src.report_engine import run_report
from src.formatter import format_table


def parse_args(argv=None):
    parser = ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(argv)


def main():
    args = parse_args()
    rows = load_files(args.files)
    try:
        result = run_report(args.report, rows)
        if not result:
            print("Report returned empty result")
        else:
            result = run_report(args.report, rows)
            output = format_table(result)
            print(output)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
