### index페이지에 articles를 다 가져와서 목록 보여주기!

crud/articles/views.py

```python
from .models import Article
from django.shortcuts import render


# Create your views here.
def index(request):
    #Article을 다 가져와서 목록을 보여줄 거임!
    articles = Article.object.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)
```



### 글쓰기 페이지->글쓰기 버튼 누르면 실제 DB에다가 글을 등록->글써짐

기존에 했던

- throw - 검색창 자체를 보여주는
- catch  -  데이터를 받아서 처리

```html
{% extends 'base.html' %}

{% block content %}

  <h1 class="text-center">New</h1>
  <form action="" method="GET">
  {% comment %} id = for 로 갖게 {% endcomment %}
    <label for="title">Title: </label>
    <input type="text" name="title" id="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <input type="submit" value="글 쓰기">
  </form>
  <hr>
  <a href=" {% url 'articles:index' %} ">[뒤로가기]</a>
{% endblock content %}
```





## 커뮤니티 게시판 만들기

> 0819때는 Article  shell_plus에서 CRUD를 이용해서 작성했음.
>
> 사용자들에게는 우리처럼 코드로 쓰게 할 수 없음.

- 글 보여주는 페이지

- 글 쓰는 페이지

- 글 수정하는 페이지

- 글 삭제

#### 껐다가 켜도 그대로 있도록 어딘가에 저장하고 싶음!



#### 현재

Article

id    title    content    create_at    updated_at

1     제목	  내용		생성날짜		수정날짜

throw(new)

catch(create) 



#### post

우편 -> 편지봉투에 내용을 잘 담아서 어디로 보낼 건지(url)



/create/ -> db 데이터를 쓰는 일

db에 데이터를 쓰게 되면 어떻게 될까요

클라우드 서비스

firebase

azure

비용 -> 돈

그런데 누군가가 내가만든 서버(/create)에 마구마구 요청보내면?

-> 내돈 왕창나감

그래서 아무나 요청을 보낼 수 없도록 django에서는 CSRF_token을 만들어 뒀음



name = csrfmiddlewaretoken

vlaue = sadkfljaslkdfjalksf

/create/

정당한 토큰이다/ 아니다를 판별하게됨!!

정당한 토큰 없이 요청을 했다? 403error 발생



정당한 토큰을 받으려면?

/new/ 페이지로 들어와서 글을 써야만 받을 수 있음!



### 그래서 GET과 POST의 차이와 쓰임새!

- GET - 요청을 아무리 여러번 해도 DB에 변화가 없는 요청! - 검색, 조회
- POST - 요청할때마다 DB에 변화가 일어나는 요청 - 글쓰기, 수정, 삭제
  - 아무나 DB를 변경할 수 없도록 보안장치 - CSRF token



#### 삭제

- detail
- 삭제버튼!
- 서버로 요청 서버에서 해당 db의 아이템 삭제
- index페이지로 redirect

- a태그를 이용하면 GET방식의 요청이므로 삭제에 쓸 수가 없음! 따라서 form태그의 POST메소드 사용!!



#### 수정

detail - 수정하기 -수정할 수 있는 화면 ()- 수정 끝나면 요청(수정하기 버튼) - 그 요청대로 수정 - detail보여줌

- detail
- 수정하기
  - 수정할 수 있는 화면을 보여주것이고 DB에서 수정이 아직 이뤄지고 있는 것이 아님 따라서 a태그 맞음
- 수정할 수 있는 화면
- 수정 끝나면 요청
  - 수정하기 버튼
- 그 요청대로 수정
- detail보여줌

- update.html은 new.html의 내용을 그대로 가져와서 수정해놓은 거임 차이점 비교해보셈