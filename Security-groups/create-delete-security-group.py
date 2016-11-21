#!/usr/bin/env python

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
nova.security_groups.create(name="web", description="Web servers")

'''

group = nova.security_groups.find(name="web")
nova.security_groups.delete(group)

The following lines would also delete the group:
nova.security_groups.delete(group.id)
group.delete()

'''