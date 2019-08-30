#!/usr/bin/env python

# To re-use the original hostid. Convert from hexadecimal to decimal

# Convert Hex to Decimal 
#
# To convert a hex_value to a decimal. The int() accepts a string and base 16. 
#  int('0x5a0a6f24',16) 
#
# Convert a Decimal to Hex : hex(1510633252) 
#
# Pass decimal value into pack method

from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
