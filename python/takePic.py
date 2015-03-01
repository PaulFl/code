#!/usr/bin/env python3
#! -*-endoding: Utf-8-*-

import time
import RPIO

camera = 20

RPIO.setup(camera, RPIO.OUT)
RPIO.output(camera, RPIO.LOW)

RPIO.output(camera, RPIO.HIGH)
time.sleep(0.5)
RPIO.output(camera, RPIO.LOW)
