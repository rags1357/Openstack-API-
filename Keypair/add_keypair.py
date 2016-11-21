#!/usr/bin/env python

#To generate a keypair,the novaclient.v1_1.keypairs.KeypairManager.create method is used :

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
keypair_name = "test-key"
keypair = nova.keypairs.create(name=keypair_name)
print keypair.private_key