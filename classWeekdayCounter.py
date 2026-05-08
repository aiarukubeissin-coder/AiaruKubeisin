import pandas as pd


class WeekdayCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.counts = None

    def count_events(self):
        try:
            self.df = pd.read_csv(self.file_path)

            self.df["event_time"] = pd.to_datetime(
                self.df["event_time"]
            )

            self.df["weekday"] = (
                self.df["event_time"].dt.weekday
            )

            self.counts = (
                self.df.groupby("weekday")
                .size()
                .reset_index(name="count")
            )

            self.counts.to_csv(
                "counts_weekday.csv",
                index=False
            )

        except FileNotFoundError:
            print("Файл табылмады")

    def show_counts(self):
        print(self.counts)

#12