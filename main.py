import ipaddress

while(True):
    print('*' * 20)
    print("Please enter the network address:")
    print("An example would be 10.0.0.0")
    network = input("-----> ")

    print('*' * 20)

    print("Please enter the network address:")
    print("An example would be 27")
    mask = input("Prefix Bits: ")
    try:
        subnet = ipaddress.ip_network((network +"/"+ mask))
        break
    except ValueError:
        print('*' * 20)
        print('*' * 20)
        print("Please enter a classful addresss space.")
        print('*' * 20)
        print('*' * 20)

address_list = []
for x in subnet.hosts():
    address_list.append(x)

print(f'First Host--------------> {address_list[0]}')
print(f'Last Host---------------> {address_list[-1]}')
print(f'Total Hosts-------------> {len(address_list) -1 }')
