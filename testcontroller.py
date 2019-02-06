import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

pump_relay_state = 0
pump_relay_debounce = 0

def debounce(pfd, laststate):
    #if same as last state wait until statechange
    return

#--------------------------------------------------------------
#try:
while True:

    pump_relay_pushbutton = pfd.input_pins[0].value
    if pump_relay_debounce == 1 & pump_relay_pushbutton == 0:
        pump_relay_debounce = 0
    if pump_relay_pushbutton == 1 & pump_relay_debounce == 0:
        pump_relay_state = not pump_relay_state
        pump_relay_debounce = 1

    pfd.output_pins[0].value = pump_relay_state
    print("pump relay switch is: " + str(pump_relay_pushbutton) + " pump relay variable is: " + str(pump_relay_state))

    relief_relay = pfd.input_pins[1].value
    pfd.output_pins[1].value = relief_relay
    print("relief relay is: " + str(pfd.input_pins[1].value))
#except:
#   pfd.output_pins[0].value = 0  
#   pfd.output_pins[1].value = 0

# examples
#output
 # pfd.output_pins[5].value = 1
#input
# switchvariable = pfd.input_pins[1].value


