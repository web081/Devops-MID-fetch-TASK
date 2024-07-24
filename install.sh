#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create systemd service file
cat <<EOF | sudo tee /etc/systemd/system/devopsfetch.service
[Unit]
Description=DevOps Fetch Service
After=network.target

[Service]
ExecStart=/Users/mac/Desktop/screenshot/internship app/devopsfetch/venv/bin/python /Users/mac/Desktop/screenshot/internship app/devopsfetch/devopsfetch.py
Restart=always
User=root
Environment=PATH=/Users/mac/Desktop/screenshot/internship app/devopsfetch/venv/bin
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable devopsfetch.service
sudo systemctl start devopsfetch.service

echo "DevOps Fetch Service installed and started."
