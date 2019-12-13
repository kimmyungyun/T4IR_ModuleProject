from flask import Flask, escape, request, render_template
from decouple import config
import requests
import random

restapi = config('KAKAO_REEST_API')
jsapi = config('KAKAO_JAVASCRIPT_API')


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', "World")
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)