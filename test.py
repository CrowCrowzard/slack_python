#!/usr/bin/env python3
# coding: UTF-8

import requests
import key

payload = {
    "token" : key.TOKEN,
    "pretty" : "1"
}

url = "https://slack.com/api/auth.test"

res = requests.post(url, params=payload)

print (res.text)
