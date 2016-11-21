#!/usr/bin/env python

'''
To add a rule to a security group, call the novaclient.v1_1.security_group_rules.SecurityGroupRuleManager.create method is used :
'''

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
group = nova.security_groups.find(name="web")
# Add rules for ICMP, tcp/80 and tcp/443
nova.security_group_rules.create(group.id, ip_protocol="icmp",
                                 from_port=-1, to_port=-1)
nova.security_group_rules.create(group.id, ip_protocol="tcp",
                                 from_port=80, to_port=80)
nova.security_group_rules.create(group.id, ip_protocol="tcp",
                                 from_port=443, to_port=443)