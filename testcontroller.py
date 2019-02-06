import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object


pump_relay_state = 0
pump_relay_debounce = 0
relief_relay_state = 0
relief_relay_debounce = 0


def debounce(pfd, laststate):
    #if same as last state wait until statechange
    return

#--------------------------------------------------------------
#try:
while True:

# read value
    pump_relay_pushbutton = pfd.input_pins[0].value
    relief_relay_pushbutton = pfd.input_pins[1].value

# check current states and toggle accordingly
    if pump_relay_pushbutton == 1 and pump_relay_debounce == 0:
            pump_relay_state ^= 1
            pump_relay_debounce = 1
    elif pump_relay_pushbutton == 0:
        pump_relay_debounce = 0

    if relief_relay_pushbutton == 1 and relief_relay_debounce == 0:
            relief_relay_state ^= 1
            relief_relay_debounce = 1
    elif relief_relay_pushbutton == 0:
        relief_relay_debounce = 0

# apply states to outputs
    pfd.output_pins[0].value = pump_relay_state
    pfd.output_pins[1].value = relief_relay_state

# debugging print
    print("pump:" + str(pump_relay_state) + " relief:" + str(relief_relay_state))

# state machine here
#    if over_p_auto_sw == False & over_p_man_sw == False & etc etc

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


