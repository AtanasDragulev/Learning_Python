import datetime
import time
import requests

LATITUDE = 42.698334
LONGITUDE = 23.319941

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}


def is_above_me():
    iss_location = requests.get("http://api.open-notify.org/iss-now.json")
    iss_location.raise_for_status()
    iss_latitude = float(iss_location.json()["iss_position"]["latitude"])
    iss_longitude = float(iss_location.json()["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if LATITUDE - 5 <= iss_latitude <= LATITUDE + 5:
        if LONGITUDE - 5 <= iss_longitude <= LONGITUDE + 5:
            return True
    return False


def is_night():
    sunset_response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    sunrise = sunset_response.json()['results']['sunrise']
    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = sunset_response.json()['results']['sunset']
    sunset = int(sunset.split("T")[1].split(":")[0])
    time_now = datetime.datetime.utcnow().hour
    if sunset < time_now < sunrise:
        return False
    return True


def check():
    if is_night() and is_above_me():
        print("Look up")
    time.sleep(10)
    check()


check()
