
import lcm
import time

from lilylcm import #channel

lc = lcm.LCM()

msg = #instance
msg.latitude = 0.0
msg.longitude = 0.0

def my_handler(channel, data):
	#define the function here

subscription = lc.subscribe("SOME-CHANNEL", my_handler)

lc.publish("SOME-CHANNEL", msg.encode())

try:
	while True:
		lc.handle()
except Keyboardinterrupt:
	pass
lc.unsubscribe(subscription)


