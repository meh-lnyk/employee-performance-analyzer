import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV data files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name to generate"
    )

    return parser.parse_args(argv)


def main():
    args = parse_args()

    print(f"Files: {args.files}")
    print(f"Report: {args.report}")


if __name__ == "__main__":
    main()
