import smbus
import time
from time import sleep
import os
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD) #BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)

red = 21
green = 19
blue = 23
mosfet = 15
button1 = 11
button2 = 12
button3 = 13
out1 = 7
out2 = 8
out3 = 10

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(mosfet,GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print ("*~*~* Start testing LEDs *~*~*\n")

SLEEP_TIME = 2

print ("Green LED on\n")
GPIO.output(green,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Green LED off\n")
GPIO.output(green,GPIO.LOW)

print ("Red LED on\n")
GPIO.output(red,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Red LED off\n")
GPIO.output(red,GPIO.LOW)

print ("Blue LED on\n")
GPIO.output(blue,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Blue LED off\n")
GPIO.output(blue,GPIO.LOW)

print ("Out 1 on\n")
GPIO.output(blue,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Out 1 off\n")
GPIO.output(blue,GPIO.LOW)

print ("Out 2 on\n")
GPIO.output(blue,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Out 2 off\n")
GPIO.output(blue,GPIO.LOW)

print ("Out 3 on\n")
GPIO.output(blue,GPIO.HIGH)
time.sleep(SLEEP_TIME)
print ("Out 3 off\n")
GPIO.output(blue,GPIO.LOW)

print ("\n")
print ("Finished testing LEDs!\n")
#print ("\n")

print ("*~*~* Start testing MOSFET *~*~*\n")
print ("\n")

print ("MOSFET on\n")
GPIO.output(mosfet,GPIO.HIGH)
time.sleep(1)
print ("MOSFET off\n")
GPIO.output(mosfet,GPIO.LOW)

#print ("\n")
print ("Finished testing MOSFET!\n")
print ("\n")

print ("*~*~* Starting button tests *~*~*\n")
print ("\n")

print ("Waiting for button 1 press...\n")
while GPIO.input(button1) == False:
    time.sleep(0.1)

print ("Button 1 pressed!\n")

print ("\n")
print ("Waiting for button 2 press...\n")
while GPIO.input(button2) == False:
    time.sleep(0.1)

print ("Button 2 pressed!\n")

print ("\n")
print ("Waiting for button 3 press...\n")
while GPIO.input(button3) == False:
    time.sleep(0.1)

print ("Button 3 pressed!\n")

print ("\n")
print ("Finished testing buttons!\n")
print ("\n")

#I2C testing code
#SCL = 5
#SDA = 3
# TO BE RUN ONLY WHEN YOU HAVE AN I2C DHT22 CONNECTED ON THE I2C LINES!

DEVICE = 0x5C #device I2C address
bus = smbus.SMBus(1)
def readdata(addr=DEVICE):
  #read 5 bytes of data from the device address (0x05C) starting from an offset of zero
  data = bus.read_i2c_block_data(addr,0x00, 5)
  print ("Humidity = " + str(data[0]) + "." + str(data[1]) + "%")
  print ("Temperature : " + str(data[2]) + "." + str(data[3]) + "C")
  if (data[0] + data[1] + data[2] + data[3] == data[4]):
    print ("checksum is correct")
  else:
    print ("checksum is incorrect")

#if __name__=="__main__":
readdata()

# RTC Testing
# First add dtoverlay=i2c-rtc,mcp7940x in /boot/config.txt
# Then reboot and disable the fake-hwclock
# Then try sudo hwclock -r to read from the RTC

print ("*~*~* Start testing RTC *~*~*\n")
# print ("")
subprocess.call(["sudo", "hwclock", "--systohc"])
subprocess.call(["sudo", "hwclock", "-r", "--verbose"])

print ("\n")
print ("Finished testing RTC!\n")
# print ("")
