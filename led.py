import time
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM) #BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)

red = 10
green = 9
blue = 11

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

print ("Testing LEDs...")
print ("")

print ("Green LED on")
GPIO.output(green,GPIO.HIGH)
<<<<<<< HEAD
time.sleep(0.5)
print ("Green LED off")
=======
time.sleep(2)
print "Green LED off"
>>>>>>> 978f98169e09bfbe4b673642fe17972790cbb176
GPIO.output(green,GPIO.LOW)

print ("")
print ("Red LED on")
GPIO.output(red,GPIO.HIGH)
<<<<<<< HEAD
time.sleep(0.5)
print ("Red LED off")
=======
time.sleep(2)
print "Red LED off"
>>>>>>> 978f98169e09bfbe4b673642fe17972790cbb176
GPIO.output(red,GPIO.LOW)

print ("")
print ("Blue LED on")
GPIO.output(blue,GPIO.HIGH)
<<<<<<< HEAD
time.sleep(0.5)
print ("Blue LED off")
=======
time.sleep(2)
print "Blue LED off"
>>>>>>> 978f98169e09bfbe4b673642fe17972790cbb176
GPIO.output(blue,GPIO.LOW)

GPIO.cleanup()
