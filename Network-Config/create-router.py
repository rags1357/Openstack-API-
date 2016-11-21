#!/usr/bin/env python

from neutronclient.v2_0 import client
import novaclient.v2.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials
from utils import print_values_server

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

# network_id is retrived from the environment details.

network_id = '81bf592a-9e3f-4f84-a839-ae87df188dc1'
try:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    neutron.format = 'json'
    request = {'router': {'name': 'router name',
                          'admin_state_up': True}}
    router = neutron.create_router(request)
    router_id = router['router']['id']
    # for example: '72cf1682-60a8-4890-b0ed-6bad7d9f5466'
    router = neutron.show_router(router_id)
    print(router)
    body_value = {'port': {
        'admin_state_up': True,
        'device_id': router_id,
        'name': 'port1',
        'network_id': network_id,
        }}

    response = neutron.create_port(body=body_value)
    print(response)
finally:
    print("Execution completed")