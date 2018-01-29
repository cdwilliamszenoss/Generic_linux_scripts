#Identify containers using 70% capacity


for i in $(df | awk '!/shm/ { if (($5 ~ /[[7-9][0-9]/) || ($5 ~/100/)) {print $6  }}'| awk -v FS='/' '{print $7}'); do docker inspect $(docker ps -q) | grep -E "DeviceName|Hostname" | grep -A1 $i; done | grep Hostname 



serviced service status | grep $Hostname
