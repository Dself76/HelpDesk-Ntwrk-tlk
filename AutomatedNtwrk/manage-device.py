from netmiko import ConnectHandler
import logging

# Setup logging
logging.basicConfig(filename='netmiko_log.txt', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

def get_device_details():
    device_type = input("Enter device type (e.g., 'cisco_ios'): ")
    ip_address = input("Enter IP address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    secret = input("Enter enable secret (if any): ")
    return {
        'device_type': device_type,
        'ip': ip_address,
        'username': username,
        'password': password,
        'secret': secret,
    }

def configure_device(device):
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        logger.info(f"Connected to {device['ip']} successfully.")

        # Sending configuration commands
        config_commands = [
            'hostname MyRouter',
            'interface FastEthernet0/1',
            'ip address 192.168.1.10 255.255.255.0',
            'no shutdown'
        ]
        output = net_connect.send_config_set(config_commands)
        print(output)
        logger.info("Configuration commands sent successfully.")

        # Disconnect
        net_connect.disconnect()
        print("Device configured successfully.")
        logger.info("Disconnected successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"Error configuring {device['ip']}: {e}")

def main():
    device = get_device_details()
    configure_device(device)

if __name__ == "__main__":
    main()
