from random import *
import lcm

from lilylcm import L06Depth
from lilylcm import L07Humidity
from lilylcm import L08Temperature
from lilylcm import L14LEDs
from lilylcm import L16ChargerCommand
from lilylcm import L19DockCommand
from lilylcm import pod_data_t

lc = lcm.LCM()

msg6 = L06Depth()
msg7 = L07Humidity()
msg8 = L08Temperature()
msg14 = L14LEDs()
msg16 = L16ChargerCommand()
msg19 = L19DockCommand()
msg20 = pod_data_t()

try:
  while True:
  
    i = randint(1,4)
  
    msg6.depth = randint(0, 100)
    msg7.humidity = randint(0, 100)
    msg8.temperature = randint(0, 500)
    msg20.gps = [randint(0,500), randint(0,500)]
    msg20.pod_heading = randint(0, 360)
    msg20.wind_data = [randint(0, 100), randint(0, 360)]
  
    if i == 1:
      msg14.switchOn = True
      msg16.targetState = "Boobies"
      msg19.switchOn = True
    
    elif i == 2:
      msg14.switchOn = True
      msg16.targetState = "Poopie"
      msg19.switchOn = False
    
    elif i == 3:
      msg14.switchOn = False
      msg16.targetState = "Peepee"
      msg19.switchOn = True
      
    elif i == 4:
      msg14.switchOn = False
      msg16.targetState = "Bootie"
      msg19.switchOn = False
    
    lc.publish("POD_Depth",  msg6.encode())
    lc.publish("09I2C_HUMIDITY",  msg7.encode())
    lc.publish("09I2C_TEMP",  msg8.encode())
    lc.publish("POD_LED",  msg14.encode())
    lc.publish("POD_Charge",  msg16.encode())
    lc.publish("POD_Magnet",  msg19.encode())
    lc.publish("pod_data", msg20.encode())

except KeyboardInterrupt:
  pass
