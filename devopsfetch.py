import psutil
import subprocess
import socket
from tabulate import tabulate
import argparse

def list_ports():
    try:
        connections = psutil.net_connections(kind='inet')
        port_list = [(conn.laddr.ip, conn.laddr.port, conn.status) for conn in connections if conn.laddr]
        print(tabulate(port_list, headers=["IP Address", "Port", "Status"], tablefmt="grid"))
    except psutil.AccessDenied as e:
        print(f"Access denied: {e}. Run the script with elevated privileges (e.g., sudo).")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_docker():
    try:
        images = subprocess.check_output(['docker', 'images']).decode('utf-8')
        containers = subprocess.check_output(['docker', 'ps', '-a']).decode('utf-8')
        print("Docker Images:\n", images)
        print("Docker Containers:\n", containers)
    except subprocess.CalledProcessError as e:
        print(f"Error listing Docker info: {e}")

def nginx_config(domain=None):
    try:
        if domain:
            config = subprocess.check_output(['nginx', '-T', '-C', f'/etc/nginx/sites-available/{domain}']).decode('utf-8')
            print(f"Nginx Configuration for {domain}:\n", config)
        else:
            config = subprocess.check_output(['nginx', '-T']).decode('utf-8')
            print(f"All Nginx Configurations:\n", config)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching Nginx config: {e}")

def list_users(username=None):
    try:
        if username:
            user_info = subprocess.check_output(['last', '-u', username]).decode('utf-8')
            print(f"User Info for {username}:\n", user_info)
        else:
            users = subprocess.check_output(['last']).decode('utf-8')
            print(f"All Users:\n", users)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching user info: {e}")

def main():
    parser = argparse.ArgumentParser(description="DevOps Fetch Tool")
    parser.add_argument('-p', '--port', type=int, help="Display active ports")
    parser.add_argument('-d', '--docker', action='store_true', help="List Docker images and containers")
    parser.add_argument('-n', '--nginx', type=str, help="Display Nginx configuration for a domain")
    parser.add_argument('-u', '--users', type=str, help="Display user info")
    args = parser.parse_args()

    if args.port:
        list_ports()
    elif args.docker:
        list_docker()
    elif args.nginx:
        nginx_config(args.nginx)
    elif args.users:
        list_users(args.users)
    else:
        print("No valid command provided. Use -h for help.")

if __name__ == "__main__":
    main()
