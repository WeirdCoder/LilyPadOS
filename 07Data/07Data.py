'''
07 Data Module
Author: alexc89

The purpose of the module is to mirror LCM channels through xBee serial or actualy any serial channel.  Please note that this module doesn't need to know the lcmtype, for it doesn't need to read the content of the data.

'''

import lcm
import time
import serial
from xbee import XBee

#Serial to LCM Mapping
SLCMMap = ["State","Heading", "GPS", "Wind"]

#Setup Handler for LCM
lc = lcm.LCM()
channelDB = dict()
PORT = '/dev/ttyUSB0'
BAUD = 9600
ser = Serial(PORT, BAUD)
xbee = XBee(ser, callback=serialHandler)
subscriptions = [lc.subscribe(name,lcmHandler) for name in SLCMMap]

def lcmHandler(channelNameLCM, data)
    #Handler converting LCM to Serial
    channelNum = SLCMMap.index(channelNameLCM)
    xbee.tx(dest_addr='\x00\x01', data='%n %s' % channelNum, data)


def serialHandler(serialData)
    #Handler converting Serial to LCM
    (channelNum, data) = serialData.split('.')
    channelNum = int(channelNum)
    channelNameLCM = SLCMMap[channelNum]
    lc.publish(channelNameLCM,data)

try:
    while True
        #handle LCM
        lc.handle()
except Keyboardinterrupt:
    print "Module Exits from Keyboard Interrupt"

ser.close()
[lc.unsubscribe(x) for x in subscriptions]
