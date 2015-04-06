# this code was last edited on March 13, 2015;
# to be revised for proper channels and instances.

import lcm
import time
from serial import Serial
from lilylcm import L20CompassHeading
from lilylcm import L11GPS
from lilylcm import L13Wind 

lc = lcm.LCM()

lc.publish("SOME-CHANNEL", msg.encode())

arduinoComm = Serial('/dev/ttyUSB0',9600)#Serial

try:
    while True:
        #Read data from Arduino
        separator = ','
        readin = arduinoComm.readline()
        (windDir,windMag,compassHeading,gpsLong, gpsLat) = readin.split(separator)
        gpsMsg = L11GPS()
        gpsMsg.latitude = gpsLat
        gpsMsg.longtitude = gpslong
        windMsg = L13Wind()
        windMsg.direction = windDir - compassHeading
        windMsg.magnitude = windMag
        compassMsg = L20CompassHeading()
        compassMsg.direction = compassHeading
        lc.publish('POD_GPS',gpsMsg.encode())
        lc.publish('POD_Wind',windMsg.encode())
        lc.publish('POD_Compass',compassMsg.encode())
        time.delay(1)
        
except Keyboardinterrupt:
	pass
lc.unsubscribe(subscription)


