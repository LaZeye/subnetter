import ipaddress

network = '192.168.1.0'
mask = '/24'
subnet = ipaddress.ip_network((network + mask))
address_list = []

for x in subnet.hosts():
    address_list.append(x)

print(f'First Host--------------> {address_list[0]}')
print(f'Last Host---------------> {address_list[-1]}')
print(f'Total Hosts-------------> {len(address_list) -1 }')
