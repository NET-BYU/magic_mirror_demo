# Person Detector
This module detects when a person approaches the Magic Mirror, then simulates a key press to alert the mirror when a person approaches and another key press when a person hasn't been detected in a while. It is assumed that the mirror will go to the Home Screen when a person approaches and a Blank Screen when the person leaves.
This module runs independently from all other code running on the Raspberry Pi. It uses the HC-SR04 Proximity Sensor connected to a Raspberry Pi. 

## Quickstart
(TODO add later)

## Software Configurations
All configurations should be saved in the file config.json. If no config file exists, then the default configurations will be used. An example config file with the default configurations is included.
Here is a list of all keys, and what their values do:
"max_distance" - 

## Hardware Assembly
The default configurations of the hardware are:

ProxSensor Vcc Pin ---- RasPi 5V (Can use Pin # 02)

ProxSensor Trig Pin ---- RasPi GPIO4 (Pin # 07)

ProxSensor Echo Pin ---- 330 Ohm Resistor ---- RasPi GPIO17 (Pin # 11) ---- 470 Ohm Resistor --- RasPi GND (Can use Pin # 09)

ProxSensor GND Pin --- RasPi GND (Can use Pin # 06)

Our custom Raspberry Pi Hat uses this default schematic (TODO: Insert picture of hat). However, you can also simply use jumpers and a breadboard, then you can choose whichever pins are most convenient.

![Proximity Sensor Schematic](https://projects-static.raspberrypi.org/projects/physical-computing/5df9593a3ce6f0df1ad3c39a73c3434f7ee70481/en/images/wiring-uds.png)
https://projects.raspberrypi.org/en/projects/physical-computing/13

### The breadboard jumper method
(TODO add later)

### The custom Raspberry Pi Hat
(TODO finish later) You need a 3cmx7cm protoboard, a 