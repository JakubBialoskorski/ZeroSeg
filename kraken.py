#!/usr/bin/env python
import requests
import ZeroSeg.led as led
import krakenex

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

k = krakenex.API()
k.load_key('kraken.key')
print(k.query_private('Balance')["result"]["ZEUR"])