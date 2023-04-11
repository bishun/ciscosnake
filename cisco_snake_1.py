import paramiko

# Define the file names for IP addresses and commands
ip_file = 'ip_addresses.txt'
command_file = 'commands.txt'

# Define the username and password for the Cisco devices
username = 'username'
password = 'password'

# Create an SSH client object
ssh = paramiko.SSHClient()

# Automatically add the host key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Open the IP address file and read the addresses into a list
with open(ip_file) as f:
    ip_addresses = f.read().splitlines()

# Open the command file and read the commands into a list
with open(command_file) as f:
    commands = f.read().splitlines()

# Iterate over the list of IP addresses and run the specified commands on each device
for ip_address in ip_addresses:
    print(f'Connecting to {ip_address}')
    try:
        # Connect to the Cisco device using SSH
        ssh.connect(ip_address, username=username, password=password)

        # Run the specified commands on the Cisco device
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.readlines()
            print(f'Output for command "{command}":\n' + '\n'.join(output))

        # Close the SSH connection
        ssh.close()

    except paramiko.AuthenticationException:
        print(f'Authentication failed for {ip_address}')
    except paramiko.SSHException as e:
        print(f'Unable to establish SSH connection to {ip_address}: {str(e)}')
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f'Unable to connect to {ip_address}: {str(e)}')