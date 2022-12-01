import requests

lat = 42.698334
lon = 23.319941


part = "current,minutely,daily,alerts"
api_key = "your_api_key"
params = {"lat": lat,
          "lon": lon,
          "exclude": part,
          "appid": api_key
          }
api = f"https://api.openweathermap.org/data/2.5/onecall"

request = requests.get(api, params=params)
request.raise_for_status()
weather_data = request.json()
weather_slice = weather_data["hourly"][:12]
weather = [day["weather"][0]["id"] for day in weather_slice if int(day["weather"][0]["id"]) < 700]
if len(weather) > 0:
    print("Bring umbrella")
