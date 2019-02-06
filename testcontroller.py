import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

def debounce(pfd, laststate):
    #if same as last state wait until statechange
    return

#--------------------------------------------------------------
#try:
while True:
    pump_relay = pfd.input_pins[0].value
    pfd.output_pins[0].value = pump_relay
    print("input pin 1 is: " + str(pfd.input_pins[0].value))

    relief_relay = pfd.input_pins[1].value
    pfd.output_pins[1].value = relief_relay
    print("input pin 1 is: " + str(pfd.input_pins[1].value))

    sleep(0.25)
#except:
#   pfd.output_pins[0].value = 0  
#   pfd.output_pins[1].value = 0

# examples
#output
 # pfd.output_pins[5].value = 1
#input
# switchvariable = pfd.input_pins[1].value


