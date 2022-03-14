#!/usr/bin/env python
import requests
import ZeroSeg.led as led

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
device.write_text(1, data["bpi"]["USD"]["rate"][:8])
