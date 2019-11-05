#!/usr/bin/python3
# Simple script for
# 1. toggle AP on/off when quick press once, 
# 2. reboot / shutting down the raspberry Pi when press over 3 / 6 secs
# by Antony Shen

import RPi.GPIO as GPIO
import time
import subprocess

# Use the Broadcom SOC Pin numbers
FUNC_PIN = 24
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(FUNC_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def btnfunc(channel):
    time.sleep(0.01)         # need to filter out the false positive of some power fluctuation
    if GPIO.input(FUNC_PIN) != GPIO.LOW:
        print('quitting event handler because this was probably a false positive')
        return

    time.sleep(1)
    # if short press, toggle AP on/off
    if GPIO.input(FUNC_PIN) == GPIO.HIGH:
        p = subprocess.Popen('systemctl status hostapd | grep "running" | wc -l', stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if b'1' in output:
            print("Toggle AP off...")
            subprocess.run(['sudo', 'systemctl', 'stop', 'hostapd'])
        else:
            print("Toggle AP on...")
            subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'])
        return

    # if press over 3s, prepare to reset (3s) or shutdown device(5s)
    time.sleep(2)
    subprocess.run(['els81-off'], shell=True)
    if GPIO.input(FUNC_PIN) == GPIO.HIGH:
        print("Short-press on reset button, reboot system now...")
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'reboot', '-h', 'now'])
        return

    # if press over 5s, prepare to shutdown device
    time.sleep(3)         # need to filter out the false positive of some power fluctuation
    if GPIO.input(FUNC_PIN) == GPIO.HIGH:
        print("Shutdown system now...")
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'sync'])
        subprocess.run(['sudo', 'shutdown', '-h', 'now'])

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(FUNC_PIN, GPIO.BOTH, callback=btnfunc, bouncetime=150)

# Now wait!
while 1:
    time.sleep(86400)

