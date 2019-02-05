import math
import time
from time import sleep
import datetime

import pifacedigitalio as p

p.init()
#--------------------------------------------------------------
while True:
    p.digital_write(0, 1)
    p.digital_read(2, 3)
    sleep(1)
    p.digital_write(0, 0)
    p.digital_read(2, 3)
    sleep(1)


