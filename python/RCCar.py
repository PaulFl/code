#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
from RPIO import PWM
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
port = 2002
led = 8
servoPin = 20
motorSpeed = 26
motor1 = 19
motor2 = 16
RPIO.setup(led, RPIO.OUT)
RPIO.setup(motor1, RPIO.OUT)
RPIO.setup(motor2, RPIO.OUT)
GPIO.setup(motorSpeed, RPIO.OUT)
servo = PWM.Servo()
motor = GPIO.PWM(motorSpeed, 100)
servo.set_servo(servoPin, 1200)
motor.start(0)

def socket_callback(socket, message):
	message = message.decode("utf-8")
	array = list(message)
	print (message)
	if (array[8] == 'L'):
		light = (array[16] == '1')
		RPIO.output(led, light)
	elif (array[8] == 'D'):
		value = ""
		value += str(array[16])
		for x in range(17, len(array)):
			if (array[x].isdigit()):
				value += str(array[x])
		intValue = int(value)
		if (intValue < 100 and intValue > -100):
			intValue += 100
			intValue *= 9
			intValue += 300
			intValue = int(round(float(intValue), -1))
			servo.set_servo(servoPin, intValue)

	elif (array[8] == 'M'):
		value = ""
		value += str(array[16])
		for x in range(17, len(array)):
			if (array[x].isdigit()):
				value += str(array[x])
		intValue = int(value)
		if (intValue < 100 and intValue > -100):
			if (intValue < -20):
				RPIO.output(motor1, RPIO.HIGH)
				RPIO.output(motor2, RPIO.LOW)
				motor.ChangeDutyCycle(-intValue)
			elif (intValue > 20):
				RPIO.output(motor1, RPIO.LOW)
				RPIO.output(motor2, RPIO.HIGH)
				motor.ChangeDutyCycle(intValue)
			else:
				motor.ChangeDutyCycle(0)

RPIO.add_tcp_callback(port, socket_callback)
print("Server started")
RPIO.wait_for_interrupts()
servo.stop_servo(servoPin)
motor.stop()
RPIO.cleanup()
