# DevOps Fetch

`devopsfetch` is a powerful tool for monitoring and retrieving system information, designed for DevOps professionals. It collects and displays data on active ports, Docker images and containers, Nginx configurations, user logins, and activities within a specified time range. It also includes a systemd service for continuous monitoring and logging.

## Features

- **Active Ports and Services**: Display all active ports and associated services.
- **Docker Information**: List all Docker images and containers, and provide details about specific containers.
- **Nginx Configuration**: Show all Nginx domains and their ports, with detailed configuration for specific domains.
- **User Information**: List users and their last login times, with details about specific users.
- **Time Range Filtering**: Display activities within a specified time range.

## Installation

### Prerequisites

- Python 3.9 or higher
- Docker (optional)
- sudo privileges for systemd service setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/devopsfetch.git
cd devopsfetch
```
### Step 2: Set Up a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install Dependencies
```
pip install -r requirements.txt
```
### Step 4: Install Systemd Service
- Run the installation script to set up the service and install dependencies
```
chmod +x install.sh
./install.sh
```
### Step 5: Configure Systemd Service
- Ensure the devopsfetch.service file is correctly configured
```
[Unit]
Description=DevOps Fetch Service
After=network.target

[Service]
ExecStart=/path/to/venv/bin/python /path/to/devopsfetch.py
Restart=always
User=root
Environment=PATH=/path/to/venv/bin
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```
- ** Replace /path/to/venv/bin/python and /path/to/devopsfetch.py with the actual paths.

### Running Locally
```
python devopsfetch.py -p           # List active ports and services
python devopsfetch.py -d           # List Docker images and containers
python devopsfetch.py -n example.com  # Display Nginx configuration for a domain
python devopsfetch.py -u username  # Display user information
python devopsfetch.py -t "start_time end_time"  # Display activities within a time range
```
### Using Docker
- ** Build the Docker Image
```
docker build -t devopsfetch .
```
- ** Run the Container
```
docker run --rm -it devopsfetch -p
docker run --rm -it devopsfetch -d
docker run --rm -it devopsfetch -n example.com
docker run --rm -it devopsfetch -u username
docker run --rm -it devopsfetch -t "start_time end_time"
```
- Replace example.com, username, and "start_time end_time" with appropriate values
### Systemd Service
- Start and Enable Service
```
sudo systemctl daemon-reload
sudo systemctl enable devopsfetch.service
sudo systemctl start devopsfetch.service
```
### Check status
``` sudo systemctl status devopsfetch.service
```