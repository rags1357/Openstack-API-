#!/usr/bin/env python

from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values

#List the routers created by the create-router code

try:
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    routers_list = neutron.list_routers(retrieve_all=True)
    print_values(routers_list, 'routers')
finally:
    print("Execution completed")
	
#List the subnets which queries the neutron.list method 

credentials = get_credentials()
neutron = client.Client(**credentials)
subnets = neutron.list_subnets()
print(subnets)