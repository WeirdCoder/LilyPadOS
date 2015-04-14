import RPi.GPIO as GPIO
import lcm
import time

from lilylcm import L21DockDetect
from lilylcm import L14LEDs ##now the satellite box
from lilylcm import L19DockCommand 

lc = lcm.LCM()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN) ##charge detection
GPIO.setup(38, GPIO.OUT) ##magnet servo
GPIO.setup(40, GPIO.OUT) ##relay for satellite box

pwm = GPIO.PWM(38, 100) ##set frequency to 100Hz
pwm.start(1) ##start with a duty cycle of 1 so the magnet is in the off position
GPIO.output(40, False) ##turn the satellite box off

msg = L21DockDetect() ##get a message ready to send to the dock detect channel

def my_handler(channel, data):
  if channel == "POD_LED":
    datamsg = L14LEDs.decode(data)
    GPIO.output(40, datamsg.switchOn)

  elif channel == "POD_Magnet":
    datamsg = L19DockCommand.decode(data)
    if datamsg.switchOn == True:
      pwm.ChangeDutyCycle(99)
    else:
      pwm.ChangeDutyCycle(1)

  msg.detected = boolean(GPIO.input(36))
  lc.publish("POD_DockDetect",  msg.encode())

subL = lc.subscribe("POD_LED", my_handler)
subD = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    lc.handle()
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(subL)
  lc.unsubscribe(subD)

