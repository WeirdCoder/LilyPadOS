from HIH6130.io import HIH6130

rht = HIH6130()
rht.read()
a = rht.read()
print rht.rh
print ("Timestamp: {0}\tRH: {1}\tTemp: {2} degC".format(rht.timestamp, rht.rh, rht.t))

