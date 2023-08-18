from netmiko.tplink.tplink_jetstream import TPLinkJetStreamSSH

print('\nPadrão Mac para TPLINK XX:XX:XX:XX:XX:XX\n')
mactp = input("Digite o MAC para TPLINK: ")

tplink_switch = {
'device_type': 'tplink_jetstream',
'host': '123.23.123.1',
'username': 'LOGIN',
'password': 'PASS',
}

print("\nConnect to host")
connect_tplink_switch = TPLinkJetStreamSSH(**tplink_switch)
print("\nConnected.")
print(">>>>>>>>>>>>>>>>>>>>>TPLINK", connect_tplink_switch.find_prompt(),"<<<<<<<<<<<<<<<<<<<<<<<<")

config_commands = ['show mac address-table address '+ mactp,
]
tplink_output = connect_tplink_switch.send_config_set(config_commands)
print(tplink_output)