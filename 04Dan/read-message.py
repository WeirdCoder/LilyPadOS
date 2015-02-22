import sys
import lcm

from lilylcm import 04Dan

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)
    
log = lcm.EventLog(sys.argv[1], "r")

for event in log:
    if event.channel == "EXAMPLE":
        msg = 04Dan.decode(event.data)
        
        print(Message:")
        print("  count  = %s" % str(msg.count))
        print("  done   = %s" % str(msg.done))
        print("  value  = %s" % str(msg.value))
        print("  name   = %s" % str(msg.name))
        print("  cured  = %s" % str(msg.cured))
        print("")