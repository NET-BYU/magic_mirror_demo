# Person Detector
This module detects when a person approaches the Magic Mirror, then simulates a key press to alert the mirror when a person approaches and another key press when a person hasn't been detected in a while. It is assumed that the mirror will go to the Home Screen when a person approaches and a Blank Screen when the person leaves.
This module runs independently from all other code running on the Raspberry Pi. It uses the HC-SR04 Proximity Sensor connected to a Raspberry Pi. It requires systemd, which is included in the Raspbian operating system by default.

## Quickstart
(TODO add later)

## Software Configurations
All configurations should be saved in the file config.json. If no config file exists, then the default configurations will be used. An example config file with the default configurations is included.
Here is a list of all keys, and what their values do:

**max_distance** - Default is 2 meters. After anything moves beyond this range, or nothing is detected, the sensor will default the measurement to this value. 

**threshold_distance** - Default is 1 meter. This means that when something moves within the threshold distance, the *Person Detected* event will be triggered (activating the mirror). When a person or object leaves the threshold, a *Person No Longer Detected* event will be triggered (activating the mirror if a person isn't detected for a certain amount of time).

**time_before_sleep** - Default is 10 seconds. When a *Person No Longer Detected* event is triggered, a timer will be set to this value and begin to count down. If the timer reaches 0 before a *Person Detected* event happens, then the mirror will switch to a blank screen. 

## Hardware Assembly
Requirements:
 * 1 Raspberry Pi (The same one running the Magic Mirror Display)
 * 1 HC-SR04 Proximity Sensor
 * 1 330 Ohm Resistor
 * 1 470 Ohm Resistor
 * Additional hardware requirements depend on which of 2 methods you choose, see "Method 1: Breadboard and jumpers" or "Method 2: The custom Raspberry Pi Hat".


The default configurations of the hardware are ("----" represents a connecting wire):
 * ProxSensor Vcc Pin ---- RasPi 5V (Can use Pin # 02)
 * ProxSensor Trig Pin ---- RasPi GPIO4 (Pin # 07)
 * ProxSensor Echo Pin ---- 330 Ohm Resistor ---- RasPi GPIO17 (Pin # 11) ---- 470 Ohm Resistor --- RasPi GND (Can use Pin # 09)
 * ProxSensor GND Pin --- RasPi GND (Can use Pin # 06)

For a graphical explanation of how everything connects, see "Method 1: Breadboard and jumpers" or "Method 2: The custom Raspberry Pi Hat"

### Method 1: Breadboard and jumpers
We use the same configuration as shown on the following raspberry pi project page:

![Proximity Sensor Schematic](images/wiring-uds.png)

https://projects.raspberrypi.org/en/projects/physical-computing/13

### Method 2: The custom Raspberry Pi Hat
(TODO finish later) You need a 3cmx7cm protoboard, a 