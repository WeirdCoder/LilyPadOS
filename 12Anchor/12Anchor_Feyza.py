import lcm
import RPi.GPIO as GPIO
import time
import atexit
from lilylcm import L15Anchor
from lilylcm import L06Depth

lc=lcm.LCM()
idleDepth=0.1
GPIO.setmode(GPIO.BCM)
pinNumber=6
GPIO.setup(pinNumber,GPIO.OUT)
close= GPIO.LOW
#closeAngleDuty=33
#openAngleDuty=50
startingTime = time.time()
def currentTime():
	return time.time() - startingTime
def depthControl_handler(channel,data):
	msg=L06Depth.decode(data)
	currentDepth=msg.depth
	msg2=L15Anchor()
	#msg2.value=openAngleDuty
        print currentTime()
	#GPIO.output(pinNumber,close)
	time.sleep(0.2)

	if currentTime()<4*60:
                print 'Stage1'
		if currentDepth<=idleDepth :# Close, too shallow
			#msg2.value=closeAngleDuty
			GPIO.output(pinNumber,GPIO.LOW)
		else: # Open when it hits the target
		#	msg2.value=openAngleDuty
			GPIO.output(pinNumber,GPIO.HIGH)
      	else:
		if(currentTime()>6*60):
			print 'StageSOS'	
			if int(currentTime())%10 <5 :
				#msg2.value=openAngleDuty
				GPIO.output(pinNumber, GPIO.HIGH)
			else:
				#msg2.value=closeAngleDuty
				GPIO.output(pinNumber,GPIO.LOW)
		else:

			GPIO.output(pinNumber, GPIO.HIGH)
        print msg2.value
#        if GPIO.input(pinNumber) == GPIO.HIGH:
#		print 'Open'
#	else:
#		print 'Close'
	lc.publish("POD_Anchor", msg2.encode())

subscription=lc.subscribe("POD_Depth", depthControl_handler)
print "Control module started"


def onExit():
   GPIO.cleanup()
   print 'Control Module exited'
   lc.unsubscribe(subscription)
atexit.register(onExit)
while True:
	try:
		lc.handle()
	except KeyboardInterrupt:
                GPIO.cleanup() 
		break
