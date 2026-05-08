from flask import Flask, jsonify
import pandas as pd


class ApiService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.app = Flask(__name__)

        self.create_routes()

    def get_data(self):
        df = pd.read_csv(self.file_path)

        df["event_time"] = pd.to_datetime(df["event_time"])

        df["weekday"] = df["event_time"].dt.weekday

        counts = df.groupby("weekday").size()

        result = []

        for day, count in counts.items():
            result.append({
                "weekday": int(day),
                "count": int(count)
            })

        return result

    def create_routes(self):
        @self.app.route("/weekday-counts", methods=["GET"])
        def weekday_counts():
            return jsonify(self.get_data())

    def run_server(self):
        print("\n=== WEEK 14 API RUNNING ===")

        self.app.run(debug=True)