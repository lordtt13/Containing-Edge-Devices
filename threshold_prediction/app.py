# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:35:59 2020

@author: Tanmay Thakur
"""
import pickle
import decimal

import numpy as np
import paho.mqtt as mqtt
import json

from parametrizing import threshold

MQTT_TOPIC = "threshold"


def append_new(data, point):
    data.append(point)
    return data.pop(0)


def on_connect(client):
    print("Connected to the MQTT server")
    client.subscribe(MQTT_TOPIC)


def on_message_recieve(client, _, msg):
    if msg.payload == 'Q':
        client.disconnect();
        print("Modules disconnected");
    elif msg.payload == 'crit':
        print("Critical condition due to sensor errors")
        client.disconnect();
    else:
        data = json.loads(msg,parse_float=decimal.Decimal,parse_int=integer)
        process(data)

def process(dict_new):
    data_temp, data_humid = pickle.load(open("data_temp.pickle", "rb")), \
                            pickle.load(open("data_humid.pickle", "rb"))
    for key, value in dict_new.items():
        if (key == "Temperature"):
            append_new(data_temp, value)
            pickle_out = open("./data_temp.pickle", "wb")
            pickle.dump(data_temp, pickle_out)
            pickle_out.close()
            print(threshold(data_temp, np.mean(data_temp), 0.75))
        else:
            append_new(data_humid, value)
            pickle_out = open("data_humid.pickle", "wb")
            pickle.dump(data_humid, pickle_out)
            pickle_out.close()
            print(threshold(data_humid, np.mean(data_humid), 0.75))


if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)

    client.on_connect = on_connect
    client.on_message = on_message_recieve

    client.loop_forever()
