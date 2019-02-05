import math
import time
from time import sleep
import datetime

import pifacedigitalio as pfd

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object
#--------------------------------------------------------------
while True:
    pfd.output_pins[1].turn_on()    # turn on/set high the second LED
    pfd.output_pins[2].set_high()   # turn on/set high the third LED
    pfd.relays[0].value = 1  # turn on/set high the first relay
    pfd.input_pins[1].value
    sleep(1)
    pfd.output_pins[1].turn_off()    # turn on/set high the second LED
    pfd.output_pins[2].set_low()   # turn on/set high the third LED
    pfd.relays[0].value = 0  # turn on/set high the first relay
    pfd.input_pins[1].value
    sleep(1)


