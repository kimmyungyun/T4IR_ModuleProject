import json
from pyproj import Proj, transform
import numpy as np
import pandas as pd

proj_UTMK = Proj(init='epsg:5178')
proj_WGS84 = Proj(init='epsg:4326')

with open("re_sigun.json", encoding="UTF-8") as f:
    q = json.load(f)

    Loc = q["features"]
    result = []
    cnt = 0;
    for idx in range(8, len(Loc)):

        loc_name = Loc[idx]['properties']['CTP_KOR_NM']
        coordinates = Loc[idx]['geometry']['coordinates']
        result_coords = []
        cnt2 = 0
        for coord in coordinates:
            cnt3 = 0
            for coo in coord[0]:
                x1, x2 = transform(proj_UTMK, proj_WGS84, coo[0], coo[1])
                coo[0] = x1;
                coo[1] = x2;
                if (cnt3% 100) == 0:
                    print(f"{cnt} / {len(Loc)} = {cnt/len(Loc)}%  ||| {cnt2} / {len(coordinates)} = {cnt2/len(coordinates)}% ||| {cnt3} / {len(coord[0])} = {cnt3/len(coord[0])}%")
                cnt3 = cnt3+1
            cnt2 = cnt2+1
            # print("HH")
        #     result_coords.append([x1, x2])
        # result.append(result_coords)
        cnt = cnt + 1
        print("DDD")

    with open("student_file3.json", "w") as json_file:
        json.dump(q, json_file)

print("QQ")