#!/usr/bin/env python

# To re-use the original hostid. Convert from hexadecimal to decimal
# https://www.rapidtables.com/convert/number/hex-dec-bin-converter.html
# Value passed into pack method is decimal value.

from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
