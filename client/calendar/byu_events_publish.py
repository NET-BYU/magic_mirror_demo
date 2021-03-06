import requests
import json
import datetime
import paho.mqtt.client as mqtt
import ssl
import calendar

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
endDate = datetime.datetime.now() + datetime.timedelta(days=20)
n = endDate.strftime("%Y-%m-%d")

res = requests.get('https://calendar.byu.edu/api/Events.json?categories=all&event[min][date]='+ today +'&event[max][date]='+ n)
j = json.loads(res.text)

u = "messages"
pa = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
h = "postman.cloudmqtt.com"
p = 27408
l = [0,1,2,3]

client = mqtt.Client()
client.username_pw_set(u, password = pa)
client.tls_set(ca_certs = r"C:\Users\levey\OneDrive\Documents\ca.crt")
client.connect(h,p,keepalive=60,bind_address="")

def formatDate(time):
    newtime = time[:16]
    hour = newtime[11] + newtime[12]
    if(int(hour) >= 12 and int(hour) != 24):
        newtime = newtime + " p.m."
    else:
        newtime = newtime + " a.m."
    if(int(hour) > 12):
        hour = int(hour) - 12
        ho = str(hour)
        if len(ho) == 1:
            ho = "0" + ho
        s = list(newtime)
        s[11] = ho[0]
        s[12] = ho[1]
        newtime = "".join(s)
    year = int(newtime[0:4])
    month = int(newtime[5:7])
    day = int(newtime[8:10])
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    months = ("temp.","Jan.","Feb.","Mar.","Apr.","May.","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec.")
    dateFormated = datetime.date(year,month,day)
    weekInd = dateFormated.weekday()
    dayOfWeek = weekDays[weekInd]
    monthFormatted = months[month]
    newtime = dayOfWeek + ", " + monthFormatted + " " + str(day)
    return newtime
m = "["
for i in l:
    m += "{\"Title\""
    m += " : \""
    m += j[i]["Title"]
    m += "\", \"Time\" : \""
    time = j[i]["StartDateTime"]
    m += formatDate(time)
    m += "\", \"Location\" : \""
    b = j[i]["LocationName"]
    if(b is None):
        m += "null"
    else:
        m += j[i]["LocationName"]
    if (i == l[-1]):
        m += "\"}"
    else:    
        m += "\"}, "
m += "]"
t = "immerse/event"
client.publish(t,m,qos=1,retain=True)



