
from gpiozero import LED
from time import sleep
from gpiozero import Button
from signal import pause
import time
import os

button = Button(22)
red = LED(18)


while True:

    button.wait_for_press()
    os.system( "/home/pi/block.sh")
    print("websites were blocked")
    red.on()
    sleep(1)

    button.wait_for_press()
    os.system( "/home/pi/unblock.sh")
    print("websites were unblocked")
    red.off()
    sleep(1)

