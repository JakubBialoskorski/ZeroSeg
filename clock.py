#!/usr/bin/env python
import ZeroSeg.led as led
import time
from datetime import datetime

def clock(device, deviceId, seconds):

    for _ in xrange(seconds):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        dot = second % 2 == 0 # calculate blinking dot
        # Set hours
        device.letter(deviceId, 6, int(hour / 10)) # Tens
        device.letter(deviceId, 5, hour % 10, dot) # Ones
        # Set minutes
        device.letter(deviceId, 4, "-")
        device.letter(deviceId, 3, int(minute / 10)) # Tens
        device.letter(deviceId, 2, minute % 10, dot) # Ones
        # Set SECONDS
        #        device.letter(deviceId, 2, int(second / 10)) # Tens
        #        device.letter(deviceId, 1, second % 10) # Ones
        time.sleep(1)

device = led.sevensegment(cascaded=2)
level = 1
device.brightness(level)

while True:
    clock(device, 1, seconds=10)