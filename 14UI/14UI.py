import lcm
import time
import socket
import json

from lilylcm import L06Depth
from lilylcm import L07Humidity
from lilylcm import L08Tempurature
from lilylcm import L14LEDs
from lilylcm import L16ChargerCommand
from lilylcm import L19DockCommand

lc = lcm.LCM()
HOST = ' '#input IP Address
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
dic = {'Hum': 0, 'Temp': 0, 'Dep': 0, 'Sat': 0, 'Charge': 0, 'Mag': 0}
def my_handler(channel, data):
  if channel == 

subDep = lc.subscribe("POD_Depth", my_handler)
subHum = lc.subscribe("POD_Humidity", my_handler)
subTemp = lc.subscribe("POD_Tempurature", my_handler)
subSat = lc.subscribe("POD_LED", my_handler) 
subChar = lc.subscribe("POD_Charge", my_handler)
subMag = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    lc.handle()
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(sub)

