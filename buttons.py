import time
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM) #BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)

button1 = 17
button2 = 18
button3 = 27

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print "*~*~* Starting button tests *~*~*"
print ""

print "Waiting for button 1 press..."
while GPIO.input(button1) == False:
    time.sleep(0.1)

print "Button 1 pressed!"

print ""
print "Waiting for button 2 press..."
while GPIO.input(button2) == False:
    time.sleep(0.1)

print "Button 2 pressed!"

print ""
print "Waiting for button 3 press..."
while GPIO.input(button3) == False:
    time.sleep(0.1)

print "Button 3 pressed!"

print ""
print "Finished testing buttons!"
print ""

GPIO.cleanup()
