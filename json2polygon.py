import json
import geojson

with open("geo_sigun.geojson", "r", encoding="utf-8") as f:
    # js = json.load(f)
    js = geojson.load(f)
    print("HH")
