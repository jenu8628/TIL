

#### 1. json파일을 가져와 원하는 정보만 dict로 출력하기(json파일에 정보(dict)가 하나일 때)

```python
music_json = open('data/music.json', encoding='UTF8')
#print(music_json)
#data/music.json data폴더 안에 music.json파일
#뒤에 r 또는 W를 넣어야 하지만 넣지 않으면 자동으로 r(reading)로 적용됨
#한글로 인해 오류가 뜨기 때문에 encoding작업이 필요
import json
music_dict = json.load(music_json)
#print(type(music_dict))
# music_json파일을 로드해서 딕셔너리 파일로 바꿔줌
def music_info(music): # 딕셔너리 중에 원하는 정보를 뽑아내는 함수를 만들자!
    result={}
    result['singer'] = music['singer']
    result['title'] = music['title']
    #dict는 중괄호로 이루어져 있지만 접근을 할 때는 대괄호와 Key를 이용!
    return result

print(music_info(music_dict))
```

- 위의 코드 정리

```python
import json # 모듈 불러오는 것은 위에 써주는 것이 좋음
def music_info(music): # 함수선언도 위에 써주는게 좋음
    result={}
    result['singer'] = music['singer']
    result['title'] = music['title']
    return result
# 다음으로 함수에 필요한 부분을 적어주는게 좋음
# json파일을 불러오는 코드
music_json = open('data/music.json', encoding='UTF8') 
# json을 dict로 변환하는 코드
music_dict = json.load(music_json)

#music_dict 함수 실행
print(music_info(music_dict))
```

- file IO : 파일 입출력
- pprint(prety printer): 출력값을 보기쉬운형태로 이쁘게 출력해줌.

- Tip : 움직일 코드를 드래그하고 `Alt` 누른 상태로 화살표키로 이동할 수 있다.


#### 2. json파일을 가져와 원하는 정보만 dict로 출력하기(json파일에 정보(dict)가 여러개 일때)

```python
import json
import pprint

def music_info(musics):
    result = []
    for music in musics:
        music_detail = {} #반복될 때마다 딕셔너리를 하나 만들것이고 그 값을 result에 담을 예정
        music_detail['singer'] = music['singer']
        music_detail['title'] = music['title']
        result = result + [music_detail] #dict를 list에 담아 result에 넣는 과정
        # [{IU}] + [{조정석}] => [{IU},{조정석}]
        return result

musics_json = open('data/musics.json', encoding = 'UTF8')
musics_list = json.load(musics_json)
#print(type(musics_list)) => list
#musics_list = [{},{},{},{},...,{}]
#pprint.pprint(musics_dict) key값이 나올때마다 엔터를 해줘서 보기 편하게 만들어줌!


# 만들고 싶은 결과
#    [
#        {
#            "singer" : "IU",
#            "title" : "에잇"
#        },
#        {
#            "singer" : "조정석",
#            "title" : "아로하"
#        }    
#    ]
```



- open()
  - filename : 내가 열고싶은 파일의 이름을 적는다.
  - mode: `r` 읽기모드, `w` 쓰기모드. 아무것도 적지 않으면 기본적으로 읽기모드로 적용된다.
  - encoding :  한글때문에 파일이 정상적으로 dict로 변환이 안된경우 `UTF8` 을 적용하여 해결했다.

```python
open(filename,mode)
```



- json
  - 아직은 뭔지 잘 모르지만 dict라고 생각하자!

```python
import json
#json데이터를 python에서 사용할 수 있는 dict데이터로 변환
json.load()
# 예시
dict_data = json.load(json_data)
```

```python
def movie_info(movie, genres):
    result = {}
    keys = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 
    'vote_average']
    for i in keys:
        result[i] = movie[i]
    for index, id in enumerate(result['genre_ids']):
        for genre in genres:
            if id == genre['id']:
                result['genre_ids'][index] = genre['name']
    result['genre_names'] = result.pop('genre_ids')
    return result
```

``` python
def movie_info(movie, genres):
    result = {}
    keys = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 
    'vote_average']
    for i in keys:
        result[i] = movie[i]
    for i in range(len(result['genre_ids'])):
        for genre in genres:
            if result['genre_ids'][i] == genre['id']:
                result['genre_ids'][i] = genre['name']
    result['genre_names'] = result.pop('genre_ids')
    return result
```

