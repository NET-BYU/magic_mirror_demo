import requests
import json
import datetime
import paho.mqtt.client as mqtt
import ssl
import calendar

#gets today's date and the date 3 days from now
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
endDate = datetime.datetime.now() + datetime.timedelta(days=3)
n = endDate.strftime("%Y-%m-%d")

#gets the json data from BYU's calendar api
res = requests.get('https://calendar.byu.edu/api/Events.json?categories=all&event[min][date]='+ today +'&event[max][date]='+ n)
j = json.loads(res.text)

#information for mqtt broker
u = "messages"
pa = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
h = "postman.cloudmqtt.com"
p = 27408
l = {0,1,2,3}

#creates mqtt client
client = mqtt.Client()
client.username_pw_set(u, password = pa)
client.tls_set(ca_certs =r"") #INSERT PATH TO CA.CRT FILE
client.connect(h,p,keepalive=60,bind_address="")

#function that formats a date into DAYOFWEEK, MONTH. DAY 
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
    months = ("Jan.","Feb.","Mar.","Apr.","May.","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec.")
    dateFormated = datetime.date(year,month,day)
    weekInd = dateFormated.weekday()
    dayOfWeek = weekDays[weekInd]
    monthFormatted = months[month]
    newtime = dayOfWeek + ", " + monthFormatted + " " + str(day)
    return newtime

#publishes the next four events under topics immerse/events/title,date,location/EVENTNUMBER
for i in l:
    t = "immerse/event/title/"+str(i)
    m = j[i]["Title"]
    client.publish(t,m,qos=1,retain=True)
    time = j[i]["StartDateTime"]
    t = "immerse/event/date/"+str(i)
    m = formatDate(time)
    client.publish(t,m,qos=1,retain=True)
    t = "immerse/event/location/"+str(i)
    m = j[i]["LocationName"]
    client.publish(t,m,qos=1,retain=True)




