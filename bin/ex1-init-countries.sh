#!/bin/bash
TEMP='/home/vagrant/temp'
if [ ! -d "$TEMP" ]; then
    mkdir $TEMP
fi
cd $TEMP
ZIPFILE="TM_WORLD_BORDERS-0.3.zip"
URL="http://thematicmapping.org/downloads/$ZIPFILE"
if [ ! -f "$TEMP/$ZIPFILE" ]; then
    wget $URL
fi
unzip -u $ZIPFILE
SHP="$TEMP/TM_WORLD_BORDERS-0.3.shp"
DB_HOST=localhost
DB_NAME=ex1
DB_USER=ex1
DB_PASS=ex1
TABLE='country'
ogr2ogr -overwrite -f "PostgreSQL" PG:"host=$DB_HOST user=$DB_USER dbname=$DB_NAME password=$DB_PASS" -nln $TABLE -nlt "MULTIPOLYGON" $SHP
