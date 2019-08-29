import paho.mqtt.client as mqtt

from WeatherAPI.WeatherAPI import Weather

import time
import json



class main:
    broker_address = "postman.cloudmqtt.com"
    password = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
    username = "messages"
    port = 27408
    ssl_certificate = "/home/maw276/magic_mirror_demo/ca.crt"

    def on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def __init__(self, topics):
        self.weather = Weather()
        self.client = self.create_client("weather_client")
        self.client.on_message = self.on_message
        self.client.on_log = self.on_log
        self.client.subscribe('Weather/Update/#')
        self.client.subscribe('Weather/Update')
        self.client.loop_start()
        print("Publishing to 'Weather/Update")
        self.client.publish('Weather/Update', "test 4242")
        time.sleep(4)
        # client.loop_stop()




    def run(self):
        # self.client.loop_forever()
        #while True:
            # self.get_all()
        self.get_weather()
            #time.sleep(600)
            # pass
        # pass

    def create_client(self, name):
        print("Creating Client")
        client = mqtt.Client(name)
        client.tls_set(self.ssl_certificate)
        client.username_pw_set(username=self.username, password=self.password)
        client.connect(self.broker_address, self.port)
        print("Finished Creating Client")
        return client

    #def on_message(self, client , userdata, message):
    #    print("message received ", str(message.payload.decode("utf-8")))
    #    print("message topic=", message.topic)
    #    print("message qos=", message.qos)
    #    print("message retain flag=", message.retain)
    #    if message.topic == "Weather/Update":
    #        temp = self.weather.get_temp()
    #        print("Publishing message to topic", "Weather/Temp")
    #        client.publish("Weather/Temp", temp, 1)

    def on_message(self, client, userdata, message):
        print("message topic=", message.topic)
        print("message received ", str(message.payload.decode("utf-8")))
        request = self.determine_request(message.topic)
        request()
        # temp = request()
        # self.client.publish('Weather/Temp', "temp is " + str(temp))
        # print(temp)

    def determine_request(self, topic):
        switcher = {"Weather/Update": self.get_all,
                    "Weather/Update/Condition": self.get_condition,
                    "Weather/Update/Sunrise": self.get_sunrise,
                    "Weather/Update/Sunset": self.get_sunset,
                    "Weather/Update/Cloud_Cover": self.get_cloud_cover,
                    "Weather/Update/Wind_Speed": self.get_wind_speed,
                    "Weather/Update/Humidity": self.get_humidity}
        return switcher[topic]

    def get_all(self):
        # self.get_temperature()
        # self.get_condition()
        # self.get_sunrise()
        # self.get_sunset()
        # self.get_cloud_cover()
        # self.get_wind_speed()
        # self.get_humidity()
        pass

    def get_weather(self):
        conditions = self.weather.get_update()
        temp = json.dumps(conditions)
        self.client.publish("immerse/Weather/Update", temp, 0, retain=True)

    def get_temperature(self):
        temp = self.weather.get_temp()
        self.client.publish("immerse/Weather/Temp", temp, 0, retain=True)
        return temp

    def get_condition(self):
        condition = self.weather.get_condition()
        self.client.publish("immerse/Weather/Condition", condition, 0, retain=True)

    def get_sunrise(self):
        sunrise = self.weather.get_sunrise()
        self.client.publish("immerse/Weather/Sunrise", sunrise, 0, retain=True)

    def get_sunset(self):
        sunset = self.weather.get_sunset()
        self.client.publish("immerse/Weather/Sunset", sunset, 0, retain=True)

    def get_cloud_cover(self):
        cloud_cover = self.weather.get_cloud_cover()
        self.client.publish("immerse/Weather/Clouds", cloud_cover, 0, retain=True)

    def get_wind_speed(self):
        wind_speed = self.weather.get_wind_speed()
        self.client.publish("immerse/Weather/Wind_Speed", wind_speed, 0, retain=True)

    def get_humidity(self):
        humidity = self.weather.get_humidity()
        self.client.publish("immerse/Weather/Humidity", humidity, 0, retain=True)


if __name__ == '__main__':
    main = main(["Weather/Update"])
    main.run()
