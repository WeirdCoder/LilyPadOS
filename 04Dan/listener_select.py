import select
import lcm
from lilylcm import 04Dan

def my_handler(channel, data):
    msg = 04Dan.decode(data)
