import json
import time
import sys
import paho.mqtt.client as mqtt

MQTT_HOST = sys.argv[1]
MQTT_USER = sys.argv[2]
MQTT_PASS = sys.argv[3]

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_HOST, 1883, 60)

DISCOVERY = {
    "person": "homeassistant/binary_sensor/reolink_person/config",
    "vehicle": "homeassistant/binary_sensor/reolink_vehicle/config",
    "pet": "homeassistant/binary_sensor/reolink_pet/config",
    "package": "homeassistant/binary_sensor/reolink_package/config"
}

for t, topic in DISCOVERY.items():
    payload = {
        "name": f"Reolink {t.capitalize()}",
        "state_topic": f"reolink/{t}",
        "device_class": "motion",
        "unique_id": f"reolink_{t}"
    }
    client.publish(topic, json.dumps(payload), retain=True)

while True:
    try:
        with open("/event.json") as f:
            event = json.load(f)

        if "value" in event and "type" in event["value"]:
            t = event["value"]["type"]
            client.publish(f"reolink/{t}", json.dumps(event))

    except:
        pass

    time.sleep(0.2)
