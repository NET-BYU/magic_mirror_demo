###########################
# Author: Maximilian Warner
# Company: BYU
# Project: Magic Mirror
# Created 8/2/19
###########################
import paho.mqtt.publish as publish
import json
import random
import time

with open('/home/maw276/magic_mirror_demo/messages/quote/quotes_list.txt') as json_file:
   quotes = json.load(json_file)
   random_quote_index = random.randint(0, len(quotes) - 1)

   # format string to json 
   theQuote = json.dumps(quotes[random_quote_index])

   # publish quote to MQTT broker
   publish.single(
       "immerse/quote",
       theQuote,
       hostname="postman.cloudmqtt.com",
       port=27408,
       retain=True,
       qos=1,
       auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
       tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
   )
