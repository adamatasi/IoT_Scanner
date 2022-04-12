#!/bin/bash

echo ""
# Message 1
tput setaf 2; echo "Installing all the required programs and modules used in this project"
sleep 2
echo ""
# Message 2
tput setaf 2; echo "The setup may take a few minutes"
sleep 2
echo ""

# Update the system
sudo apt update && sudo apt upgrade -y

tput setaf 2; echo "Done"
sleep 1
tput sgr0; echo ""

# Install Pyhton3
sudo apt install python3

tput setaf 2; echo "Done"
sleep 1
tput sgr0; echo ""

# Upgrade Python3 (in case if it is installed)
sudo apt install --upgrade python3

tput setaf 2; echo "Done"
sleep 1
tput sgr0; echo ""

# install pip3
sudo apt install python3-pip

tput setaf 2; echo "Done"
sleep 1
tput sgr0; echo ""

# install the required modules using pip3
sudo pip3 install nvdlib
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install pillow
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install pybluez
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install python-nmap
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install pyfiglet
tput setaf 2; echo "Done"
tput sgr0; echo ""

# Installing Tkinter (GUI)
sudo apt-get install python3-tk
tput setaf 2; echo "Done"
tput sgr0; echo ""

# install git (This will be used to download files from GitHub)
sudo apt install git
# Change the directory
cd ~/Desktop






# We should give this file "setup.sh" to the user
# We need to make some changes here GUYS:
# First, we need the full path of the "IoT.zip" file
# The "IoT.zip" file will contain 2 files "logo.png" and "IoT_Scanner.py"

# Download the IoT Scanner
git clone https://github.com/adamatasi/IoT_Scanner.git

tput setaf 2; echo "Done"
tput sgr0; echo ""

# Change the directory to the downloaded folder
cd ~/Desktop/IoT_Scanner

tput setaf 2; echo "Done"
tput sgr0; echo ""

# Running the script
python3 IoT_Scanner.py
