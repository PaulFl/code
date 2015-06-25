#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
import time

port = 2001
pin = 8
state = False
pastTime = time.time()
stateFile = open("/sys/class/gpio/gpio8/value", "r")

def gpio_callback(gpio_id, val):
	if (val == 0 and time.time() - pastTime >= 0.25):
		global pastTime
		global state
		stateFile.seek(0)
		state = bool(int(stateFile.read().rstrip()))
		state = not state
		RPIO.output(pin, state)
		print("Switched:", state)
		pastTime = time.time()

def socket_callback(socket, message):
	message = str(message)
	action = int(message[2])
	print(action)
	if (action == 1):
		RPIO.output(8, True)
	elif (action == 2):
		RPIO.output(8, False)
	elif (action == 3):
		RPIO.output(7, True)
	elif (action == 4):
		RPIO.output(7, False)

RPIO.setup(pin, RPIO.OUT)
RPIO.setup(7, RPIO.OUT)
RPIO.output(7, False)
RPIO.output(pin, False)
RPIO.add_interrupt_callback(9, gpio_callback, pull_up_down=RPIO.PUD_UP)
RPIO.add_tcp_callback(port, socket_callback)
print("Server started")
RPIO.wait_for_interrupts()
RPIO.cleanup()
