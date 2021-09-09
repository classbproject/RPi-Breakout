import os
import subprocess

# First add dtoverlay=i2c-rtc,mcp7940x in /boot/config.txt
# Then reboot and disable the fake-hwclock
# Then try sudo hwclock -r to read from the RTC

print("*~*~* Start testing RTC *~*~*")
print("")

subprocess.call(["sudo", "hwclock", "--verbose"])

print("")
print("Finished testing RTC!")
print("")
