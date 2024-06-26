from netmiko import ConnectHandler
import getpass

username = input('Digite seu usuário: ')
password = getpass.getpass('Digite sua senha: ')
cisco = {
    'device_type': "cisco_ios",
    'host': '10.99.1.20',
    'username': username,
    'password': password,
}

connection = ConnectHandler(**cisco)

output = connection.send_command('show ip interface brief')
print(output)

connection.config_mode()
print(connection.find_prompt())

config_commands = ['interface Ethernet0/2','ip address 1.1.1.1 255.255.255.0', 'no shut']

config = connection.send_config_set(config_commands)


connection.exit_config_mode()
print(connection.find_prompt())


output = connection.send_command('show ip interface brief')
print(output)

print(connection.save_config())

connection.disconnect()