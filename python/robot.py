#!/usr/bin/env python3
#! -*- encoding:Utf-8 -*-

import RPIO
from RPIO import PWM
import time
import RPi.GPIO as GPIO
import random
import atexit

random.seed()
GPIO.setmode(GPIO.BCM)
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
servo.set_servo(servoPin, 1300)
motor.start(0)
button = 27 
pastTime = time.time()
atexit.register(RPIO.output, motor1, RPIO.LOW)
atexit.register(RPIO.output, motor2, RPIO.LOW)

def gpio_callback(gpio_id, val):
	if (val == 0 and time.time() - pastTime >= 0.25):
		RPIO.output(led, RPIO.HIGH)
		global pastTime
		pastTime = time.time()
		RPIO.output(motor2, RPIO.HIGH)
		RPIO.output(motor1, RPIO.LOW)
		motor.ChangeDutyCycle(10)
		time.sleep(0.5)
		motor.ChangeDutyCycle(30)
		time.sleep(0.5)
		motor.ChangeDutyCycle(50)
		time.sleep(0.5)
		motor.ChangeDutyCycle(80)
		time.sleep(2)
		while True:
			randomDirection = int(random.uniform(200, 2200))
			if (randomDirection < 700 or randomDirection > 1700):
				break
		randomDirection = int(round(float(randomDirection), -1))
		servo.set_servo(servoPin, randomDirection)
		motor.ChangeDutyCycle(100)
		time.sleep(float(random.uniform(2, 5)))
		motor.ChangeDutyCycle(30)
		servo.set_servo(servoPin, 1300)
		RPIO.output(motor1, RPIO.HIGH)
		RPIO.output(motor2, RPIO.LOW)
		RPIO.output(led, RPIO.LOW)
		time.sleep(0.4)
		motor.ChangeDutyCycle(10)
		time.sleep(0.5)
		motor.ChangeDutyCycle(30)
		time.sleep(0.5)
		motor.ChangeDutyCycle(50)
		time.sleep(0.5)
		motor.ChangeDutyCycle(100)


RPIO.add_interrupt_callback(button, gpio_callback, pull_up_down=RPIO.PUD_UP)
RPIO.wait_for_interrupts()
RPIO.cleanup()
