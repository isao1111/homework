import streamlit as st
import requests from datetime import datatime
import pandas as pd

print("天気アプリ")
print("東京の天気を表示しています")
print("東京のcitycodeは130010です。")

url= "https://weather.tsukumijima.net/api/forecast/city/" + "130010"

response = requests.get(url)

weather_json = response.json()
now_hour = datetime.now().hour

if 0 <= now_hour and now_hour < 6:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
elif 6 <=now_hour and now_hour < 12:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
elif 12 <=now_hour and now_hour < 18:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
else:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T18-24']

weather_now_text = "現在の降水確率：" + weather_now
print(weather_now_text)

df1 = pd.DataFrame(weather_json['forecasts'][0]['chanceOfRain'],index=["今日"])
df2 = pd.DataFrame(weather_json['forecasts'][1]['chanceOfRain'],index=["明日"])
df3 = pd.DataFrame(weather_json['forecasts'][2]['chanceOfRain'],index=["明後日"])

df= pd.concat([df1,df2,df3])
print(df)