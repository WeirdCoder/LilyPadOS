import lcm
import time

from lilylcm import L01Apple 

lc = lcm.LCM()

msg = L01Apple()
msg.count = True

def my_handler(channel, data):
   lc.publish("01Apple",msg.encode())

subscription = lc.subscribe("05Ebola",my_handler)

try:
    while True:
        lc.handle()
except Keyboardinterrupt:
    pass
lc.unsubscribe(subscription)
