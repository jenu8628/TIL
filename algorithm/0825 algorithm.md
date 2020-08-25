## swea 풀이

### 1. swea1221_GNS

- 쌤풀이

```python
num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

T = int(input())
for tc in range(1,T+1):
    a,b = input().split() # tc와 range받기
    arr = list(input().split()) # 문제 받기
    cnt = [0]*10
    # 딕셔너리로 푸는 방법!
    for key in arr:
        cnt[num_dict[key]] += 1
    print("#{}".format(tc))
    for i in range(10):
        print(num_list[i] * cnt[i], end="")
    print()
```

- 내풀이

```python
gns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1,T+1):
    arr0 = input().split()
    arr1 = list(map(str, input().split()))
    
    for i in range(len(arr1)):
        for j in range(10):
            if arr1[i] == gns[j]:
                arr1[i] = int(j)
    arr1.sort()
    for k in range(len(arr1)):
        for n in range(10):
            if arr1[k] == n:
                arr1[k] = gns[n]
    print(arr0[0])
    for i in range(len(arr1)):
        print(arr1[i], end=" ")
```

- 다른 풀이

```python
t = int(input())
keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
dic = {}
for tc in range(t):
    put1 = []
    put1 = input().split()
    num = put1[0]

    lists = input().split()
    for key in keys:
        count = 0
        for li in lists:
            if key == li:
                count +=1
        dic[key] = count
    print(num)
    for k, v in dic.items():
        for i in range(v):
            print(f'{k}', end=' ')
```

### 2. swea_1974 스도쿠검증

- 기존풀이

```python
T = int(input())
for tc in range(1,T+1):
    arr_list = [list(map(int,input().split())) for i in range(9)]
    result = 1
    # result는 프린트 하기 위함
    for j in range(9):
        arr_height = set()
        arr_weith = set()
        for k in range(9):
            arr_weith.add(arr_list[j][k])
            arr_height.add(arr_list[k][j])
        if len(arr_weith) != 9 or len(arr_height) != 9:
            result = 0
            break
    # total은 반복문을 탈출하기 위함
    total = 0
    for x in range(0,9,3):
        for y in range(0,9,3):
            arr_sub = set()
            for m in range(3):
                for b in range(3):
                    arr_sub.add(arr_list[m+x][b+y])
            if len(arr_sub) != 9:
                result = 0
                total = 1
        # if total: 이라고 적어도 됨!
        if bool(total) == True:
            break

    print('#{} {}'.format(tc, result))
```

- 쌤풀이

```python
def check():

    for i in range(9):
        row = [0]*10
        col = [0]*10
        for j in range(9):
            # 행검사
            num1 = sudoku[i][j]
            # 열검사
            num2 = sudoku[j][i]
            # 0, False, [], None
            # 밑에는 1, True, [12]이런 식이라면 리턴 0
            # 즉 값이 있다면!
            if row[num1]:
                return 0
            if col[num2]:
                return 0
			# 위에 걸리지 않았다면 사용했음을 표시
            row[num1] = col[num2] = 1

            if i % 3 == 0 and j % 3 ==0:
                square = [0]*10
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if check():
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
```



### 파이참 단축키!

다음줄 : `shift` + `enter`

복사 : `ctrl` + `d`

이동: `alt`+ `shift` + `방향키`

들여쓰기 : `ctrl` + `alt` +`l`



### 3. swea_1258 행렬찾기

```python
def search_size(r, c):
    r_cnt = 0
    c_cnt = 0

    for i in range(r, N + 2):
        if arr[i][c] == 0:
            break
        r_cnt += 1
    for j in range(c, N + 2):
        if arr[r][j] == 0:
            break
        c_cnt += 1

    ans.append([r_cnt, c_cnt])
    # 지나간 곳이므로 0으로 바꿔줌
    init(r, c, r_cnt, c_cnt)
# 지나간 곳은 0으로 바꿔주는 함수
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r + r_cnt):
        for j in range(c, c + c_cnt):
            arr[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 2)
    arr[0] = arr[N + 1] = [0] * (N + 2)
    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0]
    ans = []

    for i in range(1, N + 2): # 0자리는 어차피 0
        for j in range(1, N + 2):
            if arr[i][j] != 0:
                search_size(i, j)
    # lambda는 익명함수 ans리스트에서 각각의 요소를 가져와서 뒤의 조건의 기준으로
    # 정렬을 하겠다.
    ans = sorted(ans, key=lambda x: ((x[0] * x[1]), x[0]))
    print("#{} {}".format(tc, len(ans)), end=" ")
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")
    print()
```



### lambda (익명함수) & key

```python
#lambda
def func(x,y):
    return x+y

print((lanbda x, y:x+y)(3, 5))
print(add(3,5))
print(func(3,5))
# 셋다 8이 나옴

add2 = lambda x, y : x+y

print(add2(5,5))
# 10

# key를 기준으로 정렬!
def f1(x):
    return x[0] #-x[0]이라하면 역순
ans =[[2,3],[3,4],[12,4],[4,5],[6,8]]

num = sorted(ans, key = f1)
```



### 회문

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            row = ''
            col = ''
            for k in range(M):
                row += arr[i][j+k]
                col += arr[j+k][i]
            if row == row[::-1]:
                print('#{} {}'.format(tc, row))
            if col == col[::-1]:
                print('#{} {}'.format(tc, col))
```



### 문자열 비교

```python
def brute_force(n, m):
    A = len(n)
    B = len(m)
    result = 0
    for i in range(B-A+1):
        cnt = 0
        for j in range(A):
            if n[j] == m[i+j]:
                cnt += 1
            else:
                break
        if cnt == A:
            result = 1
            break
    return result

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    total = brute_force(str1, str2)
    print('#{} {}'.format(tc, total))
```

### 글자수

```python
T = int(input())
for tc in range(1, T+1):
    X = input()
    Y = input()
    total = [0]*len(X)
    for i in range(len(X)):
        cnt = 0
        for j in range(len(Y)):
            if X[i] == Y[j]:
                cnt += 1
                total[i] = cnt
    max_number = total[0]
    for k in range(len(total)):
        if max_number < total[k]:
            max_number = total[k]
    print('#{} {}'.format(tc, max_number))
```

