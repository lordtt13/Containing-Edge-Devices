import json
import signal
import time

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

import dht11

# Define all the Constants
MQTT_TOPIC = "threshold"

# Initialize GPIOs of Raspi
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
    # Initialize all the modules connected to RPI here
    dht11Module = dht11.DHT11(pin=17)

    # MQTT server init
    client = mqtt.Client()

    client.connect("127.0.0.1", 1883, 60)


    def shutdown(signal_num, frame):
        print("Shutting down publisher")
        client.publish(MQTT_TOPIC, "Q")
        client.disconnect()
        GPIO.cleanup()
        exit()


    signal.signal(signal.SIGINT, shutdown)

    while True:
        # Collect all the modules data here
        dht11_result = dht11Module.read()

        data_dict = {"Temperature": 0, "Humidity": 0}

        if dht11_result.is_valid():
            data_dict["Temperature"] = dht11_result.temperature
            data_dict["Humidity"] = dht11_result.humidity
	    print(data_dict)
   	    data_json = json.dumps(data_dict, indent=4)
            client.publish(MQTT_TOPIC, data_json)

        else:
            print("Error: %d" % dht11_result.error_code)
            client.publish(MQTT_TOPIC, "crit");

        time.sleep(0.8)
