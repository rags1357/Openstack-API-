#!/usr/bin/env python

#Lists the ports created by the create-ports.py 

#!/usr/bin/env python
from neutronclient.v2_0 import client
import novaclient.v2.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials
from utils import print_values_server

credentials = get_nova_credentials()
nova_client = nvclient.Client(credentials)

#server_id and network_id are got from the environment details 

server_id = '9a52795a-a70d-49a8-a5d0-5b38d78bd12d'
network_id = 'ce5d204a-93f5-43ef-bd89-3ab99ad09a9a'
server_detail = nova_client.servers.get(server_id)
print(server_detail.id)

if server_detail is not None:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    ports = neutron.list_ports()

    print_values_server(ports, server_id, 'ports')
    body_value = {'port': {
        'admin_state_up': True,
        'device_id': server_id,
        'name': 'port1',
        'network_id': network_id,
        }}

    response = neutron.create_port(body=body_value)
    print(response)