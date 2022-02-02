#!/bin/sh
sudo chmod 777 main.py
sudo cp toggel.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable toggel.service
