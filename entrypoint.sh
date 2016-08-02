#!/bin/sh
python ./runserver.py --host 0.0.0.0 -P 8765 -a ptc -u $POKE_USER -p $POKE_PASS -l "$POKE_LOCATION" -st 4 --gmaps-key "$POKE_MAPSKEY" -sd 5 --db-type mysql --db-name $MYSQL_DATABASE --db-user $MYSQL_USER --db-pass $MYSQL_PASSWORD --db-host db $@
