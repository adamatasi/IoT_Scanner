
import sqlite3
conn = sqlite3.connect('IoT.db')
from IoT_Scan import devices, stop
from blue import *
from shodan_search import search

print('*warning this device would need to be connected to an active network to function and can not detect inactive devices. Its only been tested on rpi3 it maybe not work on there versions*')


conn.execute('''CREATE TABLE IF NOT EXISTS DEVICES
		 (ID INT PRIMARY KEY     NOT NULL,
		 IP           TEXT    NOT NULL,
		 MAC            TEXT     NOT NULL,
		 NAME         TEXT);''')

def clear():
	conn.execute('''DELETE FROM DEVICES''')
	#menu()
def scan():

	track = 0

	for i in range (1, stop):
		ip = devices[i]['ip']
		mac = devices[i]['mac']
		name = devices[i]['dev_name']
		conn.execute("INSERT INTO DEVICES (ID,IP,MAC,NAME) \
		      VALUES (?, ?, ?, ?)", (i, ip, mac, name))

		conn.commit()
		track +=1 
		if track == stop:
			break
	
	'''for x in range (1, cp):
		xl = x + stop - 1
		
		if (dev[x]['mac']) in devices.values():
			pass
		else:
			ip = 'bluetooth'
			mac = dev[x]['mac']
			name = dev[x]['ip']
			print(mac, name, xl)
			conn.execute("INSERT INTO DEVICES (ID,IP,MAC,NAME) \
			      VALUES (?, ?, ?, ?)", (xl, ip, mac, name))
		conn.commit()'''
	

	
		


#reads tables
def read():
	
	cursor = conn.execute("SELECT ID, IP, MAC, NAME from DEVICES")
	try:
		for row in cursor:

		   print("ID =", row[0], "IP =", row[1], "MAC =", row[2],"Device Name =", row[3])
		   search(row[1])
		   #print(row[1])
	except OperationalError:
		print('error')
	
#menu()


def start():
	clear()
	scan()
	read()
	

start()

conn.close()
