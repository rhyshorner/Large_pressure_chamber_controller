import math
import time
from time import sleep
import datetime

import pifacedigitalio

pifacedigital = pifacedigitalio.PiFaceDigital() # creates instance

pifacedigital.output_pins[4].turn_on() # turns output pin 4 to HIGH

# ----------------------------------------------------------

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

