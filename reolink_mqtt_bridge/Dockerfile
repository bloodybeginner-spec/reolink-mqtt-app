FROM python:3.11-slim

RUN pip install requests paho-mqtt

COPY run.sh /run.sh
COPY login.py /login.py
COPY event_stream.py /event_stream.py
COPY mqtt_forwarder.py /mqtt_forwarder.py

RUN chmod +x /run.sh

CMD ["/run.sh"]
