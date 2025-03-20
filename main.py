from flask import Flask, request, jsonify
from flask_cors import CORS  # Allowing frontend to call backend
from geocode import get_coordinates
from weather import get_weather

app = Flask(__name__)
CORS(app)  # Enabling CORS for all routes

# Function to calculate surge price and tax
def calculate_surge_price(base_price, temperature):
    if temperature < 5:
        surge_percent = 0.30
    elif 5 <= temperature < 15:
        surge_percent = 0.20
    elif 15 <= temperature < 25:
        surge_percent = 0.10
    else:
        surge_percent = 0.00

    surge_price = base_price * surge_percent
    total_price_before_tax = base_price + surge_price
    tax = (base_price + surge_price) * 0.10  # 10% tax
    total_price_after_tax = base_price + surge_price + tax

    return {
        "temperature": temperature,
        "base_price": round(base_price, 2),
        "surge_price": round(surge_price, 2),
        "final_price_before": round(total_price_before_tax, 2),
        "tax": round(tax, 2),
        "final_price_after": round(total_price_after_tax, 2),
    }

# Routing
@app.route("/get-weather", methods=["POST"])
def get_weather_api():
    data = request.json
    address = data.get("address")
    base_price = data.get("base_price")

    if not address or base_price is None:
        return jsonify({"error": "Address and base price are required"}), 400

    lat, lon = get_coordinates(address)  # Convert address to lat/lon
    if not lat or not lon:
        return jsonify({"error": "Invalid address"}), 400

    weather_data = get_weather(lat, lon)  # Fetch weather data
    if not weather_data:
        return jsonify({"error": "Weather data not found"}), 500

    temperature = weather_data.get("temperature")
    weather_description = weather_data.get("weather")
    price_details = calculate_surge_price(base_price, temperature)

    return jsonify({
        "temperature": temperature,
        "weather_description": weather_description,
        "base_price": price_details["base_price"],
        "surge_price": price_details["surge_price"],
        "tax": price_details["tax"],
        "final_price_before": price_details["final_price_before"],
        "final_price_after": price_details["final_price_after"]
    })

    #return jsonify(price_details)

if __name__ == "__main__":
    app.run(debug=True)
