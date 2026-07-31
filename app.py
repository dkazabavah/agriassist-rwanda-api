from flask import Flask, render_template, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# ---------- Load Data ----------

def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception:
        return []


crops = load_json("data/crops.json")
diseases = load_json("data/diseases.json")
market_prices = load_json("data/market_prices.json")
tips = load_json("data/farming_tips.json")
calendar = load_json("data/planting_calendar.json")


# ---------- Pages ----------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")



# ---------- Crop API ----------

@app.route("/api/crops")
def get_crops():

    search = request.args.get("search", "").lower()

    results = [
        crop for crop in crops
        if search in crop.get("name","").lower()
    ]

    return jsonify(results)



# ---------- Weather API ----------

@app.route("/api/weather")
def weather():

    city = request.args.get("city", "Kigali")

    if not WEATHER_API_KEY:
        return jsonify({
            "error": "Weather API key missing"
        }), 500


    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )


    try:

        response = requests.get(url, timeout=10)


        if response.status_code != 200:

            return jsonify({
                "error": "Unable to fetch weather data"
            }), response.status_code


        data = response.json()


        return jsonify({

            "city": data["name"],

            "temperature":
            data["main"]["temp"],

            "humidity":
            data["main"]["humidity"],

            "condition":
            data["weather"][0]["description"]

        })


    except requests.exceptions.Timeout:

        return jsonify({
            "error":"Weather service timeout"
        }),500


    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500




# ---------- Disease API ----------

@app.route("/api/diseases")
def get_diseases():

    crop = request.args.get("crop","").lower()


    results = [

        disease for disease in diseases

        if crop in disease.get("crop","").lower()

    ]


    return jsonify(results)




# ---------- Market API ----------

@app.route("/api/market")
def market():

    return jsonify(market_prices)




# ---------- Farming Tips ----------

@app.route("/api/tips")
def farming_tips():

    return jsonify(tips)




# ---------- Crop Recommendation ----------

@app.route("/api/recommend")
def recommend():

    soil = request.args.get("soil","").lower()

    results=[]


    for crop in crops:

        if soil in crop.get("soil","").lower():

            results.append(crop)


    return jsonify(results)




if __name__ == "__main__":

    app.run(debug=True)
