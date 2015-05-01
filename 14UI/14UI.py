import lcm
import time
import socket
import json

from lilylcm import L06Depth
from lilylcm import L07Humidity
from lilylcm import L08Temperature
from lilylcm import L14LEDs
from lilylcm import L16ChargerCommand
from lilylcm import L19DockCommand

lc = lcm.LCM()

#IP = input("What is the servers IP address? ")

HOST = '18.111.101.59'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
dic = {'Hum': 0, 'Temp': 0, 'Dep': 0, 'Sat': 0, 'Charge': 0, 'Mag': 0}

def my_handler(channel, data):
  if channel == "POD_Depth":
    datamsg = L06Depth.decode(data)
    dic['Dep'] = datamsg.depth
  elif channel == "09I2C_HUMIDITY":
    datamsg = L07Humidity.decode(data)
    dic['Hum'] = datamsg.humidity
  elif channel == "09I2C_TEMP":
    datamsg = L08Temperature.decode(data)
    dic['Temp'] = datamsg.temperature
  elif channel == "POD_LED":
    datamsg = L14LEDs.decode(data)
    dic['Sat'] = datamsg.switchOn
  elif channel == "POD_Charge":
    datamsg = L16ChargerCommand.decode(data)
    dic['Charge'] = datamsg.targetState
  elif channel == "POD_Magnet":
    datamsg = L19DockCommand.decode(data)
    dic['Mag'] = datamsg.switchOn
  else:
    pass
  
  s.send(json.dumps(dic))

subDep = lc.subscribe("POD_Depth", my_handler)
subHum = lc.subscribe("09I2C_HUMIDITY", my_handler)
subTemp = lc.subscribe("09I2C_TEMP", my_handler)
subSat = lc.subscribe("POD_LED", my_handler) 
subChar = lc.subscribe("POD_Charge", my_handler)
subMag = lc.subscribe("POD_Magnet", my_handler)

try:
  while True:
    lc.handle()
    time.sleep(0.5)
except KeyboardInterrupt:
  s.close()

