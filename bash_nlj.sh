#!/bin/bash
LISTENPORT=$(ss -tln | awk '{print $4}'  | sed 's|::1|::|g' | grep -Eo ':[0-9]+' |  awk -F: '{print $2}' | sort -n | uniq)
echo -n '{"data":['
for port in $LISTENPORT; do
        echo -n '{"{#PORT}":"'${port}'"},'
done |sed -e 's|\},$|\}|'
echo -n ']}'
