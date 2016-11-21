#!/usr/bin/env python

#the following code is used to delete a virtual machine using one or more of the images present in the nova_client images repository and then list the Vm's deleted at the end

from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

servers_list = nova_client.servers.list()
server_del = "vm1"
server_exists = False

for s in servers_list:
    if s.name == server_del:
        print("This server %s exists" % server_del)
        server_exists = True
        break
if not server_exists:
    print("server %s does not exist" % server_del)
else:
    print("deleting server..........")
    nova_client.servers.delete(s)
    print("server %s deleted" % server_del)