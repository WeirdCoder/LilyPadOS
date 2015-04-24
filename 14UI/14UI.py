import lcm
import time

from lilylcm import L06Depth
from lilylcm import L07Humidity
from lilylcm import L08Tempurature
from lilylcm import L14LEDs
from lilylcm import L16ChargerCommand
from lilylcm import L19DockCommand

lc = lcm.LCM()

def my_handler(channel, data):

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

