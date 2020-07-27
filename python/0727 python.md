# Data Structure(데이터 구조)

## 1. Errior & Exception (에러 & 예외)

### 1-1 Error

#### 1-1-1 문법 에러(syntax Error)

> 문법 에러가 있는 프로그램은 실행되지 않음

- `파일이름`과 `줄번호`, `^` 문자를 통해 파이썬이 코드를 읽어 들일 때(`parser`) 문제가 발생한 위치를 표현함
- EOL = end of line, 따옴표 오류, 따옴표 열고 닫는부분에 문제가 있음.
- EOF = end of file, 괄호 닫기 오류, 괄호가 열고 닫는부분에 문제가 있음.



### 1-2 Exception(예외)

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춤

- 문법적으로는 옳지만, 실행시 발생하는 에러
-  ZeroDivisionError
  - 0으로 나눌수는 없음

- nameError
  - 지역 혹은 전역 이름 공간내에서 유효하지 않는 이름.   즉, 정의되지 않은 변수를 호출 하였을 경우

-  TypeError
  - 자료형에 대한 타입 자체가 잘못 되었을 경우
  
  - 함수 호출과정에서 TypeError도 발생

```python
round('3.5')
```

- 함수호출 과정에서 다양한 오류
  - 필수 argument 누락

```python
import random
random.sample([1, 2, 3])
```

- 함수호출 과정에서 다양한 오류
  - argument 개수 초과

```python
random.choice([1, 2, 3], 6)
```

- ValueError
  - 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우

- ValueError
  - 존재하지 않는 값을 찾고자 할 경우

- IndexError
  - 존재하지 않는 index로 조회할 경우

- KeyError 
  - 딕셔너리에서 Key가 없는 경우

- ModuleNotFoundError 
  - 모듈을 찾을 수 없는 경우

- ImportError
  - 모듈을 찾았으나 가져오는 과정에서 실패하는 경우(존재하지 않는 클래스/함수 호출)

- KeyboardInterrupt
  - 주피터 노트북에서는 정지 버튼이지만, 실제로 우리가 돌릴 때는 `ctrl` + `c` 를 통해 종료하였을 때 발생



## 2. 예외 처리(Exception Handling)

> try & except
>
> try문을 이용하여 예외처리를 할 수 있음

- 활용법

```python
try:
    <코드 블럭 1>
except:
    <코드 블럭 2>
```

- `try` 아래의 코드블락(code block)이 실행됨
- 예외가 발생되지 않으면, **`except`없이 실행이 종료됨**
- 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행됨

### 2 - 1 에러 메세지 처리 `as`

> `as` 키워드를 활용하여 에러 메세지를 보여줄 수도 있음

- 활용법

```python
try:
    <코드 블럭 1>
except 예외 as error: #error는 예외 다음 나오는 에러 설명을 담게됨
    <코드 블럭 2>
```



### 2-2 복수의 예외 처리

> 하나 이상의 예외를 모두 처리할 수 있음
>
> 괄호가 있는 튜플로 여러 개의 예외를 지정할 수 있음

- 활용법

```python
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>


try:
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```

- **에러가 순차적으로 수행됨**으로, 가장 작은 범주부터 시작해야 함.

### 2-3 else

- 에러가 발생하지 않는 경우 실행 시킬 문장은 `else`를 활용함
- `else`는 `except` 코드 뒤에 와야 함
- `try` 코드 블럭이 예외를 일으키지 않았을 때, 실행되어야 하는 코드에 사용됨

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```

### 2-4 finally

- 어떤 경우에든 반드시 실행해야하는 코드에는 `finally`를 활용함
- 예외의 발생 여부과 관계없이 항상 실행됨

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```

## 3. 예외 발생 시키기(Exception Raising)

### `raise`

- `raise`를 통해 예외를 강제로 발생시킬 수 있음

```python
raise ZeroDivisionError('division by zero 오류가 발생하였습니다.')

# ZeroDivisionError: division by zero 오류가 발생하였습니다.
```



### `assert`

- `assert` 문은 예외를 발생시키는 다른 방법임

- 보통 **상태를 검증하는데 사용**되며 무조건 `AssertionError`가 발생함

```python
assert Boolean expression, error message

assert type(1) == int, '문자열을 입력하였습니다.'
# AssertionError: 문자열을 입력하였습니다.
# 라고 뜨게됨
def my_div(num1, num2):
    assert type(num1) == int, '숫자를 입력해 주세요.'
# type(num1) != int인 경우에만 AssertionError가 발생하며 뒤에 지정 문구가 나옴
# type(num1) == int인 경우에는 오류가 발생하지 않음
```

- 위의 검증식이 거짓일 경우를 발생함

- `raise`는 항상 예외를 발생시키고, `assert`는 지정한 예외가 발생한다는 점에서 다름



# 데이터 구조(Data Structure) 1

데이터를 저장하거나 조작하는 방법을 말함

> **Program = Data Structure + Algorithm**

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered)데이터 구조
  - 문자열(String)
  - 리스트(List)
- 데이터 구조에 적용 가능한 Built-in Function(내장 함수)
  - `map()`
  - `filter()`
- return이 된다는 것은 별도의 변수에 저장할 수 있다는 것

## 1. 문자열(String)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

- 문자열의 다양한 조작법(method)

### 1-1 조회/탐색

- `.find(x)`:  x의 첫 번째 위치를 반환. 없으면 `-1`을 반환
- `.index(x)`:  x의 첫 번째 위치를 반환. 없으면, 오류가 발생

```python
try:
    'apple'.index('k')
except ValueError:
    print('해당하는 값이 없습니다.')
```



### 1-2 값 변경

- `.replace(old, new[, count])`
  - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환함
- count 값을 설정안하면 기본적으로 해당문자 전체삭제,  count를 지정하면 해당 갯수만큼만 좌측부터 시행
  
- `.strip([chars])`
  - 특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거함(rstrip).
  - 지정하지 않으면 공백을 제거
- `.split()`
  - 문자열을 특정한 단위로 나누어 리스트로 반환

- `'separator'.join(iterable)`
  - 특정한 문자열로 만들어 반환
  - 반복가능한(iterable)컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`)문자열로 반환함
  - `separator` == 분리기호



### 1-3 기타 문자열 관련 검증 메소드

```python
dir('string')
```





## 2. 리스트(List)

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

- 데이터 구조로서의 리스트와 조작법(method)

### 2-1 값 추가 및 삭제

- `.append(x)`  : 리스트에 값을 추가 (return이 없는 함수)
- `.extend(iterable)` : 리스트에 iterable 값을 붙일 수 있음.
  - append와 extend 의 차이는 append는 추가하려는 값을 통째로 리스트안에 넣어주고 extend는 요소들만 하나 하나 씩 넣어준다.

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append(['coffeenie'])
# => ['starbucks', 'tomntoms', 'hollys',['coffeenie']]
cafe.extend(['twosome_place'])
# => ['starbucks', 'tomntoms', 'hollys', 'twosome_place']
cafe.extend('ediya')
# => ['starbucks', 'tomntoms', 'hollys', 'e', 'd', 'i', 'y', 'a']
```

- `.insert(i,x)`: 정해진 위치 i에 x값을 추가 (리스트의 길이를 넘어서는 인덱스는 마지막에 추가됨)
- `.remove(x)` : 리스트에서 값이 x인 것을 삭제

- `.pop` : 정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환함, i가 지정되지 않으면 마지막 항목을 삭제하고 반환
- `.clear()` : 리스트의 모든 항목을 삭제

### 2-2 탐색 및 정렬

- `index(x)` : x 값을 찾아 해당 index 값을 반환
- `.count(x)` : 원하는 값의 개수를 확인 가능
- `.sort()` : 정렬을 함, 내장함수 `sorted()` 와는 다르게 원본 list를 변형시키고, None을 리턴

- `.reverse()` : 반대로 뒤집음 (정렬아님)



### 2-3 리스트 복사

```python
original_list = [1, 2, 3]
copy_list = original_list
print(copy_list)
# => [1,2,3]

copy_list[0] = 5
print(original_list)
# => [5,2,3]

id(copy_list) == id(original_list)
copy_list is original_list
# =>True
```



### imutable vs mutable 데이터 복사 차이

```python
a = 20
b = a
b = 10

print(a)# => 20
print(b)# => 10

a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)#=>[100, 2, 3, 4]
print(b)#=>[100, 2, 3, 4]
```



## 3 리스트를 복사하는 방법

>  slice연산자 `[:]` 사용, `list()` 활용

- 복사본을 바꿔도 원본이 바뀌지 않음.



## 4 List Comprehension

> List Comprehension은 표현식과 제어문을 통해 리스트를 생성
>
> 여러줄의 코드를 한 줄로 줄일 수 있다는 장점

- [식 for 변수 in iterable] or list(식 for 변수 in iterable)

```python
number = range(1,11)
cubic_list = [number ** 3 for number in numbers]

cubic_list = []
for number in numbers:
    cubic_list.append(number ** 3)
```





# 데이터 구조(Data Structure) 2

## 1 세트(set)

> 변경가능(mutable), 순서가 없고(unordered), 순회가능한(iterable)

### 1.1 추가 및 삭제

- `.add(elem)` : elem을 세트에 추가 (return이 없음)

- `.update(*others)` : 여러가지의 값을 추가 (return이 없음)
  - 인자로는 반드시 iterable데이터 구조를 전달해야 함
- `.remove(elem)` : elem을 세트에서 삭제하고, 없으면 KeyError가 발생 (return이 없음)

- `.discard(elem)` : elem을 세트에서 삭제하고, 없어도 에러가 발생하지 않음
- `.pop()` : 임의의 원소를 제거해 반환함



## 2 딕셔너리(Dictionary)

> 변경가능(mutable), 순서가 없고(unordered), 순회가능한(iterable)
>
> `key: value` 페어의 자료구조

### 2.1 조회

- `.get(key[, default])` : key를 통해 value를 가져옴.
  - 절대로 KeyError가 발생하지 않음. default는 기본적으로 None임

### 2.2 추가 및 삭제

- `.pop(key[, default])`:key가 딕셔너리에 있으면 제거하고 반환. 그렇지 않으면 default를 반환
  - default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생
- `.update(key = value1)` : 값을 제공하는 key의 value를 value1로 덮어씀

### 2.3 딕셔너리 순회(반복문 활용)

- 딕셔너리에 for문을 실행하면 기본적으로 다음과 같이 동작

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)

john
eric
justin
```

- dictionary 에서 for문을 활용하는 4가지 방법

```python
# 0. dictionary 순회(key 활용)
for key in dict:
    print(key)
    print(dict(key))
    
#1. `.key()` 활용
for key in dict.keys():
    print(key)
    print(dict(key))
    
#2. `.values()` 활용
for val in dict.values():
    print(val)
    
#3. `.items()` 활용
for key, val in dict.items():
    print(key, val)
```



### 2.4 Dictionary comprehension

- `{키: 값 for 요소 in iterable}` or `dict([키: 값 for 요소 in iterable])`