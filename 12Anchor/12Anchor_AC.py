import smbus
import lcm
import time
import RPi.GPIO as GPIO
from lilylcm import L15Anchor
from lilylcm import L06Depth
from ABE_ADCPi import ADCPi
import time

import threading

#Setup
lc = lcm.LCM('udpm://239.255.76.67:7667?ttl=1')
servoChannel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoChannel, GPIO.OUT) 
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(servoChannel,GPIO.OUT)
pwm = GPIO.PWM(servoChannel,1520) #Serov only need 60 Hz
pwm.start(0) #Default Position
i2cBus = smbus.SMBus(1)

#Take in Servo Value from LCM and drive the Servo
def servo_handler(channel, data): #Taking Servo Value 
    msg = L15Anchor.decode(data)
    #print 'Servo'
    #print msg.value
    #pwm.ChangeDutyCycle(msg.value)

servoThreadState = {"active":True}
def servo_Thread():
    while servoThreadState["active"]:
        lc.handle()

#Read in Depth Sensor and publish depth to LCM
def depth_publish():
    depth = ADCPi(i2cBus, 0x68, 0x69)
    msg = L06Depth()
    voltage = depth.read_voltage(0x69)-.5
    pressure = voltage*12.5 # Psi
    msg.depth = (pressure*6895)/(9.8 * 1000) # depth in meter
   #fakeDepth=[0.1, 0.2, 0.345,0.299, 0.5, 0.6, 0.7, 1]
  # for i=1:8
   #	msg.depth=fakeDepth[i]
    print msg.depth
    lc.publish("POD_Depth",L06Depth.encode(msg))
	#time.sleep(0.05)


subscription = lc.subscribe("POD_Anchor",servo_handler)
print 'Depth Module Started'

servoThread = threading.Thread(target=servo_Thread)
servoThread.setDaemon(True)
servoThread.start()

try:
    while True:
        depth_publish()
        time.sleep(0.02)
        print 'Hello'
except KeyboardInterrupt:
    x = 1
finally:
    #Tear Down
    servoThreadState['active'] = False
    lc.unsubscribe(subscription)
    GPIO.cleanup()
    print 'Depth Module Exited.'
