import sys

from analyzer import calculate_metrics
from data_loader import load_ga4_csv
from report_writer import print_report


def main():
    if len(sys.argv) < 2:
        print("사용법: python main.py data/user_data_cclibrary.csv")
        return

    csv_path = sys.argv[1]

    df = load_ga4_csv(csv_path)
    metrics = calculate_metrics(df)
    print_report(metrics)


if __name__ == "__main__":
    main()
