import requests

# My OpenWeatherMap API KEY
OpenWeatherMap_API_KEY = "7de154493d96503ed06862f051361fb3"

# Coordinates
lat = 37.4224764
lon = -122.0842499

#OpenWeatherMap API endpoint
OpenWeatherMap_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OpenWeatherMap_API_KEY}&units=metric"

# Now I have to request to the weather API to give data
OpenWeatherMap_response = requests.get(OpenWeatherMap_url)
OpenWeatherMap_data = OpenWeatherMap_response.json()

if OpenWeatherMap_data.get("cod") == 200:
    weather = OpenWeatherMap_data["weather"][0]["description"]
    temperature = OpenWeatherMap_data["main"]["temp"]
    humidity = OpenWeatherMap_data["main"]["humidity"]

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
else:
    print("Error fetching weather data.")