import lcm
import time

import L04Dan

lc = lcm.LCM()

msg = L04Dan()
msg.name = "Dark n Chunky"

def my_handler(channel, data):
  print("Received message from 04")
  
subscription = lc.subscribe("04DAN", myhandler)
  
lc.publish("04DAN", msg.encode())
  
try:
  while True:
      lc.handle()
except Keyboardinterrupt:
  pass
    
lc.unsubscribe(subscription)

