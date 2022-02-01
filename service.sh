#!/bin/sh
sudo chmod 777 main
sudo cp toggel.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable toggel.service
