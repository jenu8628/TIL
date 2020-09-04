### swea1224_계산기

```python
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for tc in range(1, 11):
    input()
    line = input()
    ans = ''
    # 스택 준비
    stack = []

    for i in range(len(line)):
        # 괄호라면
        if line[i] == '(' or line[i] == ')':
            # 여는 괄호는 우선순위가 제일 높으므로 무조건 삽입
            if line[i] == '(':
                stack.append(line[i])
            else:
                # 여는 괄호가 나올 때까지 무조건 pop
                while stack[-1] != '(':
                    ans += stack.pop()
                # 여는 괄호하나 버리기
                stack.pop()
        elif line[i].isdigit():
            ans += line[i]
        # 연산자일 때
        else:
            if len(stack) == 0:
                stack.append(line[i])
            else:
                # 연산자 우선순위를 비교해서
                # 스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])
    # 남아있는 스택 비우기
    while len(stack) > 0:
        ans += stack.pop()
# ######################## 중위 표현식 -> 후위표현식
    for i in ans:
        # 숫자면 스택에 쌓기
        if i.isdigit():
            stack.append(int(i))
        # 연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A+B)
            elif i == '-':
                stack.append(A-B)
            elif i == '*':
                stack.append(A*B)
            elif i == '/':
                stack.append(A/B)
    print('#{} {}'.format(tc, stack.pop()))
```



### swea1220_Magnetic

```python
for tc in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    ans = 0
    for i in range(N):
        # 내가 만나야 될 컬러
        state = 1
        for j in range(N):
            # 내가 빨강을 만나야하고 마침 내 자리가 빨강이라면
            if state == 1 and arr[j][i] == '1':
                state = 2
            # 내가 파랑을 만나야 하고 마침 내 자리가 파랑이면 교착상태 1 증가
            elif state == 2 and arr[j][i] == '2':
                state = 1
                ans += 1

    print("#{} {}".format(tc, ans))
```

### swea4047_ 영준이의 카드 카운팅

```python
pattern = {'S':0, 'D':1, "H":2, 'C':3}

T = int(input())
for tc in range(1, T+1):
    line = input()
    card = [[0]*14 for _ in range(4)]

    # 에러인지 아닌지를 위한 bool 변수
    is_error = False

    for i in range(0, len(line), 3):
        # 패턴
        card_p = pattern[line[i]]
        # 번호
        card_n = int(line[i+1:i+3])

        # 이미 가지고 있는 카드라면 종료
        if card[card_p][card_n] == 1:
            is_error = True
            break
        # 그게아니라면 카드 표시
        card[card_p][card_n] = 1
        # 0번 인덱스는 카드 카운팅을 위해 사용
        card[card_p][0] += 1

    print("#{}".format(tc), end = " ")
    if is_error:
        print("ERROR")
    else:
        for i in range(4):
            print("{}".format(13-card[i][0]), end = " ")
        print()
```

### 이차원거리 BFS

```python
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    queue = [(r,c)]
    dist[r][c] = 1

    while len(queue)>0 :
        curr_r, curr_c = queue.pop(0)

        #4방향 탐색
        for i in range(4):
            nr = curr_r+dr[i]
            nc = curr_c+dc[i]

            #범위를 벗어났다면 넘어가기
            if nr <0 or nr>= N or nc<0 or nc>=N:
                continue
            #갈수있는자리가 아니거나 이미 거리를 구했다면 넘어가기
            if arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            #그게 아니다.! 거리 갱신 후 큐에 삽입
            queue.append((nr,nc))
            dist[nr][nc] = dist[curr_r][curr_c]+1


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
#거리를 담을 배열
dist = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i,j)


for i in dist:
    print(*i)
```

