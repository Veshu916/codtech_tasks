import socket
import subprocess
import os

def scan_open_ports(target, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, port))
            open_ports.append(port)
        except:
            pass
        finally:
            s.close()
    return open_ports

def check_software_version(software):
    try:
        result = subprocess.run([software, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        version = result.stdout.decode('utf-8').strip()
        return version
    except FileNotFoundError:
        return None

def check_misconfigurations():
    misconfigurations = []
    # Example check: Check if root login is enabled in SSH config
    ssh_config_file = '/etc/ssh/sshd_config'
    if os.path.exists(ssh_config_file):
        with open(ssh_config_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if 'PermitRootLogin yes' in line:
                    misconfigurations.append('Root login enabled in SSH config.')
    return misconfigurations

def main():
    target = '127.0.0.1'
    ports = [22, 80, 443, 8080]

    print("Scanning for open ports...")
    open_ports = scan_open_ports(target, ports)
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found.")

    print("\nChecking for outdated software versions...")
    software_list = ['python3', 'curl', 'git']
    for software in software_list:
        version = check_software_version(software)
        if version:
            print(f"{software} version: {version}")
        else:
            print(f"{software} is not installed.")

    print("\nChecking for common misconfigurations...")
    misconfigurations = check_misconfigurations()
    if misconfigurations:
        print("Misconfigurations found:")
        for misconfig in misconfigurations:
            print(f"- {misconfig}")
    else:
        print("No misconfigurations found.")

if __name__ == "__main__":
    main()
