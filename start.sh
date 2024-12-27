#!/bin/bash

# Step 1: Create a directory for Chrome
mkdir -p $HOME/chrome
cd $HOME/chrome

# Step 2: Download Google Chrome Debian package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Step 3: Extract the Chrome package without installing it
ar x google-chrome-stable_current_amd64.deb
tar -xf data.tar.xz

# Step 4: Update PATH to include the Chrome binary
export PATH=$HOME/chrome/opt/google/chrome:$PATH
find / -name Bot.py
python3 Bot.py