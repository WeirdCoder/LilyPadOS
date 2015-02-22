import select
import lcm
from lilylcm import 03Citrus

def my_handler(channel, data):
    msg = 03Citrus.decode(data)
    print("Received message on channel /"%s/"" % channel)
    print("  value  = %s" % str(msg.value))
    print("")
    
lc = lcm.LCM()
subscription = lc.subscribe("04Dan", my_handler)

try:
    timeout = 1.5 # amount of time to wait, in seconds
    while True:
        rfds, wfds, efds = select.select([lc.fileno()], [], [], timeout)
        if rfds:
            lc.handle()
            
