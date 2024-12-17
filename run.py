import paramiko
import csv
import os

# File paths
inventory_file = "inv.csv"
commands_file = "cmd.txt"

# Function to connect to a switch and execute commands
def execute_commands_on_switch(hostname, ip, username, password, commands):
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=10)

        # Prepare the log file
        log_file = f"{hostname}.log"
        with open(log_file, "w") as log:
            for command in commands:
                stdin, stdout, stderr = ssh.exec_command(command)
                output = stdout.read().decode()
                error = stderr.read().decode()

                # Write output to the log file
                log.write(f"Command: {command}\n")
                log.write(output)
                if error:
                    log.write(f"Error: {error}\n")
                log.write("\n")

        print(f"Commands executed successfully on {hostname}. Logs saved to {log_file}.")
        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {hostname} ({ip}): {e}")

# Read the inventory file
def read_inventory(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        devices = [row for row in reader]
    return devices

# Read the commands file
def read_commands(file_path):
    with open(file_path, "r") as cmdfile:
        commands = cmdfile.readlines()
    return [cmd.strip() for cmd in commands]

if __name__ == "__main__":
    # Ensure necessary files exist
    if not os.path.exists(inventory_file):
        print(f"Inventory file {inventory_file} not found.")
        exit(1)
    if not os.path.exists(commands_file):
        print(f"Commands file {commands_file} not found.")
        exit(1)

    # Load inventory and commands
    devices = read_inventory(inventory_file)
    commands = read_commands(commands_file)

    # Execute commands on each device
    for device in devices:
        hostname = device.get("hostname")
        ip = device.get("ip")
        username = device.get("user")
        password = device.get("pass")

        if not all([hostname, ip, username, password]):
            print(f"Invalid entry in inventory file: {device}")
            continue

        execute_commands_on_switch(hostname, ip, username, password, commands)

