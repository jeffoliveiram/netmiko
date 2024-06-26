from netmiko import ConnectHandler
import getpass

username = input('Digite seu usuário: ')
password = getpass.getpass('Digite sua senha: ')
f5 = {
    'device_type': 'f5_ltm',
    'host': 'x.x.x.x',
    'username': username,
    'password': password,
}

connection = ConnectHandler(**f5)

output = connection.send_command('show sys version')
print(output)

connection.disconnect()