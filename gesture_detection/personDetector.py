from gpiozero import DistanceSensor
import time
# from pynput.keyboard import Key, Controller
import paho.mqtt.client as mqtt
from threading import Timer

# TODO - (1) Simulate keypresses (2) Read from a config.json file to allow configuration

class PersonDetector:
	mirror_is_on = False
	ultrasonic = None
	keyboard = None
	activate_key = None
	deactivate_key = None
	timer = None
	pub_topic = None
	broker_address = "postman.cloudmqtt.com"
    password = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
    username = "messages"
    port = 27408
    ssl_certificate = "ca.crt"
	def __init__(self, echo_pin=17, trigger_pin=4, max_dist=2, threshold_dist=1, pub_topic="mirror_on"):
		self.ultrasonic = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=max_dist, threshold_distance=threshold_dist)
		self.ultrasonic.when_in_range = self.__person_detected
		self.ultrasonic.when_out_of_range = self.__person_not_detected
		self.client = self.create_client("proximity_client")
		self.pub_topic = pub_topic
		#self.keyboard = Controller()
		#self.activate_key = activate_key
		#self.deactivate_key = deactivate_key
		self.timer = Timer(8.0, self.shutdownCountoff, [self])
	def __person_detected(self):
		print("Person Detected")
		if self.mirror_is_on:
			self.timer.cancel()
		else:
			self.client.publish(self.pub_topic, "on")
			self.mirror_is_on = True
		#self.keyboard.press(self.activate_key)
		#self.keyboard.release(self.activate_key)
	def __person_not_detected(self):
		print("Person NOT detected")
		if self.mirror_is_on:
			self.timer.start()
	def shutdownCountoff(self):
		print("Turning off mirror")
		self.client.publish(self.pub_topic, "off")
		self.mirror_is_on = False
		#self.keyboard.press(self.deactivate_key)
		#self.keyboard.release(self.deactivate_key)
		# Do MQTT Stuff to tell the mirror to shut off
	def create_client(self, name):
        print("Creating Client")
        client = mqtt.Client(name)
        client.tls_set(self.ssl_certificate)
        client.username_pw_set(username=self.username, password=self.password)
        client.connect(self.broker_address, self.port)
        print("Finished Creating Client")
        return client
	@classmethod
	def init_from_json(jsonFileName="config.json"):
		print("Initializing from " + jsonFileName)
		

# Possible States: Person Not detected & Off, Person Detected & On, Person Not Detected & On

pd = PersonDetector()

# while True:
# 	print(ultrasonic.distance)
#	time.sleep(1)
