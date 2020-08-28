### and/ or 연산

```python
def true():
    print("참을 리턴")
    return True

def false():
    print("거짓을 리턴")
    return False

if true() and true():
    print("실행")
# 참을 리턴/ 거짓을 리턴/ 실행

if true() and false():
    print("실행")
# 참을 리턴/ 거짓을 리턴

if false() and true():
    print("실행")
# 거짓을 리턴
    
if false() and false():
    print("실행")
# 거짓을 리턴

if true() or true():
    print("실행")
# 참을 리턴/ 실행

if true() or false():
    print("실행")
# 참을 리턴/ 실행

if false() or true():
    print("실행")
# 거짓을 리턴/ 참을 리턴/ 실행

if false() or false():
    print("실행")
# 거짓을 리턴/ 거짓을 리턴

# 예시
visited = [[1,1,1],
           [1,1,1],
           [1,1,1]]
r ,c  = 1, 2
#사방 탐색을 하려고 하는데 이때 오른쪽을 확인하려고 함.
nr = r + 0
nc = c + 1
if 0 <= nr < 2 and 0 <= nc < 2 and visited[nr][nc] == 0:
    print("실행")
    
if visited[nr][nc] == 0 and 0 <= nr < 2 and 0 <= nc < 2:
    print("실행")
    # list index out of range
```



### SWEA_1211_Ladder2

```python
# 내풀이
def dfs(x, y):
    visited[x][y] = 1
    global cnt
    if x == 99:
        return

    for i in range(3):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < 100 and 0 <= my < 100:
            if not visited[mx][my] and arr[mx][my] == 1:
                cnt += 1
                return dfs(mx, my)

for i in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, 1]
    dy = [1, -1, 0]
    result = []
    total = []
    for j in range(100):
        cnt = 0
        visited = [[0] * 100 for _ in range(100)]
        if arr[0][j] == 1:
            dfs(0, j)
            result.append(cnt)
        total.append(cnt)
    min_index = total.index(min(result))
    print('#{} {}'.format(tc, min_index))

# 쌤 풀이(반복문)
dc = [-1, 1]
def dir_check(r, c):
    for i in range(2):
        nc = c + dc[i]
        if 0<= nc < 100 and ladder[r][nc] == 1:
            return i
    return 2

def go(st):
    col = st_pos[st]
    cnt = 0
    idx = st
    for i in range(100):
        d = dir_check(i, col)
        if d < 2 :
            idx += dc[d]
            cnt += abs(col - st_pos[idx])
            col = st_pos[idx]
        cnt += 1
    return cnt


for tc in range(10):
    # 테스트 케이스 번호 입력
    tc_num = int(input())
    # 2차원 리스트 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작 좌표를 담을 리스트
    st_pos = []
    # 시작 좌표를 다 담았다.
    for i in range(100):
        if ladder[0][i] == 1:
            st_pos.append(i)
    # 임의의 큰값으로 초기화
    min_value = 987654321
    # 어차피 정답으로 사용될거니 안쓰이는 수 아무거나로 초기화
    ans_idx = -1
    for i in range(len(st_pos)):
        tmp = go(i)

        if tmp <= min_value:
            min_value = tmp
            ans_idx = st_pos[i]

    print("#{} {}".format(tc_num, ans_idx))
```



### 2차원 리스트 DFS

```0
DFS를 사용하여 1의 개수 세서 출력!
input
7
0000000
0000000
0011100
0010111
0110010
0011100
0000000
```

- 풀이

```python
# 상하 좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r,c):
    # 개수를 위한 글로벌 선언
    global cnt
    # 요기 왔다는 건 1이라는 뜻이므로 카운트 증가
    arr[r][c] = 0
    cnt += 1
    # 4방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 벗어나면 out, 다음좌표가 0이라면 out
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0:
            continue
        DFS(nr, nc)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            # 개수를 매번 새로 세야 하기 때문에
            cnt = 0
            DFS(i,j)
            print(cnt)
```



### SWEA_4615_재미있는 오셀로 게임

```
1. 인풋을 받는다
2. 입력은 열행 컬러
3. 돌을 놓았을 때 8방향을 탐색을 하면서 나와 같은 컬러를 찾는다.
(이때 중간에 공백이 있거나, 맵의 범위를 벗어나면 수행X)
4. 찾은 컬러의 좌표부터 지금 놓은 좌표까지 돌아오면서 색깔을 모조리 다 나의 컬러로 바꾼다.
5. 위의 과정을 M번 반복하면 끝
```

