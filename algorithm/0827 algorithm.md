# SWEA풀이

## 파이썬 문제해결 기본-string(3일차)

### 1. 문자열비교

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

# 쌤풀이
def check(str1, str2):
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            # 만약 현재 사이클에 다르다면 브레이크
            if str2[i+j] != str1[j]:
                break
        #중간에 브레이크 걸리지 않았다면 완벽히 찾은 것
        else:
            return 1
    #완벽히 찾지 못했다면 리턴 0
    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print("#{} {}".format(tc, check(str1, str2)))
    # -------------------------
    # in 활용
    # if str1 in str2:
    #     print("#{} {}".format(tc,1))
    # else:
    #     print("#{} {}".format(tc, 0))
    # ----------------------------
    # #find활용
    # ans = 0
    # if str2.find(str1) != -1:
    #     ans = 1
    # print("#{} {}".format(tc,ans))
```



### 2. 글자수

```python
#내풀이
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

# 쌤풀이
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    check_arr = [0]*26
    count_arr = [0] * 26

    #1 str1을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i)-ord('A')] = 1
    #2 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i)-65] == 1:
            count_arr[ord(i)-65] += 1
    print("#{} {}".format(tc, max(count_arr)))
    
# 다른 풀이(파이썬필살기??)
    # dict = {}
    # 
    # for i in str1:
    #     if i not in dict:
    #         dict[i] = str2.count(i)
    # print("#{} {}".format(tc, max(dict.values()))) 
```

### 달팽이채우기

```python
    #쌤풀이
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        arr = [[0] * N for _ in range(N)]

        d = 0  # 방향 0:우, 1:하, 2:좌, 3:상
        r = 0
        c = 0
        num = 1

        while num <= N * N:
            arr[r][c] = num  # 현재칸에 값을 저장
            num += 1  # 다음숫자준비

            # 다음칸을 결정
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nd] == 0:
                # 현재좌표를 갱신
                r, c = nr, nc
            else:
                d = (d + 1) % 4
                r += dr[d]
                c += dc[d]
```

### 회문

```python
# 내풀이
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

#쌤풀이
def check():
    # 전체 크기가 N
    for i in range(N):
        #가로 검사
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            if tmp == tmp[::-1]:
                return tmp
        #세로 검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    ans = check()
    print("#{} {}".format(tc, ''.join(ans)))
```

### zip 간단사용법

```python
#zip 같은 열끼리 묶어서 표현을 해준다
#열의 숫자가 같을 때
test1 = [1,2,3,4]
test2 = [5,6,7,8]
test3 = list(zip(test1, test2))
print(test3)
# [(1, 5), (2, 6), (3, 7), (4, 8)]

#열의 숫자가 다를 때
test4 = [1,2,3,4]
test5 = [5,6,7]
test6 = list(zip(test4, test5))
print(test6)
# [(1, 5), (2, 6), (3, 7)]

# 2차원 리스트
nums = [[1,2,3,],[4,5,6]]
# 모든요소
nums2 = list(zip(nums[0],nums[1]))
# 요소 하나를 통째로 취급
nums3 = list(zip(nums))
# 언팩킹을 하영 한번에 처리도 가능
nums4 = list(zip(*nums))
print(nums2)
print(nums3)
print(nums4)
#[(1, 4), (2, 5), (3, 6)]
#[([1, 2, 3],), ([4, 5, 6],)]
#[(1, 4), (2, 5), (3, 6)]

tmp = [1,2,3,4]
print(tmp)
print(*tmp)
print(list(zip(tmp)))
[1, 2, 3, 4]
1 2 3 4
[(1,), (2,), (3,), (4,)]
```

### swea_1216 회문2

```python
# 내풀이
for i in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    N = 100
    number = []
    # 0~100까지 검사
    for i in range(N):
        # 회문길이를 99부터 내려오면서 검사할 예정
        for j in range(N-1, 0, -1):
            # 행 또는 열에서 회문길이만큼 움직일 거리
            for m in range(100-j+1):
                row = ''
                col = ''
                # 회문이 맞는지 검사
                for k in range(j):
                    row += arr[i][k+m]
                    col += arr[k+m][i]
                if row == row[::-1]:
                    number.append(len(row))
                if col == col[::-1]:
                    number.append(len(col))
    max_number = max(number)

    print('#{} {}'.format(tc, max_number))

# 쌤풀이
def check(M):
    for i in range(N):
        for j in range(N-M+1):
            #가로
            tmp = words[i][j:j+M]
            #세로
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0

for tc in range(10):
    tc_num = int(input())
    N = 100
    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words)) # 세로줄

    for k in range(100, 0, -1):
        ans = check(k)
        if ans != 0:
            break
    print("#{} {}".format(tc_num, ans))
```

