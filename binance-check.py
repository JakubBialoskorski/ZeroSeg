#!/usr/bin/env python
import requests
import ZeroSeg.led as led
from binance.client import Client

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

client = Client("YOUR_KEY", "YOUR_SECRET")
balance = client.get_asset_balance(asset='USDT')["free"][:5]
device.write_text(1, balance)