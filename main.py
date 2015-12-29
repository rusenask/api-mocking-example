#!/usr/bin/env python
import requests
from pprint import pprint as pp
import os

KEY = os.environ.get("APIKEY")


def get_weather(city):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + KEY
        response = requests.get(url)
        results = {"headers": response.headers,
                   "body": response.json()}
        pp(results)
        return results
    except Exception as ex:
        print("Got error when querying weather API: %s" % ex)


if __name__ == "__main__":
    get_weather("London")
