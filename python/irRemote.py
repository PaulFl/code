#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
import lirc

desktopLamp = 8
lamp = 7
stateFileDesktopLamp = open("/sys/class/gpio/gpio8/value", "r")
stateFileLamp = open("/sys/class/gpio/gpio7/value", "r")

RPIO.setup(desktopLamp, RPIO.OUT)
RPIO.setup(lamp, RPIO.OUT)
sockid = lirc.init("irRemote", blocking = True)

while True:
	code = lirc.nextcode()
	print(code)
	if (code == ['FlipDesktopLamp']):
		stateFileDesktopLamp.seek(0)
		RPIO.output(desktopLamp, not bool(int(stateFileDesktopLamp.read().rstrip())))
	elif (code == ['FlipLamp']):
		stateFileLamp.seek(0)
		RPIO.output(lamp, not 	bool(int(stateFileLamp.read().rstrip())))
