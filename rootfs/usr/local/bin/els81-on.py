#!/usr/bin/env python3
import os
import sys
from gpiozero import LED
from time import sleep

print("ELS81 turn-on utility")
print("written by Antony Shen <antony.shen@gemalto.com>")

if not os.geteuid() == 0:
    sys.exit("\nOnly root can run this script\n")

els81 = LED(25)

print("Turn-on ELS81...")
els81.on()
sleep(1)
els81.off()
#sleep(4)
print("done!")
