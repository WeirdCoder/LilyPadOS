import lcm
import time
from lilylcm import L15Anchor
from lilylcm import L06Depth

lc=lcm.LCM()
idleDepth=0.6


closeAngleDuty=33
openeAngleDuty=50
def depthControl_handler(channel,data):
	msg=L06Depth.decode(data)
	currentDepth=msg.depth
	msg2=L15Anchor()
	msg2.value=initialValue

	if currentDepth<=(idleDepth-0.3) :# Close, too shallow
		msg2.value=closeAngleDuty
	else: # Open when it hits the target
		msg2.value=openAngleDuty
        print msg2.value
	lc.publish("POD_Anchor", msg2.encode())
	time.sleep(0.05)
subscription=lc.subscribe("POD_Depth", depthControl_handler)
print "Control module started"

while True:
	try:
		lc.handle()
	except KeyboardInterrupt: 
		break

print 'Control Module exited'
lc.unsubscribe(subscription)

