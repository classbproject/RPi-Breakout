import time
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM) #BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)

in4 = 4
in14 = 14
in15 = 15
in7 = 7
in21 = 21
in20 = 20
in19 = 19
in13 = 13
in12 = 12

GPIO.setup(in4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print "*~*~* Start testing GPIO inputs *~*~*"
print ""

print "Waiting for input on GPIO4"
while GPIO.input(in4) == False:
	time.sleep(0.1)
print "Input on GPIO 4 detected"

print ""
print "Waiting for input on GPIO14"
while GPIO.input(in14) == False:
	time.sleep(0.1)
print "Input on GPIO 14 detected"

print ""
print "Waiting for input on GPIO15"
while GPIO.input(in15) == False:
	time.sleep(0.1)
print "Input on GPIO 15 detected"

print ""
print "Waiting for input on GPIO7"
while GPIO.input(in7) == False:
	time.sleep(0.1)
print "Input on GPIO 7 detected"

print ""
print "Waiting for input on GPIO21"
while GPIO.input(in21) == False:
	time.sleep(0.1)
print "Input on GPIO 21 detected"

print ""
print "Waiting for input on GPIO20"
while GPIO.input(in20) == False:
	time.sleep(0.1)
print "Input on GPIO 20 detected"

print ""
print "Waiting for input on GPIO19"
while GPIO.input(in19) == False:
	time.sleep(0.1)
print "Input on GPIO 19 detected"

print ""
print "Waiting for input on GPIO13"
while GPIO.input(in13) == False:
	time.sleep(0.1)
print "Input on GPIO 13 detected"

print ""
print "Waiting for input on GPIO12"
while GPIO.input(in12) == False:
	time.sleep(0.1)
print "Input on GPIO 12 detected"

print ""
print "Finished testing inputs!"
print ""

GPIO.cleanup()
