# this code was last edited on March 13, 2015;
# to be revised for proper channels and instances.

import lcm
import time
from serial import Serial
from lilylcm import pod_data_t

# all LCM calls are commented out for time being. Consult AC
lc = lcm.LCM()

arduinoComm = Serial('/dev/ttyACM0',4800)#Serial
#print arduinoComm
print 'connected'
# help on this one... 

try:
    while True:
        separator = ','
        readin = str(arduinoComm.readline())
	readin = readin.split(separator)
	# in case of faulty data, where fewer than five elements are given
	if len(readin) >= 5:
		data = [float(item) for item in readin[0:5]]
		(compassHeading,windMag,windDir,gpsLat,gpsLong) = data
	
		# comment these out for testing, this is for debugging
		print '\n================='
		print 'compass:', compassHeading
		print 'wind mag:', windMag
		print 'wind dir:', windDir
		print 'gpsLat:', gpsLat
		print 'gpsLong:', gpsLong

		# subject to change
		newMsg = pod_data_t()
		newMsg.gps = [gpsLat, gpsLong]
		newMsg.pod_heading = compassHeading
		newMsg.wind_data = [windMag,windDir]
		newMsg.timestamp = 0.0
		newMsg.pod_wave_off = 1 # is this 'True' or just 1 / 0
	
		lc.publish('pod_data',newMsg.encode())

        time.sleep(.9)

except KeyboardInterrupt:
	pass


