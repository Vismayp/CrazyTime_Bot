#!/bin/bash

# Install dependencies
apt-get update && apt-get install -y wget unzip libnss3 libatk-bridge2.0-0 libcups2 libxrandr2 libxkbcommon-x11-0 libgbm1

# Run the application
python Bot.py