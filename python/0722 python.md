# 함수(function)

> 특정한 기능(function)을 하는 코드의 묶음

- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있음.

- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있음. (`return` 값이 없으면, `None`을 반환함.)

- 함수는 호출을 `func()` / `func(val1, val2)`와 같이 함.

#### 활용법

```
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```



## 1 특정 함수 만들기

```python
# 사각형의 둘레와 넓이를 구하는 함수
def rectangle(width, height):
    area = width * height
    perimeter = (width + height) * 2
    return(area, perimeter) # 반환해줌

print(rectangle(30,20)) # 출력해줌
# (600, 100)
```



- 우리가 활용하는 print문도 파이썬에 지정된 함수이나 return이 없음.

- 내장함수(Built-in Functions)를 보려면 `dir(__builtins__)` 를 입력하면 됨.



```python
# 크기비교 함수
# 방법 1
def my_max(a,b):
    max_num = a
    if a<=b:
        max_num = b
    return f'{max_num}가 더 큽니다.'
# 방법 2
def my_max(a,b):
    if a>=b:
        return f'{a}가 더 큽니다.'
    else:
        return f'{b}가 더 큽니다.'
# 리턴이 없는 함수(따라서 output이 없다.)
def my_max2(a,b):
    if a>=b:
        print(f'{a}가 더 큽니다.')
    else:
        print(f'{b}가 더 큽니다.')
```



## 2 함수의 인자

> 함수는 기본적으로 인자를 위치로 판단함.

```python
def cylinder(r,h):
    area = (3.14 * r * r)
    volume = area * h
    return volume
print(cylinder(5,2))
print(cylinder(2,5)) # 순서를 바꾸면 다른 값이 나옵니다.
#157.0
#62.800000000000004
```

### 2-1. 기본 인자값(Default Argument Value)

- 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있음

```python
# 예시
def greeting(name='익명'):
    return f'{name}, 안녕?'

greeting()
# '익명, 안녕?''
```

- ##### 단, 기본 인자값을 가지는 인자 다음에 기본값이 없는 인자를 사용불가

```python
def greeting(name = '익명', grade):
    return f'{grade}학년 {name}님, 환영합니다.'

# 오류
  File "<ipython-input-68-5d5f0a496bad>", line 1
    def greeting(name = '익명', grade):
                 ^
SyntaxError: non-default argument follows default argument
    
# 수정
def greeting2(grade, name = '익명'):
    return f'{grade}학년 {name}님, 환영합니다.'

greeting2(4)
# '4학년 익명님, 환영합니다.'
```



### 2-2. 키워드 인자(Keyword Arguments)

> 키워드 인자는 직접 변수의 이름으로 특정 인자를 전달 가능

```python
# 예시
def greeting4(age, name = '익명'):
    return f'{age}세 {name}님, 환영합니다.'

# 기존대로 할 경우 문제점(기본적으로 인자를 위치로 파악하기 때문에)
greeting4('홍길동',20)
# '홍길동세 20님, 환영합니다.'

# 따라서 키워드 인자를 사용
greeting4(name = '홍길동', age = 20)
'20세 홍길동님, 환영합니다.'
```

- ##### 단, 키워드 인자를 활용한 다음에 위치 인자를 활용할 수는 없음.

```python
greeting(name = '홍길동', 20) # 다쓰던지, 뒤에만 쓰던지 해야 함.

#오류
  File "<ipython-input-80-b4f522bfa17f>", line 1
    greeting(name = '홍길동', 20)
                              
^
SyntaxError: positional argument follows keyword argument
```



### 2-3. 정해지지 않은 여러 개의 인자 처리

####  2-3-1) 가변(임의) 인자 리스트(Arbitrary Argument Lists)

> `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트`*args`를 활용합니다.
>
> 가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.

```python
# 예시
max(1, 5, 2, 3, 4, 10)
//
print(1,2,3,4,5,6,7,8,9,10,11,12)
//
def func(*args):
    for i in args:
        if i % 2 ==0:
            print(i)
