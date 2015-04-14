import lcm
import time

from lilylcm import L04Dan

lc = lcm.LCM()

msg = L04Dan()
msg.name = "Dark n Chunky"

def my_handler(channel, data):
  lc.publish("04DAN", msg.encode())
  return "Received message from %s" % channel
  
subscription = lc.subscribe("05EBOLA", my_handler)
  
try:
  while True:
      lc.handle()
except Keyboardinterrupt:
  pass
    
lc.unsubscribe(subscription)

