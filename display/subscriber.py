import paho.mqtt.subscribe as subscribe


def receive_msg(client, user_data, msg):
    for data in user_data:
        data.update(msg.topic, msg.payload)


def run(data_list):
    broker_address = "postman.cloudmqtt.com"
    password = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
    username = "messages"
    port = 27408
    ssl_certificate = r"/home/christopolise/devel/SmartMirrorGUI/ca.crt"
    subscribe.callback(receive_msg, "immerse/#", userdata=data_list, hostname=broker_address, port=port,
                       auth={'username': username, 'password': password}, tls={'ca_certs': ssl_certificate})


if __name__ == '__main__':
    run()
