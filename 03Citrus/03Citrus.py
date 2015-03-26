import lcm
import time

from lilylcm import L03Citrus

lc = lcm.LCM()

msg = L03Citrus()
msg.value = 3.14

def myhandler(channel, data):
  print("Received message from 02")
  lc.publish("03CITIRUS", msg.encode())

subscription = lc.subscribe("02BANANA", myhandler)

lc.publish("03CITIRUS", msg.encode())

try:
  while True:
      lc.handle()
except Keyboardinterrupt:
  pass

