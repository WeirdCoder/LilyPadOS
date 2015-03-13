import lcm
import time
"from Adafruit_PWM_Servo_Driver import PWM"
import RPi.GPIO as GPIO
from lilylcm import l15Anchor

def my_handler(channel, data):
	msg=L152Anchor()
	msg2=Activation()
	idledepth=9
	motorController()
	lc.publish("L15Anchor", msg.encode())

	 
lc=lcm.LCM()
subscription=lc.subscribe("15Anchor", my_handler)
#Subsribe to the activation signal possibly in boolean
subscriptionAc=lc.subscribe("Activation", my handler)

#set servo on GP017 to 1200microsec
servoChannel=17
GPIO.setmode(GPIO.BOARD) ##either GPIO.BOARD or GPIO.BCM depending on what you like
GPIO.setup(servoChannel, GPIO.OUT) ##servo is an output on pin 18

pwm = GPIO.PWM(servochannel, 100) ##making servo channel a PWM pin at 100Hz
pwm.start(2.5)##starting the PWM signal with a duty cycle of 2.5 is this a percentage?
def motorController()
try:
  while True:# change this to activation signal in future
    currentDepth=msg.depth
    if currentdepth<=idledepth-5: ##if the current depth is not close to the idle depth about 5m
      pwm.ChangeDutyCycle(2.5) ##doesn't change the position of the servo
      time.sleep(0.5) #wait for the next comman for 0.5 s
    else if abs(currentDepth-idledepth)<1
      pwm.ChangeDutyCycle(10) ##change the duty cycle to 10 if too close
    else 
      pwm.ChangeDutyCycle(5)##change the duty cycle to 5 other times
      time.sleep(0.10)

except KeyboardInterrupt: ##if you press control+C in terminal, it will go here
  GPIO.cleanup() ##closes all the GPIO pins in the code





"""

while (True):
  # Control the servo according to the depth 
	


  time.sleep(1)
  pwm.setPWM(0, 0, servoMax)
  time.sleep(1)
def motorcontrol(depth)

try:
	while True:
		lc.handle()
	except KeyboardInterrupt:
		pass

lc.unsubscribe(subscription)
servo.stop_servo(servoChannel)

 
