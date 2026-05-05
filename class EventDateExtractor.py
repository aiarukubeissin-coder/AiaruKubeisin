import csv
from datetime import datetime


class EventDateExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.events = []

    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.events.append(row)

    def extract_date_parts(self):
        for event in self.events:
            date_str = event["event_time"]

            dt = datetime.fromisoformat(date_str.replace("T", " "))

            event["date_only"] = dt.date().isoformat()
            event["date_tuple"] = (dt.year, dt.month, dt.day)
            event["ordinal"] = dt.date().toordinal()

    def show_data(self):
        for event in self.events:
            print(event)


def main():
    extractor = EventDateExtractor("events.csv")
    extractor.load_data()
    extractor.extract_date_parts()
    extractor.show_data()


if __name__ == "__main__":
    main()

#9