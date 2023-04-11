# ciscosnake v0.1 alpha

Batch Command Automation for Cisco Hardware

This program reads IP addresses from a file named ip_addresses.txt and commands from a file named commands.txt.
The program uses a with statement to open each file and read the contents into a list using the splitlines() method.

The program then iterates over the list of IP addresses and attempts to establish an SSH connection to each device.
For each device, it runs the specified commands and prints the output to the console.
The program handles exceptions for authentication failures, SSH connection failures, and no valid connections.

Replace username and password with the appropriate values for your Cisco devices. Create a file named ip_addresses.txt
and list each IP address on a separate line. Create a file named commands.txt and list each command on a separate line.
When you run the program, it will read the IP addresses and commands from the files and iterate over the IP addresses
to run the commands on each device.
