#!/usr/bin/python3
from gpiozero import Button
from signal import pause
from subprocess import check_call, check_output

# 2017-12-12
# This script was copied from the following RPi forum post:
# https://forum-raspberrypi.de/forum/thread/13144-projekt-jukebox4kids-jukebox-fuer-kinder/?postID=312257#post312257
# I have not yet had the time to test is, so I placed it in the misc folder.
# If anybody has ideas or tests or experience regarding this solution, please create pull requests or contact me.

def def_volU():
    print("volU")
    check_call("amixer sset Master 10+", shell=True)

def def_volD():
    print("volD")
    check_call("amixer sset Master 10-", shell=True)

def def_next():
    print("next")
    check_call("echo 'next' | nc.openbsd -w 1 localhost 4212", shell=True)

def def_prev():
    print("prev")
    check_call("echo 'prev' | nc.openbsd -w 1 localhost 4212", shell=True)

def def_halt():
    print("pause")
    check_call("echo 'pause' | nc.openbsd -w 1 localhost 4212", shell=True)

button23 = Button(23)
button23.when_pressed = def_volU

button12 = Button(12)
button12.when_pressed = def_volD

button4 = Button(4)
button4.when_pressed = def_next

button27 = Button(27)
button27.when_pressed = def_prev

button6 = Button(6)
button6.when_pressed = def_halt

pause()
