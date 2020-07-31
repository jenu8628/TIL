## 요청(request)과 응답(response)

### 1. API

> 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻함

- URL : 어디로? 에 대한 정보
- parameter(함수시간에 매개변수) : 무엇을가지고? 에 대한 정보

- 인터페이스 : 요청인터페이스, 응답구조

example

http://www.kobis.pr.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json(여기까지가 어디로? 에 해당하는 내용)**`?`**(URL끝났어 어떤내용을 보내면돼?의 구분)key = asdfasdfasdf &(key와 value의 구분) targetDt = 123124

key는 api사이트에서 발급받은것을 쓰게될 것이고 targetDt는 사이트에서 가져올 내용임.



### 2. python requests(파이썬 요청라이브러리)

```python
import requests
url = '원하는 url복붙'
r = requests.get(url) #(url 요청하기) url자리에 바로 주소를 입력해도 됨.

#2 url에 parameter(변수)를 넣고싶으면?
url = 'http://www.asdfasdfasdf.?전까지'
payload = {
    'key' : '123123123123123',
    'targetDt' : '20200123',
    'itemPerPage' : 3
}
r= requests.get(url,params = payload)

# response의 내용을 보고 싶다면?
print(r.text)
# type은?
print(Type(r.text)) #-> str

# Why? 확장자마다 다르게 사용. Json의 경우
r.json() # json데이터를 해석하는 역할을 하고 있음.
print(r.json())
print(Type(r.json())) #-> dict
```



### 3. URL을 만들기위한 기초 담아놓기 (Class이용)

```python
class URLMaker:
    url = 'https://www.kobis.or.kr/kobisopenapi/webservice/rest'
    
    def __init__(self, key):
        self.key = key
    
    # rest뒤에 박스오피스/리스트 이런거를 추가시켜줄꺼임.+key값
    def get_url(self, category, feature):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'
        
url_maker = URLMaker('key') # api키
url_maker.get_url('boxoffice','searchDailyBoxOfficeList')
    
```



- 영화정보 페이지를 구성하기 위하여 데이터를 수집하는 단계 아래의 기술된 사항은 필수적으로 구현해야 함



1. 요청조건
   1. 제공되는 kobis.py를 이용하여 일별 박스오피스 데이터를 요청
   2. 어제 날짜를 기준으로 데이터를 요청
2. 결과
   1. 제공된 데이터에서 매출액 정보만 가져옴
   2. 가져온 정보를 반환하는 함수 sales를 완성



```python
import requests
from kobis import URLMaker

def sales():
    url_maker = URLMaker('key') # api키
    url = url_maker.get_url('boxoffice', 'searchDailyBoxOfficeList')

    payload = {
        'targetDt' : '20200730'
    }

    r = requests.get(url, params=payload)
    movies_dict = r.json()
    movies = movies_dict.get('boxOfficeResult').get('dailyBoxOfficeList')
    # .get() 딕셔너리에 키값에 접근하는 메소드 get을 쓰면 코드가 중간에 끊기지 않음. 값이 없으면 None을 반환함.keyError를 무시할 수 있게 됨.
    result = []
    for movie in movies:
        result.append(movie.get('salesAmt'))
  	return result
print(sales())
```

