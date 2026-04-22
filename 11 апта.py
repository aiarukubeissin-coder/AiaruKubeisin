import pandas as pd

class EventWeekdayPandas:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    def prepare_data(self):
        self.df["event_time"] = self.df["event_time"].astype(str).str.replace("T", " ", regex=False)
        self.df["event_time"] = pd.to_datetime(self.df["event_time"], format="mixed")
        self.df["weekday"] = self.df["event_time"].dt.weekday

    def show_data(self):
        print(self.df)

def main():
    analyzer = EventWeekdayPandas("events.csv")
    analyzer.load_data()
    analyzer.prepare_data()
    analyzer.show_data()

if __name__ == "__main__":
    main()