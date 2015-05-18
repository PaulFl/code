#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
import time
import os


button=
pastTime = time.time()

RPIO.add_interrupt_callback(button, gpio_callback, pull_up_down=RPIO.PUD_UP)
RPIO.wait_for_interrupts()
RPIO.cleanup()

def gpio_callback(gpio_id, val):
	if (val == 0 and time.time() - pastTime >= 0.25):
		global pastTime
		global state
		pastTime = time.time()
		os.system("shutdown -h now")
		RPIO.stop_waiting_for_interrupts()
