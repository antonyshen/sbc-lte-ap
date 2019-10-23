#!/usr/bin/python

from subprocess import check_output
from re import findall
from time import sleep, strftime
import os

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    temp = float(findall("\d+\.\d+",temp)[0])
    return(temp)

def write_temp(temp):
    with open("/tmp/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def Shutdown():
    print("Shutdown system now...")
    os.system("els81-off")
    os.system("sudo sync; sudo sync; sudo sync")
    os.system("sudo shutdown -h now")


while True:
    temp = get_temp()
    write_temp(temp)
    if temp > 80:
        print("[mon-temp] Temp > 80...")
        Shutdown()
    else :
        sleep(60*10)


