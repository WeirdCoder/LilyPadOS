import lcm

from lilylcm import L02Banana
def my_handler(channel, data):
    msg=L02Banana()
    msg.done=true
    lc.publish("L02Banana", msg. encode())

lc = lcm.LCM()
subscription = lc.subscribe("L01Apple", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)


