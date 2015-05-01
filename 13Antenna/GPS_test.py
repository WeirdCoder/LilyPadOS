# this code is to test the gps and heading data transmission to LCM
# to be integrated with the 13Antenna.py code

import lcm
import time
from serial import Serial
from lilylcm import L20CompassHeading
from lilylcm import L11GPS 
from lilylcm import L13Wind

lc = lcm.LCM()

#lc.publish("SOME-CHANNEL", msg.encode())

# port sometimes changes
port = '/dev/ttyACM1'
delay = .09

arduinoComm = Serial(port,9600)#Serial

try:
	while True:
        	#Read data from Arduino
        	separator = ','
        	readin = arduinoComm.readline()
		print(readin)
		try:
			data = [float(item) for item in readin.split(separator)[0:3]]
		except ValueError:
			data = [0.0,42.3585847,-71.08755104]
			# check if there is a better way to handle bad data
		
		(compassHeading, gpsLat, gpsLong) = data
 		
		print "Heading:",compassHeading,"Latitude:",gpsLat,"Longitude:",gpsLong

	        gpsMsg = L11GPS()
       		gpsMsg.latitude = gpsLat
        	gpsMsg.longitude = gpsLong
		compassMsg = L20CompassHeading()
        	compassMsg.direction = compassHeading
        	lc.publish('POD_GPS',gpsMsg.encode())
        	lc.publish('POD_Compass',compassMsg.encode())
        	time.sleep(delay)
		
        
except KeyboardInterrupt:
	pass

lc.unsubscribe(subscription)


