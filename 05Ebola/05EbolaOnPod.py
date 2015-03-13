import lcm
import time

from lilylcm import L05Ebola

lc = lcm.LCM()

msg = L05Ebola()
msg.cured = True

def my_handler(channel, data):
   msg = L05Ebola.decode(data)
   if msg.cured:
       print(":( I got Ebola from the Plane")
   


print "achoo!"
lc.publish("05EBOLA",msg.encode())

subscription = lc.subscribe("PLANE_05EBOLA",my_handler)
try:
    while True:
        lc.handle()
except Keyboardinterrupt:
    pass
lc.unsubscribe(subscription)
