from netmiko import ConnectHandler
import getpass

username = input('Digite seu usuário: ')
password = getpass.getpass('Digite sua senha: ')
cisco = {
    'device_type': "cisco_ios",
    'host': 'x.x.x.x',
    'username': username,
    'password': password,
}

connection = ConnectHandler(**cisco)

list_command = ['show ip route', 'show interface desc', 'show clock']

for command in list_command:
    print(f'\n Enviando: {command} \n')
    output = connection.send_command(command)
    print (output)


connection.disconnect()

          
    
     
