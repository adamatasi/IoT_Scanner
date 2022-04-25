#!/bin/bash

# Before running the script, check the video at https://github.com/adamatasi/IoT_Scanner
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

pip3 install shodan
python3 -m pip install shodan
python3 -m pip install nvdlib

tput setaf 2; echo "Done"
sleep 1
tput sgr0; echo ""

sudo apt install python3-bluez

# install the required modules using pip3
sudo pip3 install nvdlib
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install pillow
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo apt-get install bluetooth libbluetooth-dev
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo python3 -m pip install pybluez
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install python-nmap
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install pyfiglet
tput setaf 2; echo "Done"
tput sgr0; echo ""

sudo pip3 install tkhtmlview
tput setaf 2; echo "Done"
tput sgr0; echo ""

# Installing Tkinter (GUI)
sudo apt-get install python3-tk
tput setaf 2; echo "Done"
tput sgr0; echo ""

# install git (This will be used to download files from GitHub)
sudo apt install git

# Download the IoT Scanner
git clone https://github.com/adamatasi/IoT_Scanner.git

tput setaf 2; echo "Done"
tput sgr0; echo ""

# Change the directory to the downloaded folder
cd IoT_Scanner

sleep 1
tput setaf 2; echo "Setup has been completed"
sleep 1
tput sgr0; echo ""
tput setaf 2; echo "Running the Scanner...."
sleep 1
tput sgr0; echo ""
tput setaf 2; echo "It might take a few minutes"
sleep 1
tput sgr0; echo ""

# Running the script
python3 gui.py

sleep 1

tput setaf 2; echo "Almost Done"

sleep 1
