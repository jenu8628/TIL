공식문서 : django model field



## CharField(max_lengh=None)

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수인자
- 필드의 최대 길이, 데이터베이스와 django의 유효성검사
- input type text
- char



## TextField()

- 글자의 수가 많을 때 사용
- 필수인자가 따로 없음(CahrField와의 차이점)
- `<textarea>`를 기본값으로 가지고 있음
- str



## DateTimeField()

- 최초 생성 일자: `auto_now_add=True`
  - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
  - 테이블에 어떤 데이터를 최초로 넣을 때 
- 최종 수정 일자: `auto_now=True`
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



## Migrations

> 기본적으로 python manage.py '이곳에 적는다'

### makemigrations

- 모델을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
- 모델을 활성화 하기 전에 DB 설계도를 작성
- 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라고 생각



### migrate

- 작성된 마이그레이션 파일들을 기반으로 실제 DB에 반영
- db.sqlite3라는 데이터베이스 파일에 테이블을 생성
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸



### sqlmigrate

- 해당 마이그레이션 파일이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인 하기 위한 명령어
- sqlmigrate 뒤에 앱이름과 번호 적어주기



### showmigrations

- 마이그레이션 파일들의 migrate 여부를 확인 하기 위한 명령어



### Model의 중요 3단계

1. models.py : 변경사항 발생
2. makemigrations : 설계도 만들기
3. migrate : DB에 적용



## DB API 구문 - Maing Queries

### Article.objects.all()

Class Name/ Manager / QuerySet API

objects : python model과 DB가 상호작용할 수 있도록 해주는 매니저

#### django shell에서 실행 해야함

- python shell에서는 실행 불가
- django shell을 기본으로 설정하면 기능이 많지 않아서
- 3rd party library를 설치하여 좀더 기능이 많은 shell-plus를 이용할 예정

1. ipython : python shell기능을 좀더 강화 (터미널에 ipython을 치면 됨)
2. django-extensions : django기능을 좀더 강화

- django_extensions를 앱에 추가해줘야 사용 가능
- python manage.py shell_plus입력



### django-extensions 사용이유

- 기존의 것으로 shell을 키면(python manage.py shell) 모듈이나 임포트를 직접 다해야 함,
- shell_plus로 키면 기존에 써논걸 다 불러와 줌.



## CRUD

> 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성) Read(읽기) Update(갱신), Delete(삭제)를 묶어서 일컫는 말

### Create

> 데이터를 작성하는 3가지 방법

1. 첫번째 방법

   1. article = Article() :  모델 클래스로부터 인스턴스 생성
   2. article.title = 'first' : article 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수 변경
   3. article.save() : 인스턴스로 save메서드 호출(데이터베이스에 실제로 저장)

   

2. 두번째 방법

   1. 클래스로 인스턴스 생성 시 keword 인자를 함께 작성

      ex) article = Article(title='seconds', content='django!')

   2. article.save()

   

3. 세번째 방법

   1. 생성하며 바로 DB에 저장

      ex) Article.objects.create(title='third', content='django!!')



### Read

`all()`

- `Queryset` return
- 리스트는 아니지만 리스트와 거의 비슷하게 동작(조작할 수 있음)



`get()`

- 객체가 없으면 `DoseNotExist` 에러가 발생
- 객체가 여러개일 경우는 `MultipleobjectReturned`에러가 발생
- 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있으면 사용할 수 있다.
- 주로 pk값을 조회할 때만 사용



`filter()`

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 QuerySet을 return



### Update

- 파이썬에서 하는 듯이 하면 될듯



### Delete

- .delete()





## admin(shell대신 쓸수 있음)

> 슈퍼유저 생성 : python manage.py createsuperuser

- 이름 : admin

- 비밀번호 : admin1234

- auth_user안에 슈퍼유저 정보가 있음

- 장고에서도 비밀번호는 모름
- admin에서 Article을 쉽게 다룰 수 있음
- admin에서 Article을 다룬다고 등록을 해준 뒤 해야함
- 하는법
  - 앱폴더에서 admin.py 에 들어와서 작성

```python
from django.contrib import admin
from .models import Article #명시적 상대경로 표현

# Register your models here.
admin.site.register(Article)
```

- 주의
  - 반드시 DB구축하고 (migrate) 슈퍼유저를 생성한다.