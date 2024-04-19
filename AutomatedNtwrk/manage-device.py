from netmiko import ConnectHandler

# Device Setup
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'admin123',
    'secret': 'secret123',  # Enable password
}

# Establish SSH Connection
net_connect = ConnectHandler(**device)
net_connect.enable()

# Sending configuration commands
config_commands = [
    'hostname MyRouter',
    'interface FastEthernet0/1',
    'ip address 192.168.1.10 255.255.255.0',
    'no shutdown'
]
output = net_connect.send_config_set(config_commands)
print(output)

# Disconnect
net_connect.disconnect()
print("Device configured successfully.")
