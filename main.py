# main.py

from classEventDateExtractor import EventDateExtractor
from classEventWeekdayFinder import EventWeekdayFinder
from classEventWeekdayPandas import EventWeekdayPandas
from classWeekdayCounter import WeekdayCounter
from classWeekdayChart import WeekdayChart
from classApiService import ApiService


def main():
    file_path = "events.csv"

    print("===== EVENT PROJECT =====")

    # 9
    print("\n--- TASK 9 ---")

    extractor = EventDateExtractor(file_path)

    extractor.extract_date_parts()

    extractor.show_data()

    # 10
    print("\n--- TASK 10 ---")

    weekday_finder = EventWeekdayFinder(file_path)

    weekday_finder.calculate_weekday()

    weekday_finder.show_result()

    # 11
    print("\n--- TASK 11 ---")

    pandas_weekday = EventWeekdayPandas(file_path)

    pandas_weekday.process_data()

    pandas_weekday.show_data()

    # 12
    print("\n--- TASK 12 ---")

    counter = WeekdayCounter(file_path)

    counter.count_events()

    counter.show_counts()

    # 13
    print("\n--- TASK 13 ---")

    chart = WeekdayChart(file_path)

    chart.build_chart()

    # 14
    print("\n--- TASK 14 ---")

    api = ApiService(file_path)

    data = api.get_data()

    print(data)

    api.run_server()
#/weekday-counts

if __name__ == "__main__":
    main()