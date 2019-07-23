import time
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM) #BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)

mosfet = 22

GPIO.setup(mosfet,GPIO.OUT)

print "*~*~* Start testing MOSFET *~*~*"
print ""

print "MOSFET on"
GPIO.output(mosfet,GPIO.HIGH)
time.sleep(1)
print "MOSFET off"
GPIO.output(mosfet,GPIO.LOW)

print ""
print "Finished testing MOSFET!"
print ""

GPIO.cleanup()
