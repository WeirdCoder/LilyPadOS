import lcm
from lilylcm import 04Dan

def my_handler(channel, data):
    msg = 04Dan.decode(data)
    print("Received message on channel /"%s/"" % channel)
    print("  value  = %s" % str(msg.value))
    print("")
    
lc = lcm.LCM()
subscription = lc.subscribe("EXAMPLE", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass
    
lc.unsubscribe(subscription)
