#!/usr/bin/env bash
set -o errexit

# Upgrade pip first
python -m pip install --upgrade pip

# Install Python packages (Pillow will handle its own dependencies)
pip install --no-cache-dir -r requirements.txt
