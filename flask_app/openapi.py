import urllib.request
import requests
import json

# openweather api

API_KEY = ''
city_name = input("Enter the city where you are now : ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid="

weater_data = requests.get(weather_url)
current_weather = json.loads(weater_data.text)
