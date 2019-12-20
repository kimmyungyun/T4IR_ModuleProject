# 모듈 프로젝트

카카오 지도 API, FLASK 기반의 위도, 경도를 활용한 초등학교의 폐교, 개교 예측

## Installation

[INSTALL.md](INSTALL.md) 을 참고


## Getting Started

#### 대한민국 행정구역 데이터

- [행정구역](http://www.gisdeveloper.co.kr/?p=2332) 해당 링크에 있는 파일을 사용하십시오

- [행정구역 단순화](https://mapshaper.org/) 해당 링크를 통해서 행정구역 데이터의 크기를 줄일 수 있습니다

- [함수파일](convertUTM2WGS84.py) 파일을 통해 행정구역 데이터를 위도, 경도 데이터로 바꿀 수 있습니다

#### 주의점

- 현재 버젼은 MongoDB와 OracleDB를 통해 데이터를 가져오게 되어있습니다.

- 만약 MongoDB와 OracleDB에 데이터를 넣지 않고 실행할 경우 해당 코드들을 수정해주십시오

- ```python
  load_sido_json()
  # 함수의 내용을 아래의 코드로 바꿔주십시오
  with open("save_sido2.json", encoding="UTF-8") as f:
      Loc = json.load(f)
      return Loc
  ```

- ```python
  load_pcamodel()
  # 함수의 내용을 아래의 코드로 바꿔주십시오
  with open("pca.pkl", 'rb') as rf:
      model = pickle.load(rf)
      return model
  ```

- ```python
  read_Schoollocation()
  # 함수의 내용을 아래의 코드로 바꿔주십시오
  return pd.read_csv("final_school_data.csv", encoding="euc-kr").values.tolist()
  ```

## Running the tests

```
cd path/to/directory
python app.py
```



## License

#### MIT License

```
MIT LicenseCopyright (c) <2019> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

#### 카카오 지도 API

해당 카카오 지도 API에 대한 저작권은 KAKAO developers에 있습니다
[카카오](https://developers.kakao.com/)