# Used to reset swap memory. Execute via cron. Set MAX_SWAP_VALUE to desired value.

#!/bin/bash

export MAX_SWAP_VALUE=400; if [[ $(egrep -o "*.[0-9]*." <(/sbin/swapon -s |awk 'NR>1 {print $4}')) -gt $MAX_SWAP_VALUE ]]; then echo "Turning Swap OFF"; /sbin/swapoff -a; sleep 5;fi; while [[ ! $(/sbin/swapon -s | awk 'NR>1 {print $1}') ]]; do echo "Turning Swap ON";/sbin/swapon -a;done


# List processes using swap
 for i in /proc/*/status; do  awk -v var=$i '/Name/{NAME=$0;next} /VmSwap/ && $2 > 0 {print NAME"\t"$0"\t"var} ' $i  2>/dev/null; done | sort -t ":" -k3 -n |column -t


--------------------------
