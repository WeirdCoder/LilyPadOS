import lcm
import time

from lilylcm import L06Depth
from lilylcm import L07Humidity
from lilylcm import L08Tempurature
from lilylcm import L10ChargerCOmplete
from lilylcm import L14LEDs
from lilylcm import L16ChargerCommand
from lilylcm import L19DockCommand

lc = lcm.LCM()

def my_handler(channel, data):

sub = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    lc.handle()
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(sub)

