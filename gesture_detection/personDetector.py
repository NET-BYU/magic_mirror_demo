from gpiozero import DistanceSensor
import time
import paho.mqtt.client as mqtt
from threading import Timer
import time

# TODO - (1) Read from a config.json file to allow configuration

class PersonDetector:
	mirror_is_on = False	# Variable which tells whether the mirror is actually "on" or not
	ultrasonic = None		# The proximity sensor
	timer = None			# The timer which counts down when a person is no longer detected before turning the mirror off
	pub_topic = None		# The MQTT topic we need to publish to
	client = None			# The MQTT client we use to publish
	
	def __init__(self, echo_pin=17, trigger_pin=4, max_dist=2, threshold_dist=1, pub_topic="immerse/auth"):
		self.ultrasonic = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=max_dist, threshold_distance=threshold_dist)
		self.ultrasonic.when_in_range = self.__person_detected
		self.ultrasonic.when_out_of_range = self.__person_not_detected
		self.pub_topic = pub_topic
		self.timer = Timer(5.0, self.shutdownCountoff)
		user = "messages"
		psw = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
		host = "postman.cloudmqtt.com"
		port = 27408
		self.client = mqtt.Client()
		self.client.username_pw_set(user, password = psw)
		self.client.tls_set(ca_certs = "../ca.crt")
		self.client.connect(host,port,keepalive=60,bind_address="")
		self.client.publish(self.pub_topic, "{\"State\": \"OFF\"}", qos=1, retain=True)	# Do MQTT Stuff to tell the mirror to shut off

	def __person_detected(self):
		print("Person Detected")
		if self.mirror_is_on:
			self.timer.cancel()
			self.timer = Timer(5.0, self.shutdownCountoff)
		else:
			self.client.publish(self.pub_topic, "{\"State\": \"ON\"}", qos=1, retain=True)
			self.mirror_is_on = True

	def __person_not_detected(self):
		print("Person NOT detected")
		if self.mirror_is_on:
			try:
				self.timer = Timer(5.0, self.shutdownCountoff)
				self.timer.start()
			except Exception as RuntimeError:
				print("Tried to start timer twice :P")

	def shutdownCountoff(self):
		print("Turning off mirror")
		self.client.publish(self.pub_topic, "{\"State\": \"OFF\"}", qos=1, retain=True)	# Do MQTT Stuff to tell the mirror to shut off
		self.mirror_is_on = False

	@classmethod
	def init_from_json(jsonFileName="config.json"):
		print("Initializing from " + jsonFileName)
		

pd = PersonDetector()	# Create an instance of the Person Detector to start the code
while True:
	time.sleep(10)
