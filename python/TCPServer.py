#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO

port = 1030

def socket_callback(socket, message):
	message = str(message)
	print(message)

RPIO.add_tcp_callback(port, socket_callback)
RPIO.wait_for_interrupts()
