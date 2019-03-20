# chambercontroller
large pressure chamber controller

##Components;
PiFace digital 2, from element14
    -

##Raspberry Pi 3 model B V1.2 
    - FCC ID: 2ABCB-RPI32
    - IC: 20953-RPI32

##LIBRARIES NEED TO INSTALL;
    - sudo apt-get pifacedigitalio

    - sudo apt-get pifacecommon
        NOTE: need to modify `"/usr/lib/python3/dist-packages/pifacecommon/spi.py`
              need to add `"speed_hz=ctypes.c_uint32(100000)" see below;`

             ``` # create the spi transfer struct
                transfer = spi_ioc_transfer(
                    tx_buf=ctypes.addressof(wbuffer),
                    rx_buf=ctypes.addressof(rbuffer),
                    len=ctypes.sizeof(wbuffer),
                    speed_hz=ctypes.c_uint32(100000)
                )```
    
##RPI BOOT SETTINGS REQUIRED TO CHANGE
    -   sudo nano /etc/rc.local
        -add "python3 /home/pi/chambercontroller/controller.py &"(line 50) just above `"exit 0"`(line 52)

```
!/bin/sh -e

 rc.local

 This script is executed at the end of each multiuser runlevel.
 Make sure that the script will "exit 0" on success or any other
 value on error.

 In order to enable or disable this script just change the execution
 bits.

 By default this script does nothing.

 Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

python3 /home/pi/chambercontroller/controller.py &

exit 0

```

    - to end the process in the GUI 

open terminal then type;
`$ sudo ps -ax | grep python`

find the PID code preceeding "python3 /home/pi/chambercontroller/controller.py"
then type that number into terminal; (in place of XXX)
`$ sudo kill XXX`

to get output, debugg and to see more options go to;
https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all

---------------------------------------------------------------------

##ADC
1-Channel I2C 4-20mA Current Receiver Board w/ I2C Interface
`https://www.robotshop.com/en/1-channel-i2c-4-20ma-current-receiver-board-i2c-interface.html`

ADS1115 ADC sample code;
`https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115`

