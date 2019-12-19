import json
from pyproj import Proj, transform

proj_UTMK = Proj(init='epsg:5178')
proj_WGS84 = Proj(init='epsg:4326')

with open("rere_sido.json", "r", encoding="utf-8") as f:
    js = json.load(f)

    cnt = 0
    for geo in js['geometries']:
        if geo['type'] == 'Polygon':
            for i in geo['coordinates']:
                for j in i:
                    j[0], j[1] = transform(proj_UTMK, proj_WGS84, j[0], j[1])
                    cnt = cnt+1
                    if cnt % 100 == 0:
                        print(cnt)
        elif geo['type'] == 'MultiPolygon':
            for i in geo['coordinates']:
                for j in i:
                    for k in j:
                        k[0], k[1] = transform(proj_UTMK, proj_WGS84, k[0], k[1])
                        cnt = cnt+1
                        if cnt % 100 == 0:
                            print(cnt)
    print("End")

    with open('save_sido.json', "w") as qq:
        json.dump(js, qq)
