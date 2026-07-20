import asyncio
from helpers.login import ReolinkLogin
from helpers.event_stream import EventStream
from helpers.mqtt_forwarder import MQTTForwarder

async def async_setup(app):
    cfg = app.config

    login = ReolinkLogin(
        host=cfg["camera_host"],
        user=cfg["camera_user"],
        password=cfg["camera_pass"]
    )

    token = login.get_token()

    mqtt = MQTTForwarder(
        host=cfg["mqtt_host"],
        user=cfg["mqtt_user"],
        password=cfg["mqtt_pass"]
    )

    stream = EventStream(
        host=cfg["camera_host"],
        token=token,
        callback=mqtt.forward_event
    )

    asyncio.create_task(stream.run())

    return True
