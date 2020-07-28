### 1. MAP

```python
numbers_str = '12 12 1 3 4 5'
numbers = map(int, numbers_str.split())
print(numbers) # => <map object at 0x7f117e6522b0>
print(type(numbers)) # => <class 'map'>
print(len(numbers))
[출력]
TypeError: object of type 'map' has no len()
    
numbers_str = '12 12 1 3 4 5'
numbers = list(map(int, numbers_str.split()))
print(numbers)
print(type(numbers))
print(len(numbers))
[출력]
[12, 12, 1, 3, 4, 5]
<class 'list'>
6
```

- map은 엄밀히 말하면 list타입이 아님.



### 2. 중복제거방법

-  set을 이용한 중복제거

```python
words = 'apple'
[입력]
print(words)
print(set(words))
print(list(set(words)))
[출력]
apple
{'l', 'p', 'e', 'a'}
['l', 'p', 'e', 'a']
```

-  for문과 .remove()를 이용한 중복제거

```python
words = 'apple'
letters = []
for word in words:
  if word in letters:
    letters.remove(word)
    letters.append(word)
  else:
    letters.append(word)
print(letters)
```



### 3. 복사

```python
a = [1, 2, 3, 4]
b = a[:]
a[2] = 5

c = 10
d = c
c = 5

print(a)
print(b)
print(c)
print(d)

[출력]
[1, 2, 5, 4]
[1, 2, 3, 4]
5
10
```



### 4. SW Expert Academy 문제풀이

- 2072_ 홀수만 더하기 (clear)
- 2071_평균값 구하기 (clear)
- 2070_큰 놈, 작은 놈, 같은 놈 (clear)