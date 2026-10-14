import csv
from collectors import MainCollector
from config import FIELDS


def collect(filename: str, period_in_seconds: int, interval_in_seconds: int):
    collector = MainCollector()
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if file.tell() == 0:
            writer.writeheader()

        for data in collector.collect(period_in_seconds, interval_in_seconds):
            writer.writerow(data)
