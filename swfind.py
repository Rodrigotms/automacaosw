from netmiko import ConnectHandler
from netmiko.dell.dell_powerconnect import  DellPowerConnectSSH
from netmiko.dell.dell_os10_ssh import  DellOS10SSH


print('\nPadrão Mac para HPs XXXX-XXXX-XXXX')
print('Padrão Mac para DELLs XXXX.XXXX.XXXX')
mac = input("Digite o MAC para HPs: ")
macdell = input("Digite o MAC para DELL: " )

ipaddrs = open('ile.txtf')

hp1 = [
    {
        "device_type": "hp_comware",
        "host": ipa,
        "username": "admin",
        "password": "PASSWORD",
       
    }
    for ipa in ipaddrs
]

ipaddrs2 = open('file.txt')

hp2 = [
    {
        "device_type": "hp_comware",
        "host": ipb,
        "username": "admin",
        "password": "PASSWORD",
       
    }
    for ipb in ipaddrs2
]

ipaddrs3 = open('dell5424_3524.txt')

dell = [
    {
        "device_type": "dell_powerconnect",
        "host": ipc,
        "username": "admin",
        "password": "PASSWORD",

    }
    for ipc in ipaddrs3
]

ipaddrs4 = open('tucdell1124.txt')

dell2 = [
    {
        "device_type": "DellOS10",
        "host": ipd,
        "username": "admin",
        "password": "PASSWORD",

    }
    for ipd in ipaddrs4
]
    # HPs 1920
for device in hp1:
    netCon = ConnectHandler(**device)
    name = netCon.find_prompt()
    print ("\n>>>>>>>>>>>>>>>>>>>>><HP>{0}<HP><<<<<<<<<<<<<<<<<<<<<<".format(name))
    out = netCon.send_command_timing("_cmdline-mode on \n Y\nJinhua1920unauthorized\nscreen-length disable \n")
    outmac = netCon.send_command("display mac-address " + mac)
    print(outmac)

    # HPs 1920

for device in hp2:
    netCon = ConnectHandler(**device)
    name = netCon.find_prompt()
    print ("\n>>>>>>>>>>>>>>>>>>>>><HP>{0}<HP><<<<<<<<<<<<<<<<<<<<<<".format(name))
    out = netCon.send_command_timing("_cmdline-mode on \n Y\n512900\nscreen-length disable \n")
    outmac = netCon.send_command("display mac-address " + mac)
    print(outmac)

    # 5424,3524

for device in dell:
    net_connect = DellPowerConnectSSH(**device)
    out = net_connect.send_command_timing("enable \nPASSWORD\n")
    outd = net_connect.send_command("show bridge address-table address " + macdell)
    name = net_connect.find_prompt()
    print (">>>>>>>>>>>>>>>>>>>>><DELL>{0}<DELL><<<<<<<<<<<<<<<<<<<<<<".format(name))
    print(outd)

    # Dell N1124T

for device in dell2:
    net_connect = DellOS10SSH(**device)
    out = net_connect.send_command_timing("enable \nPASSWORD\n")
    outd = net_connect.send_command("show mac address-table address " + macdell)
    name = net_connect.find_prompt()
    print (">>>>>>>>>>>>>>>>>>>>><DELL>{0}<DELL><<<<<<<<<<<<<<<<<<<<<<".format(name))
    print(outd)