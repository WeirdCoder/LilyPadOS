import lcm
from lilylcm import 03Citrus

def my_handler(channel, data):
    msg = 03Citrus.decode(data)
    print("Received message on channel /"%s/"" % channel)
    print("  value  = %s" % str(msg.value))
    print("")
    
lc = lcm.LCM()
subscription = lc.subscribe("03Citrus", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass
    
lc.unsubscribe(subscription)
