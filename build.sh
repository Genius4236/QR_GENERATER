#!/usr/bin/env bash
set -o errexit

# Install system dependencies for Pillow
apt-get update
apt-get install -y \
    python3-dev \
    python3-pip \
    python3-setuptools \
    libjpeg-dev \
    zlib1g-dev

# Upgrade pip
python -m pip install --upgrade pip

# Install Python packages
pip install --no-cache-dir -r requirements.txt