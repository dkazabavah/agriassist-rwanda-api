from utils.recommendations import recommend_crop
from flask import Flask, render_template, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def load_data(filename):
    with open(f"data/{filename}", "r") as file:
        return json.load(file)


crops = load_data("crops.json")
tips = load_data("farming_tips.json")
diseases = load_data("diseases.json")
markets = load_data("market_prices.json")
calendar = load_data("planting_calendar.json")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/api/crops")
def get_crops():

    search = request.args.get("search", "").lower()

    results = [
        crop for crop in crops
        if search in crop["name"].lower()
    ]

    return jsonify(results)


@app.route("/api/tips")
def get_tips():
    return jsonify(tips)


@app.route("/api/diseases")
def get_diseases():
    return jsonify(diseases)


@app.route("/api/markets")
def get_markets():
    return jsonify(markets)


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/diseases")
def diseases():
    return render_template("diseases.html")


@app.route("/markets")
def market_page():
    return render_template("markets.html")

@app.route("/api/calendar")
def get_calendar():
    return jsonify(calendar)


@app.route("/markets")
def markets():
    return render_template("markets.html")


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
        }),500


@app.route("/api/recommend", methods=["POST"])
def recommendation():

    data=request.json

    result = recommend_crop(
        data.get("soil"),
        data.get("season"),
        data.get("water")
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
