#!/usr/bin/env python3
# coding: UTF-8

import requests
import key

def main():
    payload = {
        "token" : key.token,
        "channel" : "#hogr",
        "text" : "Hello",
        "username" : "mybot",
        "pretty" : "1"
    }

    url = "https://slack.com/api/cht.postMessage"
    res = requests.post(url, params=payload)

    print (res)

if __name__ == '__main__':
    main()

