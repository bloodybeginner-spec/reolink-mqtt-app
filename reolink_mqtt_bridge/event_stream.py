import requests
import json
import time
import sys

host = sys.argv[1]

while True:
    try:
        with open("/token.json") as f:
            token = json.load(f)["token"]

        url = f"http://{host}/cgi-bin/api.cgi?cmd=Subscribe&token={token}&channel=0"

        with requests.get(url, stream=True) as r:
            for line in r.iter_lines():
                if not line:
                    continue

                try:
                    event = json.loads(line.decode("utf-8"))
                except:
                    continue

                with open("/event.json", "w") as f:
                    json.dump(event, f)

    except Exception:
        time.sleep(2)
