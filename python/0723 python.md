# 함수

## ※ 함수 만들기 연습

### 1. 절댓값 함수 만들기

```python
def my_abs(x):
    if type(x) == complex:
        return (x.real**2 + x.imag**2)**(1/2)
    else:
        if x == 0:
            return x**2
        elif x < 0:
            return -x
        else:
            return x
```



### 2. all() 함수 만들기

> all()은 인자로 받은 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환함.

```python
# 방법1
def my_all(elements):
    result = True
    for i in elements:
        # bool(i) == False
        # not bool(i)
        if not i:
            result = False
    return result
            
# 방법 2
def my_all(elements):
    result = True
    for i in elements:
        if bool(i) == False:
            return False
    return True
```



### 3.  any() 함수 만들기

> any()는 인자로 받는 iterable(range,list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환함.

```  python
# 방법 1
def my_any(elements):
    result = False
    for i in elements:
        #bool(i) == True -- 자동변환됨
        if i:
            result = True
            break # 사실 없어도 잘됨.
    return result

# 방법 2
def my_any(elements):
    for i in elements:
        if i: # => bool(i) == True
            return True
    return False
```



## 문제 풀이

### 1. 달팽이

> 달팽이는 낮 시간 동안에 기둥을 올라가지만 방에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다.(밤 이동거리 < 낮 이동거리)
>
> 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 작성.
>
> 함수의 인자
>
> - 기둥의 높이(미터)
> - 낮 시간동안 달팽이가 올라가는 거리(미터)
> - 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

```python
# 방법 1
def snail(height, morning, night):
    alpa = morning - night
    day = (height-morning) // alpa
    if morning > height:
        return 1
    elif (height-morning) % alpa = 0:
        # 도착점에서 day 만큼의 거리가 남았으므로 1일을 추가함.
        return day +1
    else:
        #도착점에서 morning만큼을 뺀거에서 나머지가 생겼기 때문에 2일더 올라가야함.
        return day +2
    
# 방법 2 -- 높이에서 달팽이가 올라가는 만큼을 빼면서 count, 높이가 0이하가 되면 반복문 끝
# 즉 달팽이가 기둥을 다 오르면 count를 return
def snail(height, morning, night):
    count = 0
    while True:
        count += 1
        height -= morning
        if height <= 0:
            return count
        height += night
        
# 방법 3 -- 방법 2에서 높이를 0에서 올라가는 만큼을 더하면서 count
def snail(height, morning, night):
    count = 0
    snail_height = 0
    while True:
        count += 1
        snail_height += morning
        if snail_height >= height:
            return count
        snail_height -= night
```



### 2. 자릿수 더하기

> 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력

```python
# 방법 1
# 문자로 바꾸고 하나하나를 다시 숫자로 바꿔서 더한다.
def sum_of_digit(number):
    number_str = str(number)
    total = 0
    for digit in number_str:
        total += int(digit)
    return total

# 방법 2
def sum_of_digit(number):
    total = 0
    num = str(number)
    for i in range(len(num)):
        total += int(num[i])
        
# 방법 3
# 1234 = 1*1000 + 2*100 + 3*10 + 4*1
# 1234 % 10 = 4
# 1234 // 10 => 123
# 123 % 10 => 3
# 123 // 10 => 12
# 12 % 10 => 2
# 12 // 10 => 1
# 1 % 10 => 1
# 1//10 => 0
def sum_of_digit(number):
    total = 0
    while True:
        remainder = number % 10
        total += remainder
        number = number // 10
        if number == 0:
            return total
        
# 방법 4 재귀함수 이용
def sum_of_digit(number):
    # sod(4321) => 1 + sod(432) => 1+2+sod(43) => 1+2+3+sod(4) => 1+2+3+4 
    if number < 10:
        return number
    remainder = number % 10
    number = number // 10
    return remainder + sum_of_digit(number)
```

