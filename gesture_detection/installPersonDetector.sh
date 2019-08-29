#!/bin/bash

echo 'Removing old service file (uses sudo)'
sudo rm magic-mirror-person-detector.service

echo 'Generating Systemd Service file'

echo '#!/bin/bash
(cd '$PWD'; python3 personDetector.py)' > runPersonDetector.sh

chmod +x runPersonDetector.sh

echo '[Unit]
Description=Magic Mirror Person Detector
Wants=network-online.target
After=network-online.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/bin/bash '$PWD'/runPersonDetector.sh
StandardInput=tty-force
Restart=on-failure
RestartSec=5s
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target' > magic-mirror-person-detector.service

echo 'Copying Service file into /lib/systemd/system (uses sudo)'
sudo cp magic-mirror-person-detector.service /lib/systemd/system/magic-mirror-person-detector.service
sudo cp magic-mirror-person-detector.service /etc/systemd/system/magic-mirror-person-detector.service
sudo chmod 644 /etc/systemd/system/magic-mirror-person-detector.service

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