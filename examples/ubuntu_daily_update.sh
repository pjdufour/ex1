DATE=$(date)
DATEISO=$(date "+%Y-%m-%d")
TIMESTAMP=$(date +%s)
echo "Executing daily pull of MODIS active fire data"
echo "Starting at $DATE"
ex1-modis-fires-collect.sh /home/ubuntu/temp/modis_active_fires/$DATEISO
ex1-modis-fires-export.py --output /home/ubuntu/exports/modis_active_fires/current
ex1-modis-fires-export.py --output /home/ubuntu/exports/modis_active_fires/$DATEISO
echo "Ending at $(date)"
