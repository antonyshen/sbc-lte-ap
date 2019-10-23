#!/usr/bin/python3
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import ASUS.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
SHUTDOWN_PIN=18
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    time.sleep(0.01)         # need to filter out the false positive of some power fluctuation
    if GPIO.input(SHUTDOWN_PIN) != GPIO.LOW:
        print('quitting event handler because this was probably a false positive')
        return

    os.system("els81-off")

    time.sleep(2)         # need to filter out the false positive of some power fluctuation
    if GPIO.input(SHUTDOWN_PIN) != GPIO.LOW:
        print("Short-press on reset button, reboot system now...")
        os.system("sudo sync; sudo sync; sudo sync")
        os.system("sudo reboot -h now")
    else:
        print("Shutdown system now...")
        os.system("sudo sync; sudo sync; sudo sync")
        os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(SHUTDOWN_PIN, GPIO.BOTH, callback = Shutdown, bouncetime = 150)

# Now wait!
while 1:
    time.sleep(86400)

