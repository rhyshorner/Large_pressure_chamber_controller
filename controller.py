import math
import time
from time import sleep
import datetime

import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

# Over pressure auto switch, for relief valve
over_p_auto_sw_state = 0
over_p_auto_sw_toggle = 0

# Over pressure manual switch, for relief valve override
over_p_man_sw_state = 0
over_p_man_sw_toggle = 0

# Under pressure auto switch, for relief valve
under_p_auto_sw_state = 0
under_p_auto_sw_toggle = 0

# Under pressure manual switch, for chamber pump override
under_p_man_sw_state = 0
under_p_man_sw_toggle = 0

# Over pressure signal from Wika input, for relief valve
unused_input4_state = 0
unused_input4_toggle = 0

# Over pressure signal from Wika input, for chamber pump
unused_input5_state = 0
unused_input5_toggle = 0

# chamber fill pump 
fill_state = 0
fill_toggle = 0

# chamber drain pump
drain_state = 0
drain_toggle = 0

# pump relay output state
unused_relay0_state = 0

# relief relay output state
unused_relay1_state = 0

debounce_over_p_auto_flag = 0
debounce_over_p_man_flag = 0
debounce_under_p_auto_flag = 0
debounce_under_p_man_flag = 0
debounce_unused_input4_flag = 0
debounce_unused_input5_flag = 0
debounce_fill_flag = 0
debounce_drain_flag = 0

