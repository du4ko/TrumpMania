import requests
from bson import json_util

def dl_json_(url):
    response = requests.get(url)
    data = json_util.loads(response.text)
    return data