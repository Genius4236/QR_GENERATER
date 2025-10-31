#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies for Pillow
apt-get update
apt-get install -y python3-dev python3-pip python3-venv
apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt