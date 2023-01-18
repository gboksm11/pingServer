import requests
import json 
import threading
import os

def pingServer():
    threading.Timer(5, pingServer).start()
    res = requests.get(os.environ.get('SERVER'))
    response = json.loads(res.text)
    print(response)

pingServer()
