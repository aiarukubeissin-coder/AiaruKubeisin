import csv
from datetime import datetime

class EventWeekdayFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.events = []

    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.events.append(row)

    def add_weekday(self):
        for event in self.events:
            date_str = event["event_time"]
            dt = datetime.fromisoformat(date_str.replace("T", " "))
            event["weekday"] = dt.weekday()

    def show_data(self):
        for event in self.events:
            print(event)

def main():
    finder = EventWeekdayFinder("events.csv")
    finder.load_data()
    finder.add_weekday()
    finder.show_data()

if __name__ == "__main__":
    main()