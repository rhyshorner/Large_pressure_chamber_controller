import math
import time
from time import sleep
import datetime

import pifacedigitalio as pfd

# -------CONSTANTS--------------------------------------------------
# INPUTS
OVER_PRESSURE_AUTO_SW = 0
OVER_PRESSURE_MAN_SW = 1

UNDER_PRESSURE_AUTO_SW = 2
UNDER_PRESSURE_MAN_SW = 3

OVER_PRESSURE_WIKA_IP = 4
UNDER_PRESSURE_WIKA_IP = 5

FILL_SW = 6
DRAIN_SW = 7

# OUTPUTS
PUMP_SOLENOID = 0
RELIEF_SOLENOID = 1

OVER_PRESSURE_AUTO_LED = 2
OVER_PRESSURE_MAN_LED = 3

UNDER_PRESSURE_AUTO_LED = 4
UNDER_PRESSURE_MAN_LED = 5

FILL_LED = 6
DRAIN_LED = 7

#----------------------------------------------------------------
# -initializing pifaceddgitialio
#pifacedigital = pifacedigitalio.PiFaceDigital() # creates instance
pfd.init()

#--------------------------------------------------------------
#blink output 4
try:
    while True:
        p.digital_write(0, 1)
        p.digital_read(2, 3)    # writes pin0 high
        sleep(1)
        p.digital_write(0, 0)
        p.digital_read(2, 3)
        sleep(1)
except:
    p.deinit()
# ----------------------------------------------------------

