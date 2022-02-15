import urllib.request
import requests
import json

# openweather api

API_KEY = '01007ac547f53225b91a08fdd176080d'
city_name = input("Enter the city where you are now : ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=01007ac547f53225b91a08fdd176080d"

weater_data = requests.get(weather_url)
current_weather = json.loads(weater_data.text)




# naver 쇼핑 검색 api


client_id = 'avows1Qo6y3IJw23j3ia'
client_secret = 'boNGrtqcan'

product = input("Enter the product what you need : ")
display = input("Enter the number how many pages you want to see : ")
encText = display.encode('utf-8')
shopping_url = f"https://openapi.naver.com/v1/search/shop?query={encText}&display={display}"# json 결과

request = urllib.request.Request(shopping_url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_decoding = response_body.decode('utf-8') # type() -> str
    json_data = json.loads(response_decoding) # type() -> dict

# json_data에서 title,link,image, lprice, hprice, mallName 만 저장
    name_list = ['title','mallName','lprice','hprice','link','image']
    json_dict = []
    for i in range(int(display)):
        for j in name_list:
            json_dict.append(f"{j} : " + json_data['items'][i][j]) # display 개수만큼 json_dict에 저장
else:
    print("Error Code:" + rescode)
