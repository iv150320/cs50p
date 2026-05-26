import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(rows, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
