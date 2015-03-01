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
	global state
	stateFile.seek(0)
	state = bool(int(stateFile.read().rstrip()))
	message = str(message)
	message = message[len(message)-2]
	message = int(message)
	if (message != state):
		state = bool(message)
		RPIO.output(pin, state)
		print("Switched:", state)

RPIO.setup(pin, RPIO.OUT)
RPIO.output(pin, False)
RPIO.add_interrupt_callback(9, gpio_callback, pull_up_down=RPIO.PUD_UP)
RPIO.add_tcp_callback(port, socket_callback)
print("Server started")
RPIO.wait_for_interrupts()
RPIO.cleanup()
