#!/usr/bin/with-contenv bashio

CAMERA_HOST=$(bashio::config 'camera_host')
CAMERA_USER=$(bashio::config 'camera_user')
CAMERA_PASS=$(bashio::config 'camera_pass')

MQTT_HOST=$(bashio::config 'mqtt_host')
MQTT_USER=$(bashio::config 'mqtt_user')
MQTT_PASS=$(bashio::config 'mqtt_pass')

python3 /login.py "$CAMERA_HOST" "$CAMERA_USER" "$CAMERA_PASS" &
python3 /event_stream.py "$CAMERA_HOST" &
python3 /mqtt_forwarder.py "$MQTT_HOST" "$MQTT_USER" "$MQTT_PASS"
