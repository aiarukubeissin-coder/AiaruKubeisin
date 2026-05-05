import pandas as pd
import matplotlib.pyplot as plt


class WeekdayChart:
    def __init__(self, file_path):
        self.file_path = file_path
        self.counts = None

    def load_data(self):
        self.counts = pd.read_csv(self.file_path)

    def make_chart(self):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        plt.figure()

        plt.bar(self.counts["weekday"], self.counts["count"])

        plt.xticks(range(7), days)
        plt.xlabel("Weekday")
        plt.ylabel("Count")
        plt.title("Events by Weekday")

        plt.tight_layout()

        plt.savefig("weekday_chart.png")  # файл сақталады
        plt.show()  # ГРАФИК АШЫЛАДЫ


def main():
    chart = WeekdayChart("counts_weekday.csv")
    chart.load_data()
    chart.make_chart()


if __name__ == "__main__":
    main()

#13