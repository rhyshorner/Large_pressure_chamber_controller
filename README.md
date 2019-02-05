# chambercontroller
large pressure chamber controller

Components;
PiFace digital 2, from element14
    -

Raspberry Pi 3 model B V1.2 
    - FCC ID: 2ABCB-RPI32
    - IC: 20953-RPI32

LIBRARIES NEED TO INSTALL;
    - sudo apt-get pifacedigitalio

    - sudo apt-get pifacecommon
        NOTE: need to modify "/usr/lib/python3/dist-packages/pifacecommon/spi.py
              need to add "speed_hz=ctypes.c_uint32(100000)" see below;

              # create the spi transfer struct
                transfer = spi_ioc_transfer(
                    tx_buf=ctypes.addressof(wbuffer),
                    rx_buf=ctypes.addressof(rbuffer),
                    len=ctypes.sizeof(wbuffer),
                    speed_hz=ctypes.c_uint32(100000)
                )
    
    - 

