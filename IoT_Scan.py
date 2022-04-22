import os 
import pyfiglet
import socket
from datetime import datetime





#gets the local address


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
address= (s.getsockname()[0])
s.close()

adr = address.split('.')
fa = adr[0]+'.'+adr[1] + '.' + adr[2] + '.' + '1/24'


ascii_banner = pyfiglet.figlet_format("IoT SCANNER")
print('Warning this device needs to be connected to the network and can only scan for active devices \n')


#use the arp-scan to get IoT devices 
os.system("sudo arp-scan --retry=4 --ignoredups -I wlan0 --localnet > rev.txt")

#store found devices and count device found and stop before last 3 lines
devices = {}
count = 0 
stop = 0 


f = open('rev.txt')
stop = len(f.readlines())
f.close()
stop = stop - 4
with open('rev.txt', 'r') as file: 
	for i in range(2): #skip first 2 lines
		file.readline()
	
	for line in file:
		count += 1 
		items=line.split()
		if count == stop:
			break
		if items: #add to dic
			name = ''.join(items[2:])
			if count in devices:
				print('error unknown')
			else:
				devices[count] = {'ip': items[0], 'mac': items[1], 'dev_name': name}
		
#scans port for each device found
def port(address):
	for port in range(1,445):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((address,port))
		if result ==0:
			print("Port {} status: open".format(port))
		s.close()
		
#print each device found with their active ports

breakpoint = stop -1 
def run():
	global c
	c = 0
	for x in range(0, count): #stops at last line
		c+=1	
		print('Scanning device ' + devices[c]['ip'], '| MAC address ' + devices[c]['mac'], '| Device name ' + devices[c]['dev_name'])
		#port(devices[c]['ip'])
		if c == breakpoint:
			break

print(ascii_banner)
print("~" * 50)
print("Scanning Target")
print("Scanning started at:" + str(datetime.now()))	
print("~" * 50)
run()
print('Devices found '+ str(c))

