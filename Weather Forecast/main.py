import requests
import smtplib
import os
User = "Email address from where mail will be send"
Password = "a passkey generated my google accounts"
URL="https://api.openweathermap.org/data/2.5/forecast"
API_key=os.environ["WFA_KEY"]
PARAM={
    "lat":29.21,
    "lon":79.51,
    "appid":API_key,
    "cnt":4
}

response=requests.get(URL,params=PARAM)
response.raise_for_status()
info=response.json()
# print(f"Status Code: {info["cod"]}")
forecast=info["list"]
# print(forecast)

is_rain=False
for weather in forecast:
    list_cond=weather["weather"][0]["id"]
    # print(list_cond)
    if list_cond<700:
       is_rain=True
if is_rain:
    # paramfor_msg={"phone":[phone_number],"text":[message],"apikey":[your_apikey]}
    #  requests.get("https://api.callmebot.com/whatsapp.php")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=User, password=Password)
        connection.sendmail(from_addr=User, to_addrs="address where mail will be send",
                            msg=f"Subject:Rainy Day\n\nBring up your umbrella. It's Going to be rain")
