import pandas as pd


class WeekdayCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.counts = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    def prepare_data(self):
        self.df["event_time"] = self.df["event_time"].astype(str).str.replace("T", " ", regex=False)
        self.df["event_time"] = pd.to_datetime(self.df["event_time"], format="mixed")
        self.df["weekday"] = self.df["event_time"].dt.weekday

    def count_events(self):
        self.counts = self.df.groupby("weekday").size().reset_index(name="count")

        all_days = pd.DataFrame({"weekday": list(range(7))})
        self.counts = all_days.merge(self.counts, on="weekday", how="left")

        self.counts["count"] = self.counts["count"].fillna(0).astype(int)

    def save_counts(self):
        self.counts.to_csv("counts_weekday.csv", index=False)

    def show_counts(self):
        print(self.counts)


def main():
    counter = WeekdayCounter("events.csv")
    counter.load_data()
    counter.prepare_data()
    counter.count_events()
    counter.save_counts()
    counter.show_counts()


if __name__ == "__main__":
    main()