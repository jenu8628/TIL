# 3. 문자열(string)

> brute force에 집중!

- Byte = 8bit(bit는 0과 1)
  - byte는 영문자 한글자를 나타내는 단위
- ASCII(아스키코드)는 7bit 인코딩으로 128문자(0~127)를 표현
  - 아스키코드 파이참에서 보는 법! ord()를 통해 아스키 코드값을 볼 수 있음.

### 유니코드 인코딩(UTF: Unicode Transformation Format)

- UTF-8 (in web)
  - MIN : 8bit, MAX: 32bit(1 Byte*4)
- UTF- 16 (in windows, java)
  - MIN : 16bit, MAX: 32bit(2 Byte*2)
- UTF-32 (in unix)
  - MIN : 32bit, MAX: 32bit(4 Byte*1)

### 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고/ 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있다.
- 자기 문자열에서 뒤집으려면 len//2만큼 반복문을 돌리면서 리스트 형태로 변환한 뒤 변경하고 str로 바꿔준다.

```python
def str_rev(str):
    # str -> list
    arr = list(str)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    str = "".join(arr)
    return str

str = 'algorithm'
str1 = str_rev(str)
print(str1)

# 방법 2
s = 'algorithm'
s = s[::-1]
print(s)

# 방법 3
str1 = "algorithm"
for i in range(len(str1)-1,-1,-1):
    print(str1[i], end="")
print()

# 방법 4
str3 = reversed(str1)
print(''.join(str3))

#
n = len(str1) // 2
str4 = list(str1)
for i in range(n):
    str4[i], str4[-1-i] = str4[-1-i], str4[i]
print(''.join(str4))
```



### atoi_itoa

> atoi : 문자열을 int형으로 전환
>
> itoa : int형을 문자열로 전환

```python
# #문자열을 int형으로 전환
def atoi(line):
    num=0

    for i in range(len(line)):
        num *= 10
        num += ord(line[i]) -ord('0')
    return num

number = atoi("4735")
print(type(number), number)

# int형을 문자열로 전환
def itoa(num):
    line = ''
    tmp = num
    while tmp > 0:
        number = tmp % 10
        line += chr(number + ord('0'))
        tmp //= 10
    return line

line = itoa(1234)[::-1]
print(type(line), line)
```

#### 유투브 방식(atoi)

```python
#문자열을 숫자로!
def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        # 0~9
        # if c>= '0' and c <= '9':
        # if '0' <= c <= '9': #문자열도 비교 가능!
        #     digit = ord(c) - ord('0') # c='0은 안됨!
        # else:
        #     break
        value = value * 10 + ord(c) - ord('0')
    return value


a = "123"
#a = [1,2,3]
print(type(a))
b = atoi(a)
print(type(b))
```

#### 유투브 방식(itoa)

```python
def itoa(num):
    x = num # 몫
    y = 0 # 나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10 # x//= 10
        # arr.append(chr(y+ ord('0')))
        arr.append(y)

    arr.reverse()
    # str = "".join(arr)
    return arr

x= 123
print(x, type(x))
str = itoa(x)
print(str, type(str))
```



### strcmp

> 문자열이 같은지 비교!

```python
def strcmp(s1, s2):

    if len(s1) != len(s2):
        return False
    else:
        i = 0 # 초기식
        while i < len(s1) and i < len(s2): #조건식
            if s1[i] != s2[i]:
                return False
            i += 1#증감식
    return True

a = "abcd"
b = "abc"

print(strcmp(a,b)) # True, False

# False
```

### int_float

> 여러가지 타입 확인

```python
str = "123"
str2 = "12.3"

print(int(str), type(int(str)))
print(float(str2), type(float(str2)))

test = "1+2"
print(test)
print(repr(test))
print(eval(test))
print(eval(repr(test)))
print(eval(eval(repr(test))))


#123 <class 'int'>
#12.3 <class 'float'>
#1+2
#'1+2'
#3
#1+2
#3
```



### 패턴매칭

#### 패턴매칭에 사용되는 알고리즘들

- 고지식한 패턴 검색 알고리즘(Brute Force) (구현)
  - 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작
- 카프-라빈 아고리즘(안해도됨)
- kmp알고리즘(개념만)
  - 비교하다가 다른게 나오면 동일한 패턴이 나온 곳부터 다시 비교시작!
- 보이어-무어 알고리즘(개념만)
  - 패턴에 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이 만큼이 된다.
  - 패턴내에 존재하는 경우 그 부분이 기준이 됨

```python
str1 = "A pattern matching algorithm"
str2 = "rithm"

def brute_force(str1, str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1):
        cnt = 0
        for j in range(B):
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break

        if cnt == B:
            print("여기부터 일치", i)
            return i
    return -1

tmp = brute_force(str1, str2)
print(tmp)
```



#### exclusive-or(논리합)

- XOR이라고도 함

| x    | XOR  | y    |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 0    | 1    | 1    |
| 1    | 0    | 1    |
| 1    | 1    | 0    |

