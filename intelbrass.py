from netmiko import  ConnectHandler
import time

print('Padrão Mac para  Intelbras XX:XX:XX:XX:XX:XX')
mac = input("Digite o MAC para Intelbras: ")

ip = [
    "xxx.xxx.xx.xx",
        ]


brass = [
    {
        "device_type": 'terminal_server',
        "host": ipa,
        "username": "admin",
        "password": "PASS",
        #"fast_cli": True,
        "session_log": "log.txt"

    }
    for ipa in ip
]

for device in brass:
    netCon = ConnectHandler(**device)
    netCon.write_channel("\r")
    time.sleep(1)
    netCon.write_channel("\r")
    time.sleep(1)
    netCon.write_channel("enable\r")
    time.sleep(1)
    netCon.write_channel("show mac address-table address " + mac)
    netCon.write_channel("\r")
    time.sleep(2)
    output = netCon.read_channel()

    print(output)