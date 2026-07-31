from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

with open("data/crops.json", "r") as file:
    crops = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/crops")
def get_crops():
    search = request.args.get("search", "").lower()

    results = [
        crop for crop in crops
        if search in crop["name"].lower()
    ]

    return jsonify(results)


@app.route("/api/weather")
def weather():
    city = request.args.get("city", "Kigali")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({
                "error": response.json()
            }), response.status_code

        data = response.json()

        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
