import pandas as pd


class EventWeekdayPandas:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def process_data(self):
        try:
            self.df = pd.read_csv(self.file_path)

            self.df["event_time"] = pd.to_datetime(
                self.df["event_time"]
            )

            self.df["weekday"] = (
                self.df["event_time"].dt.weekday
            )

        except FileNotFoundError:
            print("Файл табылмады")

    def show_data(self):
        print(self.df)

#11