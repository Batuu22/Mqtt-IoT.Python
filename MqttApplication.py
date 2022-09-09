from paho.mqtt import client as mqtt
import time

BROKER_NAME = "test.mosquitto.org"
PORT = 1883
TOPIC_PUB = "topic/pub"
TOPIC_SUB = "topic/sub"
fConnected = False


def on_connect(client,userdata,flags,rc):

    print(rc)

    if rc == 0:
        print("Client connected to Broker")
        global fConnected
        fConnected = True



def on_message(client,userdata,msg):

    print(msg.topic)
    print(msg.payload.decode("utf-8"))


def on_publish(client,userdata,msg):

    print("Message Published")




client = mqtt.Client("MQTT")

client.on_connect = on_connect

client.on_message = on_message

client.on_publish = on_publish

client.connect(BROKER_NAME,PORT)

client.loop_start()

while(fConnected != True):

    time.sleep(1)


client.subscribe(TOPIC_SUB)

while(True):

    time.sleep(1)

    keyInput = input()

    if keyInput != 'quit':

        client.publish(TOPIC_PUB,keyInput)
        print(keyInput)

    else :

        client.loop_stop()
        print("End the Program")
        break

    keyInput = ""

    



