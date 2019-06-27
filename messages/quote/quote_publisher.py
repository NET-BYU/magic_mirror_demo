import paho.mqtt.publish as publish
import urllib.request
import json
import time

# controls how many quotes are publish (for each run of this file)
# quote_cnt = 0
# while quote_cnt < 5:

# url of the daily quote
the_url = 'https://favqs.com/api/qotd'
# json object should be returned by the url
json_obj = urllib.request.urlopen(the_url)
# json dictionary??
data = json.load(json_obj)
# Gets the quote info and formats it
quote = (data['quote'])
quote_text = (quote['body'])
author = (quote['author'])
formatted_quote = "\"{0}\" - {1}".format(quote_text, author)

# publish quote to MQTT broker
publish.single(
    "immerse/test",  # broker and topic
    formatted_quote,  # data (the quote)
    # broker access information
    hostname="postman.cloudmqtt.com", # address??
    port=27408,
    auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
    tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
)

    # # time between publishing each quote
    # time.sleep(5)
    # quote_cnt += 1
