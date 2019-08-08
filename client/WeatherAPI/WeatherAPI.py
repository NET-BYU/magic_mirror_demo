import urllib.request
from json import loads
import time
import csv

def run():

    contents = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?id=5780026&appid=48e1755fef3b8886e5d93a0209bf146d&units=imperial").read()
    out = open("Hello.txt", "w")
    out.write(str(contents))
    out.close()
    d = loads(contents)
    temp = d["main"]["temp"]
    print((temp -273.15) * 9 / 5 + 32)
    pass

class Weather:

    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/weather?id=5780026&appid=48e1755fef3b8886e5d93a0209bf146d&units=imperial"
        self.time = 0
        self.data = None

    def get_temp(self):
        self.get_weather()
        # if int(time.time()) >= int(self.time + 600) or self.data is None:
        #     test = time.ctime(self.time)
        #     contents = urllib.request.urlopen(self.url).read()
        #     self.data = loads(contents)
        #     self.time = int(time.time())
        #     print("Getting new weather")
        # else:
        #     print("Using old weather")
        return self.data["main"]["temp"]

    def get_condition(self):
        self.get_weather()
        return self.data['weather'][0]['main']

    def get_sunrise(self):
        self.get_weather()
        return self.data['sys']['sunrise']

    def get_sunset(self):
        self.get_weather()
        return self.data['sys']['sunset']

    def get_weather(self):
        if int(time.time()) >= int(self.time + 600) or self.data is None:
            contents = urllib.request.urlopen(self.url).read()
            self.data = loads(contents)
            self.time = int(time.time())

    def get_cloud_cover(self):
        self.get_weather()
        return self.data['clouds']['all']

    def get_wind_speed(self):
        self.get_weather()
        return self.data['wind']['speed']

    def get_humidity(self):
        self.get_weather()
        return self.data['main']['humidity']

    def get_update(self):
        self.get_weather()
        weather = dict()
        weather['temp'] = self.data["main"]["temp"]
        weather['condition'] = self.data['weather'][0]['main']
        weather['sunrise'] = self.data['sys']['sunrise']
        weather['sunset'] = self.data['sys']['sunset']
        weather['cloud_cover'] = self.data['clouds']['all']
        weather['wind_speed'] = self.data['wind']['speed']
        weather['humidity'] = self.data['main']['humidity']
        weather['id'] = self.data['weather'][0]['id']
        weather['description'] = self.data['weather'][0]['description']
        weather['icon'] = self.data['weather'][0]['icon']
        return weather

if __name__ == "__main__":
    weather = Weather()
    print("Current Weather")
    temp = weather.get_temp()
    print("Temperature:", temp)
    condition = weather.get_condition()
    print("Condition:", condition)