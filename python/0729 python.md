### 모듈(module)

> 파일 단위의 코드 재사용!
>
> 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)



### 패키지(package)

> 패키지는 점( . )으로 구분된 모듈 이름(package.module)을 써서 모듈을 구조화하는 방법

- 패키지 생성 : --init--.py
- 폴더 구조

```python
my_package/
    __init__.py
    math/
        __init__.py
        tools.py 
```



# OOP(Object Oriented Programming)

## 1 OOP(객체지향 프로그래밍)

- 목표 : 세상 -> 코드
- 젤리, 우유, 쿠키, 다즈 -> 강아지라고 분류
- 지형, 현우, 채린, 진영 --> 사람
- 분류를 하기 시작
- 코드로 젤리, 우유, 다즈 ...... 를 만든다.
- 분류된 특성을 이용해 만들면 편하다.

```python
jelly_hair = 'white'
def bark():
    print('왈왈')
def 앉기():
    print('스르륵')

milk_hair = 'white'
def bark():
    print('왈왈')
def 앉기():
    print('스르륵')


#원래는 새로 만들때마다 이렇게 새로 지정을 해서 해야함. 하지만
#객체지향을 이용하면
class Dog():
    hair = 'white'
    def bark(self):        
    	print('왈왈')

jelly = Dog() #젤리는 도그라는 틀을 이용해 만들어짐.
```

- 사람이 세상에 존재하는 것을 특성을 통해 분류를 함.
- 코드에서도 똑같이 분류(틀)를 만들어서 이용하자.(객체지향)

- 객체의 특징
  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가? int, list, dict ....
  - 속성(attribute) : 어떤 상태(데이터)를 가지는가? 3+4j.real
  - 조작법(method) : 어떤 행위(함수)를 할 수 있는가? [2,4,1,3].sort()



## 2 인스턴스 & 클래스 변수/ 이름공간/ 메서드

> - 인스턴스 & 클래스 변수
> - 인스턴스 & 클래스간의 이름공간
> - 인스턴스 & 클래스 메서드(+ 스태틱 메서드)

### 1. 인스턴스 & 클래스 변수

#### 1-1.  인스턴스 변수

- 인스턴스의 속성(attribute)
- 각 인스턴스들의 고유한 변수(데이터)
- 메서드 정의에서 `self.변수명` 으로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명` 으로 접근 및 할당



#### 1-2.  클래스 변수

- 클래스의 속성(attribute)
- 해당 클래스의 모든 인스턴스가 공유
- 클래스 정의 내부에서 선언
- `클래스.변수명` 또는 `인스턴스.변수명` 으로 접근(할당)



### 2. 인스턴스 & 클래스간의 이름공간

#### 2-1. 이름 탐색 순서(name resolution)

- 인스턴스와 클래스 모두에서 같은 속성 이름이 등장하면, 속성 조회는 인스턴스를 우선함



#### 2-2. 이름 공간 원칙

- 인스턴스에서 변수의 이름을 조회를 할 수 없다면, 클래스 객체의 데이터를 조회함
- 즉, 인스턴스 => 클래스(=> 상위 클래스) 순으로 탐색



### 3. 인스턴스 & 클래스 메서드(+스태틱 메서드)

#### 3-1. 인스턴스 메서드(instance method)

- 인스턴스가 사용할 메서드
- 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
- 호출시, 펏번째 인자로 인스턴스 자기자신 `self` 이 전달됨

```python
class MyClass:
    def instance_method(self, arg1, arg2, ...)

my_instance = MyClass()
my_instance.instance_method(arg1, arg2)    

# 호출시, 첫 번째 인자로 인스턴스(my_instance)가 전달됨
MyClass.instane_method(my_instance, arg1, arg2) 
```



#### 3-2. 클래스 메서드(class method)

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- 호출시, 첫번째 인자로 클래스`cls`가 전달됨

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...

# 호출시, 첫 번째 인자로 클래스(MyClass)가 전달됨
MyClass.class_method(MyClass, arg1, arg2, ...)
```



#### 3-3. 스태틱 메서드(static method)

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- 호출시, 어떠한 인자도 전달되지 않음.

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        

# 호출시, 어떤 인자도 전달되지 않음
MyClass.static_method(arg1, arg2)
```



### 추가 내용

#### 인스턴스와 메서드

- 인스턴스는, 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 함 (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계

#### 클래스와 메서드

- 클래스 또한 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 클래스에서 인스턴스 메서드는 호출하지 않는다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계한다. (클래스 메서드와 정적 메서드)
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의한다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의한다.

#### 클래스메서드와 정적메서드

- 클래스 메서드와 정적 메서드는 인스턴스 없이 호출할 수 있다는 점은 같다.
- 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용하며 그렇지 않을 경우 정적 메서드를 사용한다.



## 3 상속

> - super()
> - 메서드 오버라이딩(Method Overriding)
> - 상속관계에서 이름공간
> - 다중 상속(Multiple Inheritance)

- 클래스에서 가장 큰 특징
- 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아짐
- 이점
  - 코드를 중복하여 정의하지 않을 수 있음
  - 공통된 속성이나 메서드를 부모클래스에 정의하고 상속함으로써, 적은 코드로 다양한 형태의 객체를 만들 수 있음

### 1. super()

- 자식 클래스에 메서드를 추가로 구현 할 수 있음
- 부모 클래스의 내용을 사용하고자 할 때, super() 를 사용할 수 있음



### 2. 메서드 오버라이딩

> Method Overriding(메서드 재정의): 자식 클래스에서 부모 클래스의 메서드를 재정의 하는 것

- 상속 받은 메서드를 재정의 할 수도 있음
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀



### 3. 상속관계에서의 이름공간

- 기존의 인스턴스 -> 클래스 순으로 이름공간을 탐색해 나가는 과정에서 상속관계에 있으면 아래와 같이 확장됨.
- 인스턴스 -> 클래스
- 인스턴스 -> 자식클래스 -> 부모클래스



### 4. 다중 상속

- 두개 이상의 클래스를 상속받는 경우, 다중 상속이 됨
- 상속의 순서는 왼쪽에서 오른쪽 순서임

