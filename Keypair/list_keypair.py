#!/usr/bin/env python

#List keypairs

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
keypairs = nova.keypairs.list()