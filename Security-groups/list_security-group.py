#!/usr/bin/env python

#To list security groups for the current project, call the novaclient.v_1.security_groups.SecurityGroupManager.list method is used :

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
security_groups = nova.security_groups.list()