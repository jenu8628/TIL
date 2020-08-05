### 1. 델타 검색방법

```python
arr=[ [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]
    ]
N=len(arr)
M=len(arr[0])

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

for x in range(N):
    for y in range(M):
        for i in range(4):
            testX = x+dx[i]
            testY = y+dy[i]

            if 0 <= testX < N and 0 <= testY < M:
                print(arr[testX][testY], end= " ")


            # 혹은 아래처럼 해도 됨
            # if testX<0 or testX>=N: continue
            # if testY<0 or testY>=M: continue
            # print(arr[testX][testY], end=" ")
```



#### 1-1) 델타검색문제

> 5X5 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하는 문제
>
> 25개의 요소에 대해 모두 조사하여 총합을 구하세요~

```python
arr = [[1, 2, 3, 4, 5],
       [5, 6, 7, 8, 9],
       [10, 3, 4, 2, 8],
       [8, 34, 2, 0, 4],
       [4, 9, 31, 27, 4]
]

N = len(arr)
M = len(arr[0])

dx = [-1,0,1,0 ]
dy = [0,-1,0,1 ]
result = 0

for x in range(N):
    for y in range(M):
        for k in range(4):
            testX = x+dx[k]
            testY = y+dy[k]

            if 0<= testX < N and 0<= testY < M:
                result += abs(arr[x][y] - arr[testX][testY])

print(result)
```



### 2 비트연산자

| 연산자 | 의미                                        |
| ------ | ------------------------------------------- |
| &      | 비트 단위로 AND연산을 한다                  |
| \|     | 비트 단위로 OR 연산을 한다                  |
| <<     | 피연산자의 비트 열을 왼쪽으로 이동시킨다.   |
| >>     | 피연산자의 비트 열을 오른쪽으로 이동시킨다. |

```python
#비트 단위의 연산은 2진법으로 바뀌어서 하게 된다.
a=5 #0101
b=3 #0011
print(a & b) # 0001, 논리곱 => 1
print(a | b) # 0111, 논리합 => 7
print(1 << 3) # 0001 -> 1000 : 8 (2**3)
print(a ^ b) # 0110  => 6 / ^ : 같으면 0 다르면 1이 나옴
```

- << 연산자

  - 1<<n : 2**n, 즉 원소가 n개일 경우의 모든 부분집합의 수를 의미

- &연산자

  - i&(1<<j): i의 j번째 비트가 1인지 아닌지를 리턴

  | i    | j =0,1,2 |
  | ---- | -------- |
  | 0    | 000      |
  | 1    | 001      |
  | 2    | 010      |
  | 3    | 011      |
  | 4    | 100      |
  | 5    | 101      |
  | 6    | 110      |
  | 7    | 111      |

  3 & (1<<0) : 011 & 001 => T

  3 & (1<<1) : 011 & 010 => T

  3 & (1<<2) : 011 & 100 => F

  FTT => 011 

  즉 3의 비트열을 찾게 됨

#### 2-1. 부분집합을 구하는 다양한 방법

```python
# 방법1 (원소가 4개인 집합의 부분집합)(완전탐색)
bit = [0, 0, 0, 0]
for i in range(2) :
    bit[0] = i                  # 0번째 원소
    for j in range(2) :
        bit[1] = j              # 1번째 원소
        for k in range(2) :
            bit[2] = k          # 2번째 원소
            for l in range(2) :
                bit[3] = l      # 3번째 원소
                print(bit)      # 생성된 부분집합 출력

# 방법2 (원소가 3개인 집합의 부분집합)
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i                  # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            print(bit)      # 생성된 부분집합 출력

# 방법3
def printList(arr, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(arr[i], end=" ")
    print()

arr=[1, 2, 3]
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i                  # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            printList(arr, bit)      # 생성된 부분집합 출력
            
# 비트연산 방법
arr = [1,2,3]
n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ',')
    print()
print()
```

#### 2-2. 부분집합 문제

> 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해 보자.

```python
N = 10
K = 0
arr = list(map(intm input().split()))
cnt = 0
for i in range(1<<N):
    SUM = 0
    sub = []
    for j in range(N):
        if i & (1<<j):
            sub.append(arr[j])
            SUM += arr[j]
            
    if SUM == k:
        cnt += 1
        print(sub)
```



