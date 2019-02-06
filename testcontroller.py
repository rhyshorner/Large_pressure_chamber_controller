import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

# Over pressure auto switch, for relief valve
over_p_auto_sw_state = 0
over_p_auto_sw_debounce = 0

# Over pressure manual switch, for relief valve override
over_p_man_sw_state = 0
over_p_man_sw_debounce = 0

# Under pressure auto switch, for relief valve
under_p_auto_sw_state = 0
under_p_auto_sw_debounce = 0

# Under pressure manual switch, for chamber pump override
under_p_man_sw_state = 0
under_p_man_sw_debounce = 0

# Over pressure signal from Wika input, for relief valve
over_p_wika_state = 0
over_p_wika_debounce = 0

# Over pressure signal from Wika input, for chamber pump
under_p_wika_state = 0
under_p_wika_debounce = 0

# chamber fill pump 
fill_state = 0
fill_debounce = 0

# chamber drain pump
drain_state = 0
drain_debounce = 0

# pump relay output state
pump_relay_state = 0

# relief relay output state
relief_relay_state = 0

#--------------------------------------------------------------
#try:
while True:
    # noise filtering by adding in some counters
# read value
    over_p_auto_sw = pfd.input_pins[0].value
    over_p_man_sw = pfd.input_pins[1].value
    under_p_auto_sw = pfd.input_pins[2].value
    under_p_man_sw = pfd.input_pins[3].value
    over_p_wika = pfd.input_pins[4].value
    under_p_wika = pfd.input_pins[5].value
    fill_sw = pfd.input_pins[6].value
    drain_sw = pfd.input_pins[7].value

    #output 
    # pin0 = pump solenoid
    # pin1 = relief solenoid
    # pin2 = over_p_auto_indicator
    # pin3 = over_p_man_indicator
    # pin4 = under_p_auto_indicator
    # pin5 = under_p_man_indicator
    # pin6 = fill
    # pin7 = drain

# ------------------------------------------------------------------------
# OVER PRESSURE AND PUMP
    if over_p_auto_sw == 1 and over_p_auto_sw_debounce == 0:
        #turn manual switch off, interlock
        over_p_man_sw_state = 0
        #toggle auto switch, either on or off
        over_p_auto_sw_state ^= 1
        #flag debounce variable
        over_p_auto_sw_debounce = 1
    #elif button release
    elif over_p_auto_sw == 0:
        #de-flag debounce variable
        over_p_auto_sw_debounce = 0
    
    if over_p_man_sw == 1 and over_p_man_sw_debounce == 0:
        #turn auto switch off, interlock
        over_p_auto_sw_state = 0
        #toggle manual switch, either on or off
        over_p_man_sw_state ^= 1
        #flag debounce variable
        over_p_man_sw_debounce = 1
    #elif button release
    elif over_p_man_sw == 0:
        #de-flag debounce variable
        over_p_man_sw_debounce = 0

# pump 
    if over_p_man_sw_state == 1:
        # energize pump relay 
        pump_relay_state = 1
    elif over_p_auto_sw_state == 1:
        # if wika input is 1
        if over_p_wika == 1:
            # energize pump relay 
            pump_relay_state = 1
        # else if wika input is 0
        else:
            # de-energize pump relay 
            pump_relay_state = 0
    else:
        pump_relay_state = 0

#------------------------------------------------------------------------
# UNDER PRESSURE AND RELIEF
    if under_p_auto_sw_state == 1 and under_p_auto_sw_debounce == 0:
        #turn manual switch off, interlock
        under_p_man_sw_state = 0
        #toggle auto switch, either on or off
        under_p_auto_sw_state ^= 1
        #flag debounce variable
        under_p_auto_sw_debounce = 1
    #elif button release
    elif under_p_auto_sw == 0:
        #de-flag debounce variable
        under_p_auto_sw_debounce = 0
    
    if under_p_man_sw == 1 and under_p_man_sw_debounce == 0:
        #turn auto switch off, interlock
        under_p_auto_sw_state = 0
        #toggle manual switch, either on or off
        under_p_man_sw_state ^= 1
        #flag debounce variable
        under_p_man_sw_debounce = 1
    #elif button release
    elif under_p_man_sw == 0:
        #de-flag debounce variable
        under_p_man_sw_debounce = 0

# pump 
    if under_p_man_sw_state == 1:
        # energize pump relay 
        relief_relay_state = 1
    elif under_p_auto_sw_state == 1:
        # if wika input is 1
        if under_p_wika == 1:
            # energize pump relay 
            relief_relay_state = 1
        # else if wika input is 0
        else:
            # de-energize pump relay 
            relief_relay_state = 0
    else:
        relief_relay_state = 0

# -----------------------------------------------------------------------------
# FILL AND DRAIN
    if fill_sw == 1 and fill_debounce == 0:
        #drain interlock??
        #drain_state = 0
        #toggle fill switch, either on or off
        fill_state ^= 1
        #flag debounce variable
        fill_debounce = 1
    #elif button release
    elif fill_sw == 0:
        #de-flag debounce variable
        fill_debounce = 0
    
    if drain_sw == 1 and drain_debounce == 0:
        #fill interlock??
        #fill_state = 0
        #toggle drain switch, either on or off
        drain_state ^= 1
        #flag debounce variable
        drain_debounce = 1
    #elif button release
    elif drain_sw == 0:
        #de-flag debounce variable
        drain_debounce = 0

#----------------------------------------------------------------------------------
# apply states to outputs
    pfd.output_pins[0].value = pump_relay_state
    pfd.output_pins[1].value = relief_relay_state
    pfd.output_pins[2].value = over_p_auto_sw_state
    pfd.output_pins[3].value = over_p_man_sw_state
    pfd.output_pins[4].value = under_p_auto_sw_state
    pfd.output_pins[5].value = under_p_man_sw_state
    pfd.output_pins[6].value = fill_state
    pfd.output_pins[7].value = drain_state

# debugging print
    print("pump:" + str(pump_relay_state) 
    + " relief:" + str(relief_relay_state) 
    + " OP auto:" + str(over_p_auto_sw_state) 
    + " OP man:" + str(over_p_man_sw_state) 
    + " UP auto:" + str(under_p_auto_sw_state) 
    + " UP man:" + str(under_p_man_sw_state) 
    + " fill:" + str(fill_state) 
    + " drain:" + str(drain_state)
    )

#    relief_relay = pfd.input_pins[1].value
#    pfd.output_pins[1].value = relief_relay
#    print("relief relay is: " + str(pfd.input_pins[1].value))
#except:
#    pfd.output_pins[0].value = 0  
#    pfd.output_pins[1].value = 0

# examples
#output
 # pfd.output_pins[5].value = 1
#input
# switchvariable = pfd.input_pins[1].value


