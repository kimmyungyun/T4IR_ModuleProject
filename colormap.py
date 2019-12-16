import json
from pyproj import Proj, transform
import numpy as np
import pandas as pd

proj_UTMK = Proj(init='epsg:5178')
proj_WGS84 = Proj(init='epsg:4326')

with open("sido.json", encoding="UTF-8") as f:
    q = json.load(f)

    Loc = q["features"]
    result = []
    cnt = 0;
    for loc in Loc:

        loc_name = loc['properties']['CTP_KOR_NM']
        coordinates = loc['geometry']['coordinates'][0]
        result_coords = []
        cnt2 = 0
        for coord in coordinates:

            x1, x2 = transform(proj_UTMK, proj_WGS84, coord[0], coord[1])
            coord[0] = x1;
            coord[1] = x2;
            if (cnt2% 100) == 0:
                print(f"{cnt} / {len(Loc)} = {cnt/len(Loc)}%  ||| {cnt2} / {len(coordinates)} = {cnt2/len(coordinates)}%")
            cnt2 = cnt2+1
            # print("HH")
        #     result_coords.append([x1, x2])
        # result.append(result_coords)
        cnt = cnt + 1
        print("DDD")

    with open("student_file.json", "w") as json_file:
        json.dump(q, json_file)

print("QQ")