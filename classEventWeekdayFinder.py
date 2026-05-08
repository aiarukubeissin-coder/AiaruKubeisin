from datetime import datetime


class EventWeekdayFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.weekdays = []

    def calculate_weekday(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                next(file)

                for line in file:
                    event_time = line.strip()

                    try:
                        dt = datetime.fromisoformat(event_time)

                        weekday = dt.weekday()

                        self.weekdays.append({
                            "event_time": event_time,
                            "weekday": weekday
                        })

                    except ValueError:
                        print("Дата қате")

        except FileNotFoundError:
            print("Файл табылмады")

    def show_result(self):
        for item in self.weekdays:
            print(item)

#10