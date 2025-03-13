import requests

OPENCAGE_API_KEY = "9048966996da4ac395098eef17315ec5"

def get_coordinates(address):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={OPENCAGE_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error fetching coordinates: {data.get('status', 'Unknown error')}")
            return None, None

        if data["results"]:
            lat = data["results"][0]["geometry"]["lat"]
            lon = data["results"][0]["geometry"]["lng"]
            return lat, lon
    except Exception as e:
        print(f"Error with geocoding API: {e}")
    return None, None