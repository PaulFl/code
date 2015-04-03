#!/usr/bin/env python3
#! -*-endoding: Utf-8-*-

import time
import RPIO

timeout = 10000
total = 0
DEBUG = 0
stateFile = open("/sys/class/gpio/gpio8/value", "r")
pin = 8
RPIO.setup(pin, RPIO.OUT)

def CapRead(inPin,outPin):
    total = 0
    
    # set Send Pin Register low
    RPIO.setup(outPin, RPIO.OUT)
    RPIO.output(outPin, RPIO.LOW)
    
    # set receivePin Register low to make sure pullups are off 
    RPIO.setup(inPin, RPIO.OUT)
    RPIO.output(inPin, RPIO.LOW)
    RPIO.setup(inPin, RPIO.IN)
    
    # set send Pin High
    RPIO.output(outPin, RPIO.HIGH)
    
    # while receive pin is LOW AND total is positive value
    while( RPIO.input(inPin) == RPIO.LOW and total < timeout ):
        total+=1
    
    if ( total > timeout ):
        return -2 # total variable over timeout
        
     # set receive pin HIGH briefly to charge up fully - because the while loop above will exit when pin is ~ 2.5V 
    RPIO.setup( inPin, RPIO.OUT )
    RPIO.output( inPin, RPIO.HIGH )
    RPIO.setup( inPin, RPIO.IN )
    
    # set send Pin LOW
    RPIO.output( outPin, RPIO.LOW ) 

    # while receive pin is HIGH  AND total is less than timeout
    while (RPIO.input(inPin)==RPIO.HIGH and total < timeout) :
        total+=1
    
    if ( total >= timeout ):
        return -2
    else:
        return total


# loop
while True:
	total = 0
	for j in range(0,20):
		total += CapRead( 17 , 18 );
	#print(total)
	if (total > 1900):
		stateFile.seek(0)
		state = bool(int(stateFile.read().rstrip()))
		if (state):
			state = False
			RPIO.output(pin, state)
			time.sleep(0.5)
	if (total > 4000):
		stateFile.seek(0)
		state = bool(int(stateFile.read().rstrip()))
		if (not state):
			state = True
			RPIO.output(pin, state)
			time.sleep(0.5)
	#print(state)
	time.sleep(0.04)

# clean before you leave
GPIO.cleanup()
