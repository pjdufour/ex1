#!/bin/bash
TEMP=$1
if [ ! -d "$TEMP" ]; then
    mkdir -p $TEMP
fi
cd $TEMP
ZIPFILE="Global_24h.zip"
URL="https://firms.modaps.eosdis.nasa.gov/active_fire/shapes/zips/$ZIPFILE"
if [ ! -f "$TEMP/$ZIPFILE" ]; then
    wget $URL
fi
unzip -u $ZIPFILE
SHP="$TEMP/Global_24h.shp"
DB_HOST=localhost
DB_NAME=ex1
DB_USER=ex1
DB_PASS=ex1
TABLE='hotspot'
ogr2ogr -append -f "PostgreSQL" -a_srs "EPSG:4326" PG:"host=$DB_HOST user=$DB_USER dbname=$DB_NAME password=$DB_PASS" -nln $TABLE -nlt "POINT" $SHP
