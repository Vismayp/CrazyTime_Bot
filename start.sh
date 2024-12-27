#!/bin/bash

# Update package list and install dependencies
apt-get update && apt-get install -y wget

# Download and install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb || true

python3 Bot.py