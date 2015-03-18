import serial
import lcm
import time

from lilylcm import ##activation signal to turn on docking lights

lc = lcm.LCM()

port = serial.Serial("/dev/ttyACM0", baudrate = 9600) ##change to what ever port the arduino is connected to

sub = lc.subscribe("ACTIVATION", my_handler) ##change to activation class name

try:
  while True:
    port.write(str(sub.activate))
    time.sleep(0.05)
except KeyboardInterrupt:
  lc.unsubscribe(sub)

