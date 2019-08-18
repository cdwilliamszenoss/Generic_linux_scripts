#!/usr/bin/env python

# To re-use the original hostid. Convert from hexadecimal to decimal
# Convert Hex to Decimal : int(hex_value,16)
# Convert Decimal to Hex : hex(decimal_value)

# Pass decimal value into pack method

from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
