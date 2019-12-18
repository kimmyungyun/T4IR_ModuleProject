from flask import Flask, escape, request, render_template
from decouple import config
import json
import pandas as pd
import numpy as np

import pickle
import math
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

Jet_colormap = [
    '#0000BF'
    , '#0000FF'
    , '#0040ff'
    , '#0080ff'
    , '#00bfff'
    , '#00ffff'
    , '#3fffbf'
    , '#7fffbf'
    , '#bfff3f'
    , '#ffff00'
    , '#ffbf00'
    , '#ff7f00'
    , '#ff4000'
    , '#ff0000'
    , '#bf0000'
    , '#7f0000'
    , '#000000']

restapi = config('KAKAO_REEST_API')
jsapi = config('KAKAO_JAVASCRIPT_API')
with open("save_sido2.json", encoding="UTF-8") as f:
    Loc = json.load(f)

with open("pca.pkl", 'rb') as rf:
    model = pickle.load(rf)

app = Flask(__name__)

def init_pca():
    pipe = model['pipe']
    pipe.fit(model['X_train'], model['Y_train'])
    return pipe

pipe = init_pca()

def predict(x, y):
    x = float(x)
    y = float(y)

    X_test = [np.array([x, y], dtype=np.float32)]

    predictions = pipe.predict(X_test)
    print(predictions)
    return predictions


@app.route('/')
def hello():
    unique_location = pd.read_csv("final_school_data.csv", encoding="euc-kr").values.tolist()
    # print(Loc["features"][0]["geometry"])
    return render_template("index.html", app_key=jsapi, unique_location = unique_location, \
                           location_size = len(unique_location), colormaps = Jet_colormap, predict=predict,\
                            json_data = Loc["geometries"])

@app.route('/predict',methods=["POST"])
def predic():
    pos = request.form.get('lat')
    pos2 = request.form.get('lng')
    result = {}
    pre = predict(pos, pos2)[0]
    print(pre)
    if pre == 1:
        result['qq'] = True
    else:
        result['qq'] = False
    return json.dumps(result)

if __name__=='__main__':
    app.run(debug=True, port=8080)