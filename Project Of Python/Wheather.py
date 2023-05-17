import requests
import json
import pyttsx3

city=str(input("Enter Your City name :"))
url=f"https://api.weatherapi.com/v1/current.json?key=de5a1259a5034cb690c94325231705&q={city}"
r=requests.get(url)
WeatherDictonary=json.loads(r.text)
temp=WeatherDictonary["current"]["temp_f"]
print(temp)
text_to_speech = pyttsx3.init()
word=(f"The current temperature of {city} city is {temp} degree farehanhit.")
text_to_speech.say(word)
text_to_speech.runAndWait()
