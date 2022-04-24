# IoT_Scanner

Introduction:  

Anybody who is concerned with WIFI security and personal computer/laptop. For Example, Fleming college, McDonald’s, Tim Horton, hotels, and home network. The IoT Tester can help scan the network you are connected to and list all vulnerabilities so we can be protected and detect any potential threat. This device offers detailed information (name, range, IP address, etc.) of all connected devices with detected vulnerabilities by checking and comparing from the in-built database.  

What makes this tester superior to most others on the market is its ability to detect Bluetooth devices not just devices on Wi-Fi networks. 

This tester will be connected to your system and performance will depend on your system specification. 

Identifies devices on the network 

-easy use  

-mechanical button 

-fast responsive execution  


IoT Tester v.2.0 specs: 

•	The latest model of Raspberry Pi, the 4B with 4GB RAM 

•	Our very own HighPi case for Raspberry Pi 4 

•	USB-C Power Supply, 5.1V 3.0A, Black, UL Listed 

•	64GB Micro SD Card Pre-Programmed with Raspbian 

•	HDMI A male to Micro D male cable, 3ft 

•	USB card reader for microSD cards 

•	Aluminum Heatsink for Raspberry Pi 4B (3-Pack) 

•	GPIO Interface Board with Ribbon Cable (T-Cobbler Plus) 

•	Full-Size Breadboard (830 points) 

•	2 x RGB LED 

•	2 x Red LEDs 

•	2 x Green LEDs 

•	2 x Yellow LEDs 

•	2 x Blue LEDs 

•	2 x Push Button Switches 

•	10 x 220 Ohm Resistors 

•	10 x 10K Ohm Resistors 

•	20 x Male to Male Jumper Wires 

•	20 x Male to Female Jumper Wires 

•	Printed PiShop Raspberry Pi Quick Start Guide 

################################################################

Summary:  

Scans the network and lists all device IP addresses and MAC addresses. It will then allow the user to select a device and will be able to track this device’s detailed info This could help make the network more secure and be aware of potential threats.   

The main objective is to map out the IoT devices and their associated vulnerability.  

List all networks Wi-Fi and Bluetooth devices with name and IP address 

Compare scanned results for vulnerabilities by looking into the database 

We used python3 to create scripts and execute them to achieve the goal 

First, we divided the project into parts so we can work on it individually which would be  

Execution script 

Scanning network script Wi-Fi and Bluetooth  

Database to store scanned results  

Scanning vulnerabilities with NVD  

Result email delivery  

################################################################

Getting started 

Setting up your Raspberry Pi IoT Tester 

To get started with your IoT Tester you will need the following accessories: 

A computer monitor, or television, most should work as a display but for best results, you should use a display HDMI input. You’ll also need an appropriate display cable, to connect your monitor to your IoT Tester. 

A computer keyboard and mouse  

Any standard USB keyboard and mouse will work with your IoT Tester 

Wireless keyboards and mice will work if already paired. 

For keyboard layout configuration options see raspi-config. 

################################################################

Connecting a Display  

Unless you are setting up your Tester to operate headless, for regular use you will want to plug the IoT Tester into a display: either a computer monitor or a television.  

################################################################

SD Cards for Raspberry Pi/IoT Tester 

Raspberry pi computers use a micro-SD card, except for very early models which use full-sized SD cards. 

Recommended capacity  

We recommend using an SD card of 8GB or greater capacity with raspberry pi OS. If you are using the lite version of raspberry Pi OS, you can use a 4GB card. It also comes with our inbuilt application to scan all of your networks including the Bluetooth devices.  

################################################################

Dependencies and modules installation 

With our IoT Tester, the user needs to install dependencies and modules for a successful thorough scan for best results. 

################################################################

Step by Step instructions:

1- User needs to have our file "setup.sh".
When running this file for the first time, it will install the latest system update (update the packages), Python3, Python-pip3, and some Python modules required to complete the scan and run our app.
The modules include: Tkinter (used for the gui), bluetooth (to scan for Bluetooth devices), nvdlib (to get info about vulnerabilities and CVEs from the NVD Library).

2- Double click the file "setup.sh"
	NOTE: If the file opens as a text file, you need to change the "Execute permissions" to anyone so you can run the file in your machine.
	There are two ways to change the permissions (The first way is much easier):
		1- Right Click the file (setup.sh) > Properties > Go to Permissions tab > Change "Execute" to "Anyone".
		2- Right Click the file (setup.sh) > Properties > Under General > Copy the location of the file (path) > On the top left corner or down left corner > Click your Raspberry Pi logo > Choose "Accessories" > Terminal > Type without brackets (cd AND_THEN_PASTE_THE_COPIED_LOCATION) > Hit Enter
			Your text or command should look like this "cd /home/pi/Desktop/ASA_IoT"
				> Now type without brackets (chmod +x setup.sh) > Hit Enter

3- Go back and Double click the file "setup.sh" > Choose "Execute" or "Execute in Terminal"
	If you want to see the process, choose "Execute in Terminal".

4- Wait for 2-5 minutes (depends on the packages that are being installed)

5- The scan will restart after installing all the packages and modules.

6- When the scan completes, our GUI app will start.

7- Click "Click here to see the results" to see the full scanning results.
	The results will be shown on the second window.
	The results include all connected devices (Wifi and Bluetooth) with there IP Addresses and Mac Addresses, and the vulnerabilities associated to them.

8- You may wish to save these results your own. To do so, Click on the second window that has the results > CTRL+A (to select all) > CTRL+C (to copy the selected texts) > Create a new text file and name it whatever you want > CTRL+V (To paste the texted in the text file)

9- Close the app by clicking the "Exit Program" button.

10- Our email app will start > You can follow the instructions on the second window or complete here.
	- In order to be able to send emails via this app, you need to TURN ON "less secure apps" on your Google account.
	- This is required because our email app created using Python and Python is considered as a third-party-app.
	- Go to the following link https://myaccount.google.com/lesssecureapps > Sign in to your Google Account > Turn the option ON (Should be OFF by default) > Go back to the email app
	- Fill the form with your info:
		. Email: The Google account that you used on the previous step.
		. Password: The same Google account password.
		. To: The email address you are sending the file to.
		. Subject: Any
		. Body: Any
	- Click "Attach" and select the file "results.txt"
		. You may wish to attach a file called "rev.txt". This file contains a list of all connected devices.
	- Click "Send"

11- Go to your email address that you sent the file to > Open the email your received > Click the attached file/files > The file "results.txt" contains all the vulnerabilities associated to your devices.

12- You can copy one of these CVEs and search for them on Google or NATIONAL VULNERABILITY DATABASE (NVD) at https://nvd.nist.gov/

13- THE NATIONAL VULNERABILITY DATABASE contains a list of all CVEs. Each CVE includes Details/Description, Severity, Solutions, and more.

14- You can follow the solutions to secure that device.
