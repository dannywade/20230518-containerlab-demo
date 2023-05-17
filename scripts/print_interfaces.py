from netmiko import ConnectHandler
from getpass import getpass
from rich import print

cli_user = input("Username: ")
cli_pw = getpass()

eos1 = {
    "device_type": "arista_eos",
    "host": "eos1",
    "port": "22",
    "username": cli_user,
    "password": cli_pw,
}

eos2 = {
    "device_type": "arista_eos",
    "host": "eos2",
    "port": "22",
    "username": cli_user,
    "password": cli_pw,
}

device_list = [eos1, eos2]

# Show command that we execute.
command = "show ip int brief"

# Loop through devices and print parsed output
for device in device_list:
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)
    # Print output
    print(f"[italic red1]{device['host']}[/italic red1]", output)
    print()
