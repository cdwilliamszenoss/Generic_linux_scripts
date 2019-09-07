# When executed the system will disable the swap partition and trasfer all data to physical RAM. Once completed, the script
# will automatically renable swap on the system.
#
# Used to reset swap memory. Execute via cron. Set MAX_SWAP_VALUE to desired value.
 

export MAX_SWAP_VALUE=400; if [[ $(egrep -o "*.[0-9]*." <(/sbin/swapon -s |awk 'NR>1 {print $4}')) -gt $MAX_SWAP_VALUE ]]; then echo "Turning Swap OFF"; /sbin/swapoff -a; sleep 5;fi; while [[ ! $(/sbin/swapon -s | awk 'NR>1 {print $1}') ]]; do echo "Turning Swap ON";/sbin/swapon -a;done



