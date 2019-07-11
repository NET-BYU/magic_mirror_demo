# ############################################################################################################################
# # Quote API Option 1 favqs.com
#
# import paho.mqtt.publish as publish
# import urllib.request
# import json
# import time
#
# # controls how many quotes are publish (for each run of this file)
# # quote_cnt = 0
# # while quote_cnt < 5:
#
# # url of the daily quote
# the_url = 'https://favqs.com/api/qotd'
# # json object should be returned by the url
# json_obj = urllib.request.urlopen(the_url)
# # json dictionary??
# data = json.load(json_obj)
# # Gets the quote info and formats it
# quote = (data['quote'])
# quote_text = (quote['body'])
# author = (quote['author'])
# formatted_quote = "\"{0}\" - {1}".format(quote_text, author)
#
# # publish quote to MQTT broker
# publish.single(
#     "immerse/quote/text",  # broker and topic
#     quote_text,  # data (the quote)
#     # broker access information
#     hostname="postman.cloudmqtt.com", # address??
#     port=27408,
#     auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
#     tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
# )
#
# publish.single(
#     "immerse/quote/author",  # broker and topic
#     author,  # data (the quote)
#     # broker access information
#     hostname="postman.cloudmqtt.com", # address??
#     port=27408,
#     auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
#     tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
# )
#
#     # # time between publishing each quote
#     # time.sleep(5)
#     # quote_cnt += 1
# ##########################################################################################################################
# Quote API Option 2 brainyquote.com
import paho.mqtt.publish as publish
import requests
import xmltodict
import time


brainy_quote_url = 'https://www.brainyquote.com/link/quotefu.rss'
data = requests.get(brainy_quote_url)
xpars = xmltodict.parse(data.text)

rssFeed = (xpars['rss'])
channel = (rssFeed['channel'])
item = (channel['item'])
author = (item[0]['title'])
quote_text = (item[0]['description'])

# publish quote to MQTT broker
publish.single(
    "immerse/quote/text",  # broker and topic
    quote_text,  # data (the quote)
    # broker access information
    hostname="postman.cloudmqtt.com", # address??
    port=27408,
    auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
    tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
)

publish.single(
    "immerse/quote/author",  # broker and topic
    author,  # data (the quote)
    # broker access information
    hostname="postman.cloudmqtt.com", # address??
    port=27408,
    auth={"username": "messages", "password": "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"},
    tls={"ca_certs": "/home/maw276/magic_mirror_demo/messages/quote/ca.crt"},
)
