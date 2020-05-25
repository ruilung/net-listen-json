#!/bin/bash
LISTENPORT=$(ss -tln | awk '{print $4}' | grep -Eo ':[0-9]+' |  awk -F: '{print $2}' | sort | uniq)
echo -n '{"data":['
for port in $LISTENPORT; do
        echo -n '{"{#PORT}":"'${port}'"},'
done |sed -e 's:\},$:\}:'
echo -n ']}'
