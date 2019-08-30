#!/usr/bin/env python

# To re-use the original hostid. Convert from the hexadecimal value to a decimal value

# To convert a hex_value to a decimal use the int() function. It accepts a string and a base of 16. 
#  int('0x5a0a6f24',16) 
#
# To convert a Decimal to Hex : hex(1510633252) 
#
# To set the hostid on the node pass the decimal value into pack method

from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
