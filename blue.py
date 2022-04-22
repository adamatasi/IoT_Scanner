from bluetooth import *

print ("Scanning bluetooth devices...")

nearby_devices = discover_devices(lookup_names = True)

print ("bluetooth devices found %d" % len(nearby_devices))

c = 0

dev = {}
for name, addr in nearby_devices:
     #print (" %s - %s" % (addr, name))
     c += 1

     dev[c] = {'ip': addr, 'mac': name}

 
cp = c + 1 

for x in range(1, cp):
	print('device found:', dev[x]['ip'])
	print('mac address:', dev[x]['mac'])	
	if x == c:
		break
		

