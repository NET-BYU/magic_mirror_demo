#!/bin/bash
# NOTE - DON'T run as sudo. You will be prompted for sudo access when needed.
# This script will install the person detector and create a systemd service for it to run at startup
pip install --user pynput
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
echo 'Copying Service file into /lib/systemd/system (requires sudo)'
sudo cp magic-mirror-person-detector.service /lib/systemd/system/magic-mirror-person-detector.service
echo 'Enabling person detector to start at bootup (requires sudo)'
sudo systemctl enable magic-mirror-person-detector

while true; do
    read -p "Would you like to start the Person Detector now (requires sudo)? (Type 'yes' to start now or 'no' to wait until reboot): " yn
    case $yn in
        [Yy]* ) echo 'Starting'; sudo systemctl start magic-mirror-person-detector; exit;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done