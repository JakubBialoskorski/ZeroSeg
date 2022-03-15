#!/usr/bin/env python
import requests
import ZeroSeg.led as led
import krakenex

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

k = krakenex.API(key="YOUR_KEY", secret="YOUR_SECRET")
device.write_text(1, k.query_private('Balance')["result"]["ZEUR"][:5])