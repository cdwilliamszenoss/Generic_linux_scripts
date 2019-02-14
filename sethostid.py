#!/usr/bin/env python

# Value passed into pack is an Octal conversion of the hostid

from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