func(1, 2, 3, 4, 5, 6)
//
import sys
def my_max(*args):
    max_value = -sys.maxsize
    for i in args:
        if max_value < i:
            max_value = i
    return max_value
//
#참고
tuple = sequence(순서있는) immutable(불변) 시퀀스
args는 tuple임
```



#### 2-3-2) 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

>  정해지지 않은 키워드 인자들은 **`dict`** 형태로 처리가 되며, `**`로 표현함
>
> 보통 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있음

```python
def my_dict(**kwargs):
    return kwargs
my_dict(한국어 = '안녕')
```



## 3 함수와 스코프(scope)

> 함수는 코드 내부에 공간(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분됨.
>
> - **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
> - **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
>
> - **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
> - **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

```python
# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    a = 30 # 전역보다 지역스코프에 있는 값을 가져감.
    print(a) # 지역스코프에서 전역스코프에는 접근가능
    print(b)

# 중2병, 히키코모리, 막내동생법칙
# "내방(지역스코프, local scope)은 아무도못와, 근데 난 밖(전역스코프, global scope)에를 볼거야"
# "방(지역스코프, local scope)에 물이있으면 밖(전역스코프, global scope) 에나갈필요없이 방안에 있는 물을 먹을거야"
# 변수 c는 접근 불가합니다. 전역스코프에서 지역스코프는 접근불가 불가
#print(c) :이대로 전역스코프에서 출력하면 Error가 뜸.
# 50을 인자로 전달하여 출력할 수 있습니다.
func(50)
```

### 3-1. 이름검색(resolution) 규칙

> 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음.
>
> 이것을, `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나감.
>
> - `L`ocal scope: 정의된 함수
>
> - `E`nclosed scope: 상위 함수
>
> - `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
>
> - `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
print = 'ssafy'
print(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-2cb6b91e6926> in <module>
      1 #
      2 print = 'ssafy'
----> 3 print(3)

TypeError: 'str' object is not callable
    
#내장함수인 print 를 global scope에서 'ssafy'라고 했으므로 기존의 print 역할을 하지 못함.

#del print를 통해 기존에 저장한 내용을 다 지워줘야됨.
```

1. `print()` 코드가 실행되면
2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고,
4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됨
5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문

``` python
a = 10  # 전역 변수
b = 20  # 전역 변수

def enclosed():
    a = 30  # enclosed함수의 지역 변수
    
    def local():
        c = 40 # local함수의 지역 변수
        print(a, b, c)
    local()
    a = 50  # enclosed함수의 지역 변수이며, local함수에서는 Enclosed Scope
    
enclosed()
# 30 20 40
```

#### 3-1-1) 전역 변수의 변환(잘 사용하지 않음.)

``` python
global_num = 3
def local_scope():
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)

# 출력
global_num이 5으로 설정되었습니다.
global_num: 3

# 굳이 전역에 있는 변수를 바꾸려면    
global_num = 3
def local_scope():
    global global_num
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
# 출력
global_num이 5으로 설정되었습니다.
global_num: 5
```



#### 3-1-2)변수의 수명주기(lifecycle)

>  변수의 이름은 각자의 `수명주기(lifecycle)`가 있음.

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)



## 4. 재귀 함수(recursive function)

> 재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻함.
>
> 알고리즘을 설계 및 구현에서 유용하게 활용됨.
>
> 점화식 = 재귀식
>
> 최대 재귀깊이(1000번)를 넘어가면 더이상 함수를 호출 하지 않고, 종료됨

### 4-1. 재귀함수 vs 반복문

#### 4-1-1) 팩토리얼 계산

```python
#재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# 반복문
def fact(n):
    result = 1
    for i in range(1,n+1):
        result*= i
    return result
```



#### 4-1-2) 피보나치 수열

```python
#재귀함수
def fib(n):
  if n==1:
    return 1
  elif n==2 :
    return 1
  return fib(n-1) + fib(n-2)

# 반복문
def fib_loop():
    result=1
    for i in range(1,n+1):
        if n == 1:
            result = 1
        elif n==2:
            result = 1
        else:
            result = result + 
```

