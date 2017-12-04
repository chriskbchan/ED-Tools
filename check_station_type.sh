stname=$1
echo Looking up ${stname} ...
jq -r --arg stname "${stname}" '.[] | select(.name==$stname) | .type_id, .type, .is_planetary' stations_filtered.json
jq -cr --arg stname "${stname}" '.[] | select(.name==$stname)' stations_filtered.json
