import requests

WEATHER_API_KEY = "7de154493d96503ed06862f051361fb3"

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error fetching weather: {data.get('message', 'Unknown error')}")
            return None

        if data.get("cod") == 200:
            return {
                "weather": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"]
            }
    except Exception as e:
        print(f"Error with weather API: {e}")
    return None
