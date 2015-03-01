import lcm

from lilylcm import 04Dan

lc = lcm.LCM()

msg = 04Dan()
msg.name = str "Dark 'n Chunky"

lc.publish("04Dan", msg.encode())
