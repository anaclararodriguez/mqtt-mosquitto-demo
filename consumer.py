from paho.mqtt.client import MQTTMessage, Client as MQTTClient

def on_connect(client, userdata, flags, tc):
    print("Mqtt connected, listening for messages... ")
    client.subscribe("topic")

def on_message(client, userdata, messgae: MQTTMessage):
    print("Message received: " + str(messgae.payload.decode()))

client = MQTTClient()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()