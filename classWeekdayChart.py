import pandas as pd
import matplotlib.pyplot as plt


class WeekdayChart:
    def __init__(self, file_path):
        self.file_path = file_path

    def build_chart(self):
        try:
            df = pd.read_csv(self.file_path)

            df["event_time"] = pd.to_datetime(
                df["event_time"]
            )

            df["weekday"] = (
                df["event_time"].dt.weekday
            )

            counts = (
                df.groupby("weekday")
                .size()
            )

            plt.figure(figsize=(8, 5))

            plt.bar(
                counts.index,
                counts.values
            )

            plt.xlabel("Weekday")
            plt.ylabel("Count")
            plt.title("Events By Weekday")

            plt.savefig("weekday_chart.png")

            print("PNG сақталды")

        except FileNotFoundError:
            print("Файл табылмады")

#13