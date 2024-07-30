import requests
import json
import pyttsx3

newsAI=pyttsx3.init()
API_KEY="Api key get from newsapi website"
info = input("Which topic do you you want to now?")
country=input("from which country")
url = f"https://newsapi.org/v2/top-headlines?country={country}&category={info}&apiKey={API_KEY}"
cont = requests.get(url)
# print(cont.text)
news = json.loads(cont.text)
# print(news)
newsAI.say("The render is complete. These headlines are relevant to your query.")

for new in news["articles"]:
    print("Title: ", new["title"])
    newsAI.say(new["title"])
    newsAI.say(new["description"])
    print("Description: ", new["description"])
    print("-----------------------------------")
newsAI.say("Query complete, sir")
newsAI.runAndWait()