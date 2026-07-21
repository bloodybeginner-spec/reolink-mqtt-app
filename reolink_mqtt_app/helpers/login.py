import requests
import json
import sys

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

payload = [
    {
        "cmd": "Login",
        "param": {
            "User": user,
            "Password": password
        }
    }
]

r = requests.post(
    f"http://{host}/cgi-bin/api.cgi",
    json=payload,
    timeout=5
)

data = r.json()[0]["value"]
token = data["token"]
session = data["sessionId"]

with open("/token.json", "w") as f:
    json.dump({"token": token, "session": session}, f)
