import serial
import lcm
import time

from lilylcm import L21DockDetect

lc = lcm.LCM()

port = serial.Serial("/dev/ttyACM0", baudrate = 9600) ##change to what ever port the arduino is connected to

msg = L21DockDetect()

def my_handler(channel, data):
  if port.readline() == "ON":
    msg.detected = True
    lc.publish("POD_DockDetect", msg.encode())
  else if port.readline() == "OFF":
    msg.detected = False
    lc.publish("POD_DockDetect", msg.encode())
  else:
    pass

subL = lc.subscribe("POD_LED", my_handler)
subD = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    port.write(str(sub.activate))
    lc.handle()
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(subL)
  lc.unsubscribe(subD)

