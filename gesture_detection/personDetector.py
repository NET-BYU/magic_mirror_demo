from gpiozero import DistanceSensor
import time
import pynput

# TODO - (1) Simulate keypresses (2) Read from a config.json file to allow configuration

def activate_mirror():
	print("Mirror Activated")

def deactivate_mirror():
	print("Mirror Deactivated")

ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=2, threshold_distance=1)
ultrasonic.when_in_range = activate_mirror
ultrasonic.when_out_of_range = deactivate_mirror

while True:
	print(ultrasonic.distance)
	time.sleep(1)
