# 파이썬 기초

## 1. 변수

> dust = 60
>
> - dust는 60이다(X)
> - dust에 60을 저장한다(O)



### 1) 할당 연산자(Assignment Operator)

- 변수는 =을 통해 할당된다.
- type()은 해당 데이터 타입을 확인
- id()는 해당값의 메모리 주소를 확인

```python
x = 'ssafy'
type(x)
id(x)
x = y = 'ssafy' #같은 값을 동시에 할당가능
a, b = 2020, 4 #동시에 여러개의 변수에 값 여러개를 할당가능 단, 변수개수와 할당값의 개수가 동일해야함.
a, b, c = 10, 20 #오류 : 변수와 할당값의 개수가 맞지않음
a, b = b, a #변수 a와 b의 값을 바꿈
```



### 2) 식별자(Identifiers)

> 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)이다.
>
> - 내장함수나 모듈 등의 이름으로 만들면 안된다.
> - 첫 글자에 숫자가 올 수 없다.
> - 예약어는 사용할 수 없다.
>
> ```python
> import keyword
> print(keyword.kwlist)
> ```



### 3) 데이터 타입(Data Type)

#### 1. 숫자 타입

##### ①  int (정수, integer)

- 모든 정수는 int로 표현됨

```python
a = 4
type(4)
```

- 정수 자료형에서 오버플로우가 없다.



##### ②  float (부동소수점, 실수, floating point number)

- 실수는 float으로 표현됨.
- 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며 항상 같은 값으로 일치되지 않습니다. 이는 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류로 값을 같은지 비교하는 과정에서 문제가 발생할 수 도 있음.
- 컴퓨터식 지수표현 방식

```python
b = 314e-2
```

- 실수의 연산
  - 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있다.
  - 오류 처리방법

``` python
3.5 + 3.2  #6.7
3.5-3.2 == 0.3 #False / 3.5-3.2 = 0.299999999999
round(3.5-3.2, 2) == 0.3 #True/ round: 반올림, 현재는 2번째 자리에서 반올림 하라는 뜻, 4사 6입 짝수에서는 5는 내림 / 홀수에서는 5는 올림
```

- sys 모듈과 math 모듈을 통해 처리하는 방법

```python
import sys
print(sys.float_info.epsilon) #'epsilon'은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환

abs(a - b) <= sys.float_info.epsilon 
#2.220446049250313e-16
#True

import math
math.isclose(a,b)
# True
```



##### ③ complex (복소수, complex number)

> 허수부를 j로 표현

- 문자열을 복소수로 변환할 때 문자열은 중앙의 + 또는 -연산자 주위에 공백을 포함해서는 안됨.

```python
b= complex('3+4j') # O
c= complex('3 + 4j') # Error
```



####  2. 문자(string) 타입

