### 필터 사용(django templates에 들어가서 보고 사용하면 됨)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dtl-example</title>
</head>
<body>
  <h3> lorem ipsum </h3>
  {% lorem %}
  <hr>
  {% lorem 3 w %}
  <hr>
  {% lorem 5 w random %}
  <hr>
  {% lorem 2 p %}

  <h3>2. 글자 수 제한</h3>
  <p>{{ my_sentence|truncatechars:3}}</p>
  <p>{{ my_sentence|truncatechars:3}}</p>
  <p>{{ my_sentence|truncatewords:3}}</p>

  <h3>3. 글자 관련 필터</h3>
  <p> {{ 'abc'|length }} </p>
  <p> {{ 'ABC'|lower }} </p>
  <p> {{ 'my_sentence'|title }} </p>
  <p> {{ 'abc def'|capfirst }} </p>
  <p> {{ 'menus'|random }} </p>

  <h3>4. 연산</h3>
  <p>{{ 4|add:6 }}</p>

  <h3>5. 날짜 표현</h3>
  {{ datetimenow }} <br>
  {% now "DATETIME_FORMAT" %} <br>
  {% now "SHORT_DATETIME_FORMAT" %} <br>
  {% now "DATE_FORMAT" %} <br>
  {% now "SHORT_DATE_FORMAT" %}
  <hr>
  {% now "Y년 m월 d일 (D) h:i" %}
  <hr>
  {% now "Y" as current_year %}
  Copyright {{ current_year }}
  <hr>
  {{ datetimenow|date:"SHORT_DATE_FPRMAT" }}
  <hr>```
</body>
</html>
```



### 새로운 APP생성

- URL이 app별로 겹치니까 app별로 urls.py를 만듬

- import 해주고

  - from django.urls import path

    from . import views

- urlpatterns 리스트를 선언

- 프로젝트 url.py설정 변경

  - from django.urls import path, include

  - path('articles/', include('articles.urls')),

    path('pages/', include('pages.urls')),

- catch와 throw와 같이 url을 사용하는 경우를 대비해 urlpatterns에 name을 붙여줘서 /catch/와 같은 주소형태가아닌 {% url 'catch' %}와 같이 씀.
- 같은 파일명이 있을 때 다른 폴더에서 불러오는 것을 방지하기 위해 앱별로 templates폴더 안에 폴더를 하나 더 만들어서 html 파일을 생성
- bootstrap을 사용하고 싶을 때 base가 되는 html파일을 만들고 그것을 불러서 사용
  - {% block content %}
  - {% endblock content %}
  - base.html은 settings.py 안에 TEMPLATES안에 DIRS 에 추가해서 사용
  - 없으면 first_project안에 templates폴더를 읽지를 않음.
  - 사용할 때는 사용하고자 하는 html파일에 {% block content %} {% endblock content %}를 써줌

- 각 폴더별 urls에 app_name을 지정하면 html파일에서 다른 url을 불러올 때 구분이 쉽게 됨.