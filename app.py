from flask import Flask, escape, request, render_template
from decouple import config
import json
import pandas as pd
import numpy as np
import cx_Oracle
import os
import pymongo 
from pymongo import MongoClient
from io import BytesIO
from gridfs import GridFS
from bson import objectid

import pickle
import math
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 폐교 밀도 color value -- 김명윤
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

#.env 파일에 적혀있는 키값 가져오기 -- 김명윤
restapi = config('KAKAO_REEST_API')
jsapi = config('KAKAO_JAVASCRIPT_API')

# #몽고디비 연결 -- 김우희 
conn = pymongo.MongoClient().python_test
fs = GridFS(conn)

#각 시도 별 구역 위도,경도 몽고 DB연결-- 김우희
def load_sido_json():
    f = fs.get_last_version(filename = "save_sido2.json")
    model = json.load(BytesIO(f.read()))
    return  model

# 학습된 모델 데이터 몽고DB 연결-- 김우희
def load_pcamodel():
    f = fs.get_last_version(filename = "pca.pkl")
    data = f.read()
    model = pickle.load(BytesIO(data))
    # model = pickle.load(rf)
    return model
model = load_pcamodel()
Loc = load_sido_json()
app = Flask(__name__)

# 학습된 모델 로딩 -- 김명윤
def init_pca():
    pipe = model['pipe']
    pipe.fit(model['X_train'], model['Y_train'])
    return pipe

    # 오라클 데이터 베이스 연동 -- 김우희
def read_Schoollocation():
    connection = cx_Oracle.connect('HR','1234','localhost/xe')
    cursor = connection.cursor()
    return pd.read_sql("select * from FINAL_SCHOOL_DATA",connection).values.tolist()

pipe = init_pca()

# 위도 경도를 사용해 모델 적용 -- 김명윤
def predict(x, y):
    x = float(x)
    y = float(y)

    X_test = [np.array([x, y], dtype=np.float32)]

    predictions = pipe.predict(X_test)
    print(predictions)
    return predictions


@app.route('/')
def hello():
    unique_location=read_Schoollocation()

    return render_template("index.html", app_key=jsapi, unique_location = unique_location, \
                           location_size = len(unique_location), colormaps = Jet_colormap, predict=predict,\
                            json_data = Loc["geometries"])

# 카카오맵에 입력한 좌표를 전달받아 예측된 값을 전달 -- 김명윤
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
    app.run(debug=True, port=5000)