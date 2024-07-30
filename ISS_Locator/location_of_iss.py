import time
import requests
from datetime import datetime
import smtplib

LAT = 29.379910
LNG = 79.477386
User = ""#Your email address
Password = ""#Password set on you google profile
time_current = datetime.now()


def iss_inbound():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    info = response.json()
    longitude = float(info["iss_position"]["longitude"])
    latitude = float(info["iss_position"]["latitude"])
    if LAT - 5 <= latitude <= LAT + 5 and LNG + 5 <= longitude <= LNG + 5:
        return True


def is_night():
    parameter = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    info = response.json()
    sunrise_time = int(info["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(info["results"]["sunset"].split("T")[1].split(":")[0])
    if time_current.hour >= sunset_time or time_current.hour <= sunrise_time:
        return True


while True:
    time.sleep(60)
    if iss_inbound() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=User, password=Password)
            connection.sendmail(from_addr=User, to_addrs="Email address where you want to send the email", msg="Subject:ISS Inbound\n\nLook Up!")
