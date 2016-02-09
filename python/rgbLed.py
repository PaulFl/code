#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
from RPIO import PWM
import time
import RPi.GPIO as GPIO
import random

random.seed()
GPIO.setmode(GPIO.BCM)

frequency = 200
speed = 0.05
delay = 1

rPin = 13;
gPin = 19
bPin = 26
GPIO.setup(rPin, RPIO.OUT)
GPIO.setup(gPin, RPIO.OUT)
GPIO.setup(bPin, RPIO.OUT)

red = GPIO.PWM(rPin, frequency)
green = GPIO.PWM(gPin, frequency)
blue = GPIO.PWM(bPin, frequency)

red.start(0)
green.start(0)
blue.start(0)

newBlue = 0
newRed = 0
newGreen = 0

blueValue = 0
greenValue = 0
redValue = 0

while True:
	color = random.randrange(6)

	if color == 0:
		newBlue = 100
		newGreen = 0
		newRed= 0
	elif color == 1:
		newBlue = 0
		newGreen = 100
		newRed = 0
	elif color == 2:
		newBlue = 0
		newGreen = 0
		newRed = 100
	elif color == 3:
		newBlue = 100
		newGreen = 100
		newRed = 0
	elif color == 4:
		newBlue = 0
		newGreen = 100
		newRed = 100
	elif color == 5:
		newBlue = 100
		newGreen = 0
		newRed = 100

	while newBlue != blueValue or newGreen != greenValue or newRed != redValue:
		if blueValue > newBlue:
			blueValue -= 1
		elif blueValue < newBlue:
			blueValue += 1
		if greenValue > newGreen:
			greenValue -= 1
		elif greenValue < newGreen:
			greenValue += 1
		if redValue > newRed:
			redValue -= 1
		elif redValue < newRed:
			redValue += 1

		red.ChangeDutyCycle(redValue)
		green.ChangeDutyCycle(greenValue)
		blue.ChangeDutyCycle(blueValue)
		
		time.sleep(speed)

	time.sleep(delay)
