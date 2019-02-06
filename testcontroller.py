import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

pump_relay_pushbutton = 0
pump_relay_state = 0
pump_relay_debounce = 0

def debounce(pfd, laststate):
    #if same as last state wait until statechange
    return

#--------------------------------------------------------------
#try:
while True:

# read value
    pump_relay_pushbutton = pfd.input_pins[0].value

# check current states and toggle accordingly
    if pump_relay_pushbutton == True:
        if pump_relay_state == True:
            pump_relay_state = False
        else:
            pump_relay_state = True

# apply states to outputs
    if pump_relay_state == True:
        pfd.output_pins[0].value = True
        print("pump switch: " + str(pump_relay_pushbutton) + ", pump var: " + str(pump_relay_state) + ", pump debounce: " + str(pump_relay_debounce))
    else:
        pfd.output_pins[0].value = False


#    relief_relay = pfd.input_pins[1].value
#    pfd.output_pins[1].value = relief_relay
 #   print("relief relay is: " + str(pfd.input_pins[1].value))
#except:
#   pfd.output_pins[0].value = 0  
#   pfd.output_pins[1].value = 0

# examples
#output
 # pfd.output_pins[5].value = 1
#input
# switchvariable = pfd.input_pins[1].value


