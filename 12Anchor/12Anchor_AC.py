import lcm
import time
import RPi.GPIO as GPIO
from lilylcm import L15Anchor
from lilylcm import L06Depth

#Setup
lc = lcm.LCM()
servoChannel = 17
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoChannel,GPIO.OUT)
pwm = GPIO.GPIO.PWM(servoChannel,60) #Serov only need 60 Hz
pwm.start(0) #Default Position


#Take in Servo Value from LCM and drive the Servo
def servo_handler(channel, data): #Taking Servo Value 
    msg = L15Anchor.decode(data)
    pwm.ChangeDutyCycle(msg.value*100/255.0)

#Read in Depth Sensor and publish depth to LCM
def depth_publish():
    ##TODO readIn
    msg = L06Depth()
    lc.publish("POD_Depth",L06Depth.encode(msg))


subscription = lc.subscribe("POD_Anchor",servo_handler)
print 'Depth Module Started'

while True:
    try:
        lc.handle()
        depth_publish()
    except KeyboardInterrupt:
        break


#Tear Down
print 'Depth Module Exited.'
lc.unsubscribe(subscription)
GPIO.cleanup()
