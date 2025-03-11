from flask import Flask, request, render_template
from geocode import get_coordinates
from weather import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        address = request.form["address"]
        lat, lon = get_coordinates(address)

        if lat and lon:
            weather_data = get_weather(lat, lon)

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
