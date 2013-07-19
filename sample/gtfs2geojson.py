#!/usr/bin/env python
#
# Script to convert a GTFS format shapes.txt into per-line GeoJSON files
# Usage: create output directory gtfs2geojson
#        python gtfs2geojson.py dir-with-gtfs-data/shapes.txt

import sys

import json

lines = {}

for line in open(sys.argv[1]).readlines()[1:]:
    shp_id, pt_seq, dist, lat, lon = line.split(",")
    
    lines.setdefault(shp_id, []).append((float(lon),float(lat)))


for line, points in lines.items():
    output = file("%s.json" % line, "wt")
    print >>output, """
{ "type": "Feature",
  "geometry":
    { "type": "LineString",
      "coordinates":
"""

    print >>output, json.dumps(points)

    print >>output, """
    }
}
"""
#    for point in points:
#        print >>output, point
