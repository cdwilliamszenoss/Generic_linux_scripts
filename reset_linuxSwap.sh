# Used to reset swap memory. Execute via cron. Set MAX_SWAP_VALUE to desired value.

export MAX_SWAP_VALUE=4000; if [[ $(egrep -o "*.[0-9]*." <(swapon -s |awk 'NR>1 {print $4}')) -gt $MAX_SWAP_VALUE ]]; then echo "Turn off"; swapoff -a; sleep 5;fi; while true; do if [[ ! $(swapon -s | awk 'NR>1 {print $1}') ]]; then echo "Turn ON";swapon -a; sleep 5;else echo "UP"; break;fi;done
