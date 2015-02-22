import lcm

from lilylcm import 04Dan

lc = lcm.LCM()

msg = 04Dan()
msg.count = int #value
msg.done = boolean #value
msg.value = double #value
msg.name = str #value
msg.cured = boolean #value

lc.publish("EXAMPLE", msg.encode())
