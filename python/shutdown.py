#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
import time
import os


button=20
pastTime = time.time()

def gpio_callback(gpio_id, val):
	if (val == 0 and time.time() - pastTime >= 0.25):
		global pastTime
		global state
		pastTime = time.time()
		os.system("/sbin/shutdown -h now")
		RPIO.stop_waiting_for_interrupts()

RPIO.add_interrupt_callback(button, gpio_callback, pull_up_down=RPIO.PUD_UP)
RPIO.wait_for_interrupts()
RPIO.cleanup()
