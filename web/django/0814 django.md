# Django

> python web framework

### 1. 웹 개발을 하는 것 == 카페를 만드는 것

- A - Z 모두 직접 하기
- 프랜차이즈 창업

### 2. MTV(Model, Template, View)

path('admin/', admin.site.urls)

​							이 부분이 view함수의 이름

### 3. 랜더링

> 무엇인가 만들어진다.

### 4. 코드 작성 순서

1. urls.py
2. views.py
3. templates

### 5. 데이터 흐름

url -> view -> templates



## 오전시간에 한 작업

#### django설치

- pip install django

+ `ctrl` + `shift` + `p`  눌러서 open settings json 들어가서 복붙

#### django pjt 생성

- django-admin startproject 이름

#### 서버를 켜서 로켓 페이지 확인

- python manage.py runserver

#### django app생성

- python manage.py startapp 이름

#### app을 pjt에 등록

#### urls->view->templates

#### 원하는 변수가 여러개일 경우 

>  context라는 딕셔너리를 생성하여 안에 작성하여 입력

#### django templates rangauge

> 변수를 {{}}로 감싸서 넣어줌



## 오후에 배운 내용

#### variable routing

127.0.0.1:8000/hello/이름

이름님 반갑습니다.

- 'hello/<<str:name>>/'



### Django Template Language(DTL)

- django template system에서 사용하는 built-in template system이다.
- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬 처럼 if, for를 사용할 수 있지만 이거는 단순히 python code로 실행되는 것이 아닙니다.

#### syntax

- ##### variable: `{{ }}`

- ##### filter: `{{ variable|filter }}`

- ##### tags: `{% tag %}`

ex)

```html
1.
{% for menu in menus %}
  {{ menu }}
{% endfor %}
=> 짜장면 탕수육 짬뽕

2.
{% for menu in menus %}
  {{ forloop.counter }} : {{ menu }}
{% endfor %}
=> 1 : 짜장면 2 : 탕수육 3 : 짬뽕

3.
{% for x in empty_list %}
  {{ x }}
{% empty %}
  <p>아무것도 없어요!!</p>
{% endfor %}
=> 아무것도 없어요!

4.
{% if '짜장면' in menus %}
  <p>짜장면은 고춧가루지</p>
{% endif %}
=> 짜장면은 고춧가루지

5.
{% if empty_list|length > 10 %}
  <p>길이가 10보다 크네요</p>
{% else %}
  <p>길이가 10보다 작네요</p>
{% endif %}
=> 길이가 10보다 작네요
```



### 템플릿 시스템 설계 철학

- 장고는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.



https://search.naver.com/search.naver?query=헤이즈

네이버 주소창 메커니즘.



#### form

> 정보를 보낼 때 사용

- action
  - 어디다가 보낼지 선택
  - 어디다가 정보를 보낸다는건 해당 url로 정보를 함께 담아요청을 한다.
  - 서버측 해당 url로 보낸 정보를 받아 처리한다.

- GET
  - form에서 정보를 보내는 방법중 하나
  - 보낸 정보를 받으면 url에 내가보낸 정보가 적힌다.
