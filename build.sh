#!/usr/bin/env bash
set -o errexit

# Update pip
python -m pip install --upgrade pip

# Install system dependencies
apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    python3-venv \
    gcc \
    libjpeg-dev \
    zlib1g-dev

# Install Python packages
pip install -r requirements.txt