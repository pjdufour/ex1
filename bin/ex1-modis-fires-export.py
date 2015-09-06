#!/usr/bin/python
from base64 import b64encode
from optparse import make_option
import json
import argparse
import time
import os
import sys
import subprocess
import zipfile
import psycopg2
import osgeo.ogr as ogr
import osgeo.osr as osr
#==#
def make_request(url, params, auth=None, data=None, contentType=None, GEVENT_MONKEY_PATCH=False):
    """
    Prepares a request from a url, params, and optionally authentication.
    """

    if GEVENT_MONKEY_PATCH:
        # Import Gevent and monkey patch
        try:
            from gevent import monkey
            monkey.patch_all()
        except:
            print "gevent monkey patch failed"

    import urllib
    import urllib2
    
    if params:
        url = url + '?' + urllib.urlencode(params)

    req = urllib2.Request(url, data=data)

    if auth:
        req.add_header('AUTHORIZATION', 'Basic ' + auth)

    if contentType:
        req.add_header('Content-type', contentType)
    else:
        if data:
            req.add_header('Content-type', 'text/xml')

    return urllib2.urlopen(req)


def export_hotspots(args):

    verbose = args.verbose
    output = args.output

    conn_params = {
        'host': args.db_host,
        'port': args.db_port,
        'database': args.db_name,
        'user': args.db_user,
        'password': args.db_pass}

    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("SELECT iso3 FROM country GROUP BY iso3;")
    rs = cur.fetchall()
    countries = [iso3 for (iso3, ) in rs]

    columns = ["H.ogc_fid", "H.wkb_geometry", "H.latitude", "H.longitude", "brightness", "scan", "track", "acq_date", "acq_time", "satellite", "confidence", "version", "bright_t31", "frp", "fips", "iso2", "iso3", "un", "name", "area", "pop2005", "region", "subregion", "lon", "lat"]

    stmts = [
        "DROP MATERIALIZED VIEW IF EXISTS hotspots_by_country;",
        "CREATE MATERIALIZED VIEW hotspots_by_country AS SELECT "+(", ".join(columns))+" FROM hotspot as H INNER JOIN country as C ON st_intersects(H.wkb_geometry, C.wkb_geometry) ;"]

    for stmt in stmts:
        print stmt
        cur.execute(stmt)

    cur.close()
    conn.close()

    export_hotspots_to_disk(args, countries)

def export_hotspots_to_disk(args, countries):

    out_parent = args.output

    conn_params = {
        'host': args.db_host,
        'port': args.db_port,
        'database': args.db_name,
        'user': args.db_user,
        'password': args.db_pass}

    conn_str = "PG:host={host} port={port} dbname={database} user={user} password={password}".format(**conn_params)
    print conn_str
    conn = ogr.Open(conn_str)
    in_lyr = conn.GetLayer("hotspots_by_country")
    in_lyr_def = in_lyr.GetLayerDefn()

    out_drv = ogr.GetDriverByName("ESRI Shapefile")
    for iso3 in countries: 
        print "Exporting hotspots for country "+iso3
        in_lyr.SetAttributeFilter("iso3 = '{iso3}'".format(iso3=iso3))
        out_shp = os.path.join(out_parent, "{iso3}.shp".format(iso3=iso3))
        if os.path.exists(out_shp):
            out_drv.DeleteDataSource(out_shp)
        out_ds = out_drv.CreateDataSource(out_shp)
        out_lyr = out_ds.CreateLayer(iso3, geom_type=ogr.wkbPoint)

        for i in range(0, in_lyr_def.GetFieldCount()):
            out_lyr.CreateField(in_lyr_def.GetFieldDefn(i))

        out_lyr_def = out_lyr.GetLayerDefn()

        for in_f in in_lyr:
            out_f = ogr.Feature(out_lyr_def)
            for i in range(0, out_lyr_def.GetFieldCount()):
                out_f.SetField(out_lyr_def.GetFieldDefn(i).GetNameRef(), in_f.GetField(i))

            g = in_f.GetGeometryRef()
            out_f.SetGeometry(g.Clone())
            out_lyr.CreateFeature(out_f)

        out_ds.Destroy()

    conn.Destroy()

#==#
parser = argparse.ArgumentParser(description='Clip & export 24-hr hotspots by country.')
parser.add_argument('--verbose', '-v', default=0, action='count', help="Print out debug messages.")
parser.add_argument("--output", default="/var/www/hotspots", help="The output directory to export the country hotspots shapefile.")
parser.add_argument("--db_host", default="localhost", help="The database host")
parser.add_argument("--db_port", default="5432", help="The database port")
parser.add_argument("--db_name", default="ex1", help="The database name")
parser.add_argument("--db_user", default="ex1", help="The database user")
parser.add_argument("--db_pass", default="ex1", help="The database password")
args = parser.parse_args()
#==#
export_hotspots(args)
