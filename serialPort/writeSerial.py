#!/usr/bin/python
# -*-coding:Utf-8 -*

import serial
import time
import psutil

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
	cpu = str(int(psutil.cpu_percent()))
	ser.write(cpu)
	ser.write('\n')
	print cpu
	time.sleep(1)
