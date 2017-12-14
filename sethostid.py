from struct import pack
f = open('/etc/hostid', 'w')
f.write(pack('i', 1510633252))
f.close()
