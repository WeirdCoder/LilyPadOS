import lcm
import time

from lilylcm import L05Ebola

lc = lcm.LCM()

msg = L05Ebola()
msg.cured = True

def my_handler(channel, data):
   print("Received message from 04!")

subscription = lc.subscribe("04DAN",my_handler)

while True:
    lc.publish("05EBOLA",msg.encode())

try:
    while True:
        lc.handle()
except Keyboardinterrupt:
    pass
lc.unsubscribe(subscription)
