from gpiozero import DistanceSensor
import time
from pynput.keyboard import Key, Controller

# TODO - (1) Simulate keypresses (2) Read from a config.json file to allow configuration

class PersonDetector:
	ultrasonic = None
	keyboard = None
	activate_key = None
	deactivate_key = None
	def __init__(self, echo_pin=17, trigger_pin=4, max_dist=2, threshold_dist=1, activate_key=' ', deactivate_key='h'):
		self.ultrasonic = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=max_dist, threshold_distance=threshold_dist)
		self.ultrasonic.when_in_range = self.__activate_mirror
		self.ultrasonic.when_out_of_range = self.__deactivate_mirror
		self.keyboard = Controller()
		self.activate_key = activate_key
		self.deactivate_key = deactivate_key
	def __activate_mirror(self):
		print("Mirror Activated")
		self.keyboard.press(self.activate_key)
		self.keyboard.release(self.activate_key)
	def __deactivate_mirror(self):
		print("Mirror Deactivated")
		self.keyboard.press(self.deactivate_key)
		self.keyboard.release(self.deactivate_key)
	@classmethod
	def init_from_json(jsonFileName="config.json"):
		print("Initializing from " + jsonFileName)
		


pd = PersonDetector()

# while True:
# 	print(ultrasonic.distance)
#	time.sleep(1)
