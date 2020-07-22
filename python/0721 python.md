# 데이터 & 제어문

## 1 리스트

### 1. 요소들의 개수 구하기.

> 주어진 이름으로 이루어진 리스트에서 몇명이 포함되어 있는지 구하기

``` python
star = ['현우', '경민', '봉현', '병훈', '수지']
# 방법 1
len(star) # star의 길이, 즉 리스트 요소의 개수를 뜻함.

# 방법2
count = 0
for i in star:
    count += 1
print(count)
```



### 2. 중복된 개수 구하기

> 다음 리스트에서 '수지'가 몇번 나왔는지 구하기

```python
star = ['현우', '수지', '경민', '수지', '봉현', '병훈', '수지', '현우', '수지']

#방법 1
star.count('수지') # 리스트 star안에서 '수지'의 카운트를 셈

#방법2
count = 0
for i in star:
    if i == '수지':
    	count += 1
print(count)
```



###  3. 최댓값 구하기

> 주어진 리스트의 요소 중에서 최댓값을 출력하기

```python
numbers = [7, 15 , 23, 8, 30, 41, 29, 38, 41, 53, 42, 31]
#방법 1
max(numbers) # max는 최대를 찾아줌

#방법 2
sorted(numbers)[-1] #sorted는 작은 크기 순으로 정리, [-1] 리스트중 제일 끝에 항목

#방법 3
max_number = numbers[0]
for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)
```



### 4. 최솟값 구하기

``` python
numbers = [7, 15 , 23, 8, 30, 41, 29, 38, 41, 53, 42, 31]
#방법 1
min(numbers) # min는 최소를 찾아줌

#방법 2
sorted(numbers)[0] #sorted는 작은 크기 순으로 정리, [0] 리스트중 첫 항목

#방법 3
min_number = numbers[0]
for number in numbers:
    if min_number < number:
        min_number = number
print(min_number)
```



### 4. 최댓값과 등장 횟수 구하기

```python
numbers = [13, 15, 18, 24, 15, 24, 16, 20, 24, 13, 17, 24]
#방법 1
print(max(numbers), number.count(max(numbers)))

#방법 2
count = 0
max_number = numbers[0]
for number in numbers:
    if max_number <= number:
        max_number = number
        count = 1
    elif max_number == number:
        count+=1
print(max_number)
print(count)
```



## 2 단어

### 1. 단어 제거

```python
# 입력 apple 출력 pple

word = input()

# 방법 1
word.replace('a','')

# 방법 2
result = ''
for char in word:
    if char != a:
        result = result + char
print(result)
```



### 2. 단어 뒤집기

```python
# 입력 apple 출력 elppa

word = input()

# 방법 1
print(word[::-1])

# 방법 2
reversed_word=''
for index in range(len(word)-1,-1,-1): # 0까지로 하면 0자리를 포함하지 않으니 -1까지, -1단위로
    char = word[index]
    reversed_word += char
print(reversed_word)

# 방법 3
result =''
for char in word:
    result = char + result
print(result)   
```



