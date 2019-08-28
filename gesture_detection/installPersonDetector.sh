#!/bin/bash
# NOTE - DON'T run as sudo unless you know what you're doing. You will be prompted for sudo access when needed.
# This script will install the person detector and create a systemd service for it to run at startup

# SUDO_CONTINUED="0"

# Check to make sure they are not running as sudo
# if [ "$EUID" -eq 0 ]
# then
#     echo "WARNING: need to call this script as a normal user, not as sudo!"
#     echo "Certain python libraries are recommended to be installed as a normal user!"
#     read -p "Would you like to continue anyway? Type 'c' to continue (only if you know what you're doing!) or 'q' to quit (recommended)?" -n 1 -r
#     echo '' # move to a new line
#     # Check to see if they wish to continue anyway
#     if [[ ! $REPLY =~ ^[Cc]$ ]]
#     then
#         exit 1
#     fi
#     # Keep track that they are running as sudo and continued anyway
#     SUDO_CONTINUED="1"
# fi

# if [ $SUDO_CONTINUED -eq 1 ]
# then
#     echo "Installing pynput python library as sudo."
#     pip install pynput
# else
#     echo "Installing pynput python library as normal user."
#     pip install --user pynput
# fi

echo 'Removing old service file (uses sudo)'
sudo rm magic-mirror-person-detector.service

echo 'Generating Systemd Service file'
echo '[Unit]
Description=Magic Mirror Person Detector
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 '$PWD'/personDetector.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target' > magic-mirror-person-detector.service

echo 'Copying Service file into /lib/systemd/system (uses sudo)'
sudo cp magic-mirror-person-detector.service /lib/systemd/system/magic-mirror-person-detector.service

echo 'Enabling person detector to start at bootup (uses sudo)'
sudo systemctl enable magic-mirror-person-detector

#Check to see if they want to start the Person Detector now.
while true; do
    read -p "Would you like to start the Person Detector now (uses sudo)? (Type 'yes' to start now or 'no' to wait until reboot): " yn
    case $yn in
        [Yy]* ) echo 'Starting Person Detector'; sudo systemctl start magic-mirror-person-detector; exit;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done