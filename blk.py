
from time import sleep
import time
import os
import blynklib

BLYNK_AUTH = '35TxWUWLMH4q7of7Wn5tU1AOBbbaVctz'

blynk = blynklib.Blynk(BLYNK_AUTH)


@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print('V1:'+ str(value))
    if value[0]=="1":
        os.system("/home/pi/block.sh")
        print("blocked")
    else:
        os.system("/home/pi/unblock.sh")
        print("unblocked")
while True:
    blynk.run()

