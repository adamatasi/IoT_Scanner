#! /bin/bash

echo ""
# Message 1
tput setaf 2; echo "Installing all the required programs and modules used in this project"
sleep 3
echo ""
# Message 2
tput setaf 2; echo "The setup may take a few minutes"
sleep 3
echo ""

# Update the system
sudo apt update && sudo apt upgrade -y
# Install Pyhton3
sudo apt install python3
# Upgrade Python3 (in case if it is installed)
sudo apt install --upgrade python3
# install pip3
sudo apt install python3-pip
# install the required modules using pip3
sudo pip3 install -r requirements.txt
# install git (This will be used to download files from GitHub)
sudo apt install git
# Download the IoT Scanner
git clone https://iot.zip && unzip IoT.zip && python3 /backup/modules.py
# Change the directory to the downloaded folder
cd /home/<user>/Downloads/IoT
# Running the script
python3 test.py