### 3. 검색(Search)

> 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

- 종류
  - 순차 검색(sequential search) (시험지 찾을 때 한장씩 넘겨찾는거?)
  - 이진 검색(binary search) (정렬되있는 상태에서 반씩 찾아서 찾는 것)
  - 해쉬(hash) (함수만들어서 하는것(B형시험볼때 필요 Pass))

#### 3.1 순차검색(Sequential Search)

- 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
- 검색 대상의 수가 많은 경우에 비효율적
- 정렬되어 있지 않은 경우
  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음.
  - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
- 정렬되어 있는 경우
  - 자료를 순차적으로 검색하면서 키값을 비교, 원소의 키값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 검색종료

```python
# 정렬되어 있지 않는 경우
def sequentialSearch(arr, len(arr), key)
	i = 0
    while i < n and a[i] != key:        
        i += 1
    if i < n: return i
    else: return -1

# 정렬되어 있는 경우
def sequentialSearch(arr, len(arr), key)
	i = 0
    while i < n and a[i] < key: # 키값보다 작으면 종료!        
        i += 1
    if i < n and a[i] == key : return i
    else : return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(sequentialSearch(arr, len(arr), key))
```



#### 3-2. 이진 검색(Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 진행
- 검색 범위를 반으로 줄임 ( 소주 병뚜껑  UP&DOWN 게임)
- 정렬된 상태에서만 가능

```python
# 기본
def binarySearch(a, key):
    start = 0
    end = len(a)
    while start <= end:
        middle = (start + end) // 2
        # ==
        if a[middle] == key:
            return True, middle
        # >(작은경우)
        elif a[middle] > key:
            end = middle - 1
        # <(큰경우)
        else:
            start = middle + 1
        # 못찾은 경우
    return False, -1
# 재귀함수 이용
#후에 다시 할 예정
#pass
    
arr = [2, 4, 7, 9, 11, 19, 23]
key = 7
print(bin_search(arr, key))
```



#### *인덱스

- 인덱스라는 용어는 DB에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컬음. DB(Database)분야가 아닌 곳에서는 Look up table등의 용어를 사용하기도 함
- 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문에 저장하는데 필요한 디스크 공간이 테이블을 저장하는데 필요한 디스크 공간보다 적다.



### 4. 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 주어진 리스트 중에서 최소값을 찾아 그 값을 리스트의 맨 앞에 위치한 값과 교환 반복

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
```

- 달팽이 문제(2차배열 정렬)

``` python
cnt = 1
arr = [[0]*5]

row_start = 0
row_end = 4
col start = 0
col_end = 4

while row_start = row_end and col_start <= col_end:
    #왼쪽 -> 오른쪽
    for i in range(col_start, col_end+1):
        arr[row_start][i] = cnt
        cnt += 1
    row_start += 1
    
    #위 -> 아래
    for i in range(row_start, row_end +1):
        arr[col_end][i] = cnt
        cnt += 1
    col_end -= 1
    
    #오른쪽 -> 왼쪽
    for i in range(col_end, col_start -1, -1):
        arr[row_end][i] = cnt
        cnt += 1
    row_end -=1
    
    # 아래 => 위
    for i in range(row_end, row_start - 1, -1):
        arr[i][col_start] = cnt
        cnt += 1
    col_start += 1

print(arr)
```



### SWEA 풀이

- 1545_거꾸로 출력해 보아요
  -  매우 쉬움
- 1859_백만 장자 프로젝트
  - 어려웠음. 코드를 만드는거 자체는 크게 어렵지 않으나 input이 커서 시간초과로 많이 틀림.
  - 시간 초과가 되지 않기 위해 생각하기가 어려웠음.
- 1926_간단한 369게임
  - 훨씬 간단하게 코드를 작성할 수 있을거 같은데 아직 나에게는 그러한 방법이 떠오르지 않아 가정문으로만 써놓았다. 반복문과 가정문을 적절히 섞어서 놓는다면 코드가 훨씬 짧아질 것 같음