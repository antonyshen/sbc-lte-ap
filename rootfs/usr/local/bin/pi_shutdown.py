#!/usr/bin/python3
# Simple script for shutting down the raspberry Pi

import os

# Our function on what to do when the button is pressed
def Shutdown():
    print("Shutdown system now...")
    os.system("els61_off.py")
    os.system("sudo sync; sudo sync; sudo sync")
    os.system("sudo shutdown -h now")

Shutdown()