debounce_over_p_auto_starttimer = 0
debounce_over_p_man_starttimer = 0
debounce_under_p_auto_starttimer = 0
debounce_under_p_man_starttimer = 0
debounce_unused_input4_starttimer = 0
debounce_unused_input5_starttimer = 0
debounce_fill_starttimer = 0 
debounce_drain_starttimer = 0
#--------_over_p_auto_------------------------------------------------------
try:
    while True:
        # noise filtering by adding in some counters
    # read value
        over_p_auto_sw = pfd.input_pins[0].value
        over_p_man_sw = pfd.input_pins[1].value
        under_p_auto_sw = pfd.input_pins[2].value
        under_p_man_sw = pfd.input_pins[3].value
        #unused_input4 = pfd.input_pins[4].value
        #unused_input5 = pfd.input_pins[5].value
        fill_sw = pfd.input_pins[6].value
        drain_sw = pfd.input_pins[7].value

        #output 
        # pin0 = unused relay0
        # pin1 = unused relay1
        # pin2 = over_p_auto_indicator
        # pin3 = over_p_man_indicator
        # pin4 = under_p_auto_indicator
        # pin5 = under_p_man_indicator
        # pin6 = fill
        # pin7 = drain

    # ------------------------------------------------------------------------
    # OVER PRESSURE AND PUMP
        if debounce_over_p_auto_flag == 0:
            if over_p_auto_sw == 1 and over_p_auto_sw_toggle == 0:
                debounce_over_p_auto_flag = 1
                debounce_over_p_auto_starttimer = time.time()

                #turn manual switch off, interlock
                over_p_man_sw_state = 0
                #toggle auto switch, either on or off
                over_p_auto_sw_state ^= 1
                #flag toggle variable
                over_p_auto_sw_toggle = 1
            #elif bu_over_p_auto_tton release
            elif over_p_auto_sw == 0 and over_p_auto_sw_toggle == 1:
                debounce_over_p_auto_flag = 1
                debounce_over_p_auto_starttimer = time.time()

                #de-flag toggle variable
                over_p_auto_sw_toggle = 0
                #reset debounce timer flag
                #debounce_over_p_auto_flag = 0
        
        if (time.time() - debounce_over_p_auto_starttimer) >= 0.2:
            #reset debounce timer flag
            debounce_over_p_auto_flag = 0
        
    #--------------
        if debounce_over_p_man_flag == 0:
            if over_p_man_sw == 1 and over_p_man_sw_toggle == 0:
                debounce_over_p_man_flag = 1
                debounce_over_p_man_starttimer = time.time()
                over_p_auto_sw_state = 0
                over_p_man_sw_state ^= 1
                over_p_man_sw_toggle = 1

            elif over_p_man_sw == 0 and over_p_man_sw_toggle == 1:
                debounce_over_p_man_flag = 1
                debounce_over_p_man_starttimer = time.time()
                over_p_man_sw_toggle = 0
                
        if (time.time() - debounce_over_p_man_starttimer) >= 0.2:
            debounce_over_p_man_flag = 0

    #------------------------------------------------------------------------
    # UNDER PRESSURE AND RELIEF
    #auto
        if debounce_under_p_auto_flag == 0:
            if under_p_auto_sw == 1 and under_p_auto_sw_toggle == 0:
                debounce_under_p_auto_flag = 1
                debounce_under_p_auto_starttimer = time.time()
                under_p_man_sw_state = 0
                under_p_auto_sw_state ^= 1
                under_p_auto_sw_toggle = 1

            elif under_p_auto_sw == 0 and under_p_auto_sw_toggle == 1:
                debounce_under_p_auto_flag = 1
                debounce_under_p_auto_starttimer = time.time()
                under_p_auto_sw_toggle = 0
                
        if (time.time() - debounce_under_p_auto_starttimer) >= 0.2:
            debounce_under_p_auto_flag = 0

    #manual
        if debounce_under_p_man_flag == 0:
            if under_p_man_sw == 1 and under_p_man_sw_toggle == 0:
                debounce_under_p_man_flag = 1
                debounce_under_p_man_starttimer = time.time()

                under_p_auto_sw_state = 0
                under_p_man_sw_state ^= 1
                under_p_man_sw_toggle = 1
            elif under_p_man_sw == 0 and under_p_man_sw_toggle == 1:
                debounce_under_p_man_flag = 1
                debounce_under_p_man_starttimer = time.time()
                under_p_man_sw_toggle = 0
                
        if (time.time() - debounce_under_p_man_starttimer) >= 0.2:
            debounce_under_p_man_flag = 0

    # -----------------------------------------------------------------------------
    # FILL AND DRAIN
        if debounce_fill_flag == 0:
            if fill_sw == 1 and fill_toggle == 0:
                debounce_fill_flag = 1
                debounce_fill_starttimer = time.time()
                fill_state ^= 1
                fill_toggle = 1
            elif fill_sw == 0 and fill_toggle == 1:
                debounce_fill_flag = 1
                debounce_fill_starttimer = time.time()
                fill_toggle = 0

        if (time.time() - debounce_fill_starttimer) >= 0.2:
            debounce_fill_flag = 0

        if debounce_drain_flag == 0:
            if drain_sw == 1 and drain_toggle == 0:
                debounce_drain_flag = 1
                debounce_drain_starttimer = time.time()
                drain_state ^= 1
                drain_toggle = 1
            elif drain_sw == 0 and drain_toggle == 1:
                debounce_drain_flag = 1
                debounce_drain_starttimer = time.time()
                drain_toggle = 0

        if (time.time() - debounce_drain_starttimer) >= 0.2:
            debounce_drain_flag = 0

    #----------------------------------------------------------------------------------
    # apply states to outputs
        #pfd.output_pins[0].value = unused_relay0_state
        #pfd.output_pins[1].value = unused_relay1_state
        pfd.output_pins[2].value = over_p_auto_sw_state
        pfd.output_pins[3].value = over_p_man_sw_state
        pfd.output_pins[4].value = under_p_auto_sw_state
        pfd.output_pins[5].value = under_p_man_sw_state
        pfd.output_pins[6].value = fill_state
        pfd.output_pins[7].value = drain_state

    # debugging print
        print("OP auto:" + str(over_p_auto_sw_state) 
        + " OP man:" + str(over_p_man_sw_state) 
        + " UP auto:" + str(under_p_auto_sw_state) 
        + " UP man:" + str(under_p_man_sw_state) 
        + " fill:" + str(fill_state) 
        + " drain:" + str(drain_state)
        )
except:
        print("a script interuption has occured")
        print("all outputs pins set to low")
# apply script shutdown output values
        #pfd.output_pins[0].value = 0 #on board relay
        #pfd.output_pins[1].value = 0 #on board relay
        pfd.output_pins[2].value =  0 #over_p_auto_sw_state
        pfd.output_pins[3].value =  0 #over_p_man_sw_state
        pfd.output_pins[4].value =  0 #under_p_auto_sw_state
        pfd.output_pins[5].value =  0 #under_p_man_sw_state
        pfd.output_pins[6].value =  0 #fill_state
        pfd.output_pins[7].value =  0 #drain_state