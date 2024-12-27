#!/bin/bash

# Update package list and install Chrome with sudo
sudo apt-get update
sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb

python3 Bot.py