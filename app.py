from flask import Flask, escape, request, render_template
from decouple import config

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

Jet_colormap = [[0, 0, 191],
                [0, 0, 191]
    , [0, 0, 255]
    , [0, 63, 255]
    , [0, 127, 255]
    , [0, 191, 255]
    , [0, 255, 255]
    , [63, 255, 191]
    , [127, 255, 127]
    , [191, 255, 63]
    , [255, 255, 0]
    , [255, 191, 0]
    , [255, 127, 0]
    , [255, 63, 0]
    , [255, 0, 0]
    , [191, 0, 0]
    , [127, 0, 0]]

restapi = config('KAKAO_REEST_API')
jsapi = config('KAKAO_JAVASCRIPT_API')

app = Flask(__name__)

@app.route('/')
def hello():
    unique_location = pd.read_csv("unique_location.csv", encoding="UTF-8").values.tolist()
    return render_template("index.html", app_key=jsapi, unique_location = unique_location, location_size = len(unique_location)
                           , colormaps = Jet_colormap)

if __name__=='__main__':
    app.run(debug=True, port=8080)