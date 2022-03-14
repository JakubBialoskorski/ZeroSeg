#!/usr/bin/env python

import time, requests, alpha_vantage, json, urllib
import ZeroSeg.led as led
from datetime import datetime

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

def how_rich():
    API_URL = "https://www.alphavantage.co/query"
    symbols = ['TICKER_SYMBOL_HERE']
    for symbol in symbols:
        data = { "function": "GLOBAL_QUOTE",
                 "symbol": symbol,
                 "datatype": "json",
                 "apikey": "YOUR_API_KEY" }
        response = requests.get(API_URL, data)
        data = response.json()
        output = data["Global Quote"]["05. price"]
        how_rich = float(output) * NUMBER_OF_STOCKS_HERE
        device.write_text(1, str(how_rich))

how_rich()
