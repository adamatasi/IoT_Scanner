#IoT_Scanner
Step by Step instructions:

You can either watch the video to see how it's done OR follow the instructions below.

Video Link: https://youtu.be/6sr7vAXrZN4

Instructions: 1- User needs to have our file "setup.sh". When running this file for the first time, it will install the latest system update (update the packages), Python3, Python-pip3, and some Python modules required to complete the scan and run our app. The modules include: Tkinter (used for the gui), bluetooth (to scan for Bluetooth devices), nvdlib (to get info about vulnerabilities and CVEs from the NVD Library).

2- Double click the file "setup.sh" NOTE: If the file opens as a text file, you need to change the "Execute permissions" to anyone so you can run the file in your machine. There are two ways to change the permissions (The first way is much easier): 1- Right Click the file (setup.sh) > Properties > Go to Permissions tab > Change "Execute" to "Anyone". 2- Right Click the file (setup.sh) > Properties > Under General > Copy the location of the file (path) > On the top left corner or down left corner > Click your Raspberry Pi logo > Choose "Accessories" > Terminal > Type without brackets (cd AND_THEN_PASTE_THE_COPIED_LOCATION) > Hit Enter Your text or command should look like this "cd /home/pi/Desktop/ASA_IoT" > Now type without brackets (chmod +x setup.sh) > Hit Enter

3- Go back and Double click the file "setup.sh" > Choose "Execute" or "Execute in Terminal" If you want to see the process, choose "Execute in Terminal".

4- Wait for 2-5 minutes (depends on the packages that are being installed)

5- The scan will restart after installing all the packages and modules.

6- When the scan completes, our GUI app will start.

7- Click "Click here to see the results" to see the full scanning results. The results will be shown on the second window. The results include all connected devices (Wifi and Bluetooth) with there IP Addresses and Mac Addresses, and the vulnerabilities associated to them.

8- You may wish to save these results your own. To do so, Click on the second window that has the results > CTRL+A (to select all) > CTRL+C (to copy the selected texts) > Create a new text file and name it whatever you want > CTRL+V (To paste the texted in the text file)

9- Close the app by clicking the "Exit Program" button.

10- Our email app will start > You can follow the instructions on the second window or complete here. - In order to be able to send emails via this app, you need to TURN ON "less secure apps" on your Google account. - This is required because our email app created using Python and Python is considered as a third-party-app. - Go to the following link https://myaccount.google.com/lesssecureapps > Sign in to your Google Account > Turn the option ON (Should be OFF by default) > Go back to the email app

		NOTE: We recommend to go back to https://myaccount.google.com/lesssecureapps and turn "less secure apps" OFF after sending the email.
		NOTE: Our next version v2.0 will not ask the user to enter the "sender email address". User will have to enter the "receiver email address" only.
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
