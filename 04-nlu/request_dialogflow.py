#!/usr/bin/python
# -*- coding: utf8 -*-

import sys 
try:
    reload         # Python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:  # Python 3
    from importlib import reload

import urllib
import uuid
import json
import requests

query = sys.argv[1]
lang = 'zh-tw'
session_id = str( uuid.uuid1() )
timezone = 'Asia/Taipei'
authorization = '<FIXME>'

headers = {
    "accept": "application/json",
    "authorization": authorization
}

url = 'https://api.dialogflow.com/v1/query?v=20170712'
params = {'query':str(query), 'lang':lang, 'sessionId': session_id, 'timezone': timezone}

response = requests.request("GET", url, headers=headers, params=params)
data = json.loads(response.text)

print(data)

status = data['status']['code']
print("Status: {}".format(status))

if status == 200:
    resolveQuery = data['result']['resolvedQuery']
    fulfillment = data['result']['fulfillment']['speech']

    print("Query: {}".format(resolveQuery))
    print("Response: {}".format(fulfillment))

