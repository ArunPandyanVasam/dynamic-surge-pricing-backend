import requests

OpenCageGeocoding_API_KEY = "9048966996da4ac395098eef17315ec5" # My API KEY
address = "1600 Amphitheatre Parkway, Mountain View, CA" # Random Place

# OpenCage API endpoint
OpenCageGeocoding_url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={OpenCageGeocoding_API_KEY}"

# Now I have to send request to Opencage using URL
OpenCageGeocoding_response = requests.get(OpenCageGeocoding_url)
OpenCageGeocoding_data = OpenCageGeocoding_response.json()

# Using data extract the latitude and longitude
if OpenCageGeocoding_data["results"]:
    lat = OpenCageGeocoding_data["results"][0]["geometry"]["lat"]
    lon = OpenCageGeocoding_data["results"][0]["geometry"]["lng"]
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Location not found")