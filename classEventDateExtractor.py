from datetime import datetime


class EventDateExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = []

    def extract_date_parts(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                next(file)

                for line in file:
                    event_time = line.strip()

                    try:
                        dt = datetime.fromisoformat(event_time)

                        only_date = dt.date()

                        ordinal = only_date.toordinal()

                        data_tuple = (
                            only_date.year,
                            only_date.month,
                            only_date.day
                        )

                        self.result.append({
                            "date": str(only_date),
                            "ordinal": ordinal,
                            "tuple": data_tuple
                        })

                    except ValueError:
                        print("Дата қате")

        except FileNotFoundError:
            print("Файл табылмады")

    def show_data(self):
        for item in self.result:
            print(item)