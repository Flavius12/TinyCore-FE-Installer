#!/bin/sh
sudo python3 /usr/local/tcfe-setup/InstallerApp.py
EXIT_CODE=$?
sudo python3 /usr/local/tcfe-setup/RebootInfoApp.py ${EXIT_CODE}
sudo reboot
