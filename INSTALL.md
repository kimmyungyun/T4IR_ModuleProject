## Installation

해당 프로그램을 돌리기 위해서는 아래의 모듈 준비 및 카카오 API 등록을 해줘야한다

### Prerequisites

- Python >= 3.6
- pandas
- numpy
- json
- pickle
- decouple - 이 모듈은 직접 API KEY를 넣어줄 경우 필요가 없습니다
- 해당 코드에는 OracleDB와 MongoDB를 사용했으나 json 파일과 csv 파일로 직접 로드를 해도 된다
- KAKAO API



### Installing

해당 명령어를 실행하면 필요한 패지키를 설치한다

```
pip install -r requirements.txt
```



### 카카오 API 준비

- [KAKAO Developers](https://developers.kakao.com/) 해당 링크에서 회원가입 및 로그인을 통해 API KEY를 받아와야 한다
- [지도 API 가이드라인](http://apis.map.kakao.com/web/guide/) 해당 링크의 준비하기를 따라 하면 된다
- Flask 를 통해서 서버를 열 경우, URL을 보통 `127.0.0.1:5000`을 제공할 텐데, 이 경우 카카오 플랫폼에 추가하는 URL 또한 `127.0.0.1:5000`을 등록해줘야한다
- 만약 `localhost:5000`으로 등록할 경우, 접속하는 URL을 `localhost:5000`으로 사용하면 문제가 없다

### .env 파일 준비

- .env 파일 내용

```
KAKAO_JAVASCRIPT_API="YOUR API KEY"
```

- 해당 `YOUR API KEY`부분에 위에서 발급받은 API KEY를 넣으시면 됩니다

