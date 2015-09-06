# Asset Latest Ubuntu
apt-get update; apt-get upgrade;
# Install Basic CLI
apt-get install -y vim git unzip
# Install Python Basics
apt-get install -y python-software-properties
# Add GIS Repos
add-apt-repository ppa:ubuntugis/ubuntugis-unstable
apt-get update
# Install Libraries
apt-get install -y build-essential libxml2-dev libxslt1-dev libjpeg-dev gettext python-dev python-pip python-virtualenv
apt-get install -y libgdal1h libgdal-dev libgeos-dev libproj-dev libpq-dev
apt-get install -y python-gdal python-psycopg2
# Install GDAL/OGR CLI
apt-get install -y gdal-bin
# Install PostGis
apt-get install -y postgresql-9.3-postgis-2.1
# Initialize PostGIS
#sudo postgres psql -d ex1 -c "CREATEUSER ex1 WITH ENCRYPTED PASSWORD 'ex1';"
#sudo postgres psql -c "CREATE DATABASE template_postgis ENCODING 'UTF8' TEMPLATE template1;"
#sudo postgres psql -d template_postgis -c "CREATE EXTENSION postgis;"
#psql -d template_postgis -c "CREATE EXTENSION postgis_topology;"
#psql -d template_postgis -c "CREATE EXTENSION fuzzystrmatch;"
#psql -d template_postgis -c "CREATE EXTENSION postgis_tiger_geocoder;"
#sudo postgres psql -c "CREATE DATABASE ex1 ENCODING 'UTF8' TEMPLATE template_postgis;"
#sudo postgres psql -d ex1 -c "ALTER DATABASE ex1 OWNER TO ex1;"
#sudo postgres psql -d ex1 -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ex1;"
#bash --login -c 'echo "host    ex1             ex1             127.0.0.1/32            md5" >> /etc/postgresql/9.3/main/pg_hba.conf'
# Disable other login methods
#/etc/init.d/postgresql restart
