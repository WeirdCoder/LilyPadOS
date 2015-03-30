import serial
import lcm
import time

from lilylcm import L21DockDetect
from lilylcm import L14LEDs
from lilylcm import L19DockCommand 

lc = lcm.LCM()

port = serial.Serial("/dev/ttyACM0", baudrate = 9600) ##change to what ever port the arduino is connected to

dic = [0,0]
msg = L21DockDetect()

def change():
  if dic == [0,0]:
    return 0
  elif dic == [0,1]:
    return 1
  elif dic == [1,0]:
    return 2
  elif dic == [1,1]:
    return 3 

def my_handler(channel, data):
  if channel == "POD_LED":
    datamsg = L14LEDs.decode(data)
    dic[0] = datamsg.switchOn

  elif channel == "POD_Magnet":
    datamsg = L19DockCommand.decode(data)
    dic[1] = datamasg.switchOn

  port.write(change())

  if port.readline() == "ON":
    msg.detected = True
    lc.publish("POD_DockDetect",  msg.encode())
  elif port.readline() == "OFF":
    msg.detected = False
    lc.publish("POD_DockDetect", msg.encode())
  else:
    print "Somethings fucked up in 10Docking.py"

subL = lc.subscribe("POD_LED", my_handler)
subD = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    lc.handle()
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(subL)
  lc.unsubscribe(subD)

