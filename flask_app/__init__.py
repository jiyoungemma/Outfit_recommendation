import os
from flask import Flask, render_template, request

import pickle

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html'), 200

@app.route('/city', methods=['POST'])
def city():
    value = request.form['index']
    city_name = "%s" %value

    import requests
    import json

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid="

    weater_data = requests.get(weather_url)
    current_weather = json.loads(weater_data.text)

    weather_like = current_weather['weather'][0]['description'] # 현재 날씨 상태
    temp_feel_like= round(current_weather['main']['feels_like'] - 273.15,2) # 현재 체감 온도
    windy = current_weather['wind']['speed']
    
    
    model = pickle.load(open('weather.pkl','rb'))

    outfit = model.predict([temp_feel_like])

    return render_template('weather.html',weather=weather_like,
                        temp=temp_feel_like, windy=windy,outfit=outfit), 200

@app.route('/outfit', methods=['POST'])
def outfit():

    return render_template('recommend.html'),200
if __name__ == "__main__":
    app.run(debug=True)