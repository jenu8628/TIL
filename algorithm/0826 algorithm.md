# 스택1

## 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형구조를 가짐
  - 선형구조: 자료간의 관계가 1대1의 관계를 가짐
  - 비선형구조: 자로간의 관계가 1대N의 관계를 가짐
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있음.
- 마지막에 삽입한 자료를 가장 먼저 꺼냄 후입선출이라고 부름



### 자료구조와 연산

- 자료구조 : 자료를 선형으로 저장할 저장소
- 연산
  - 삽입: 저장소에 자료를 저장. push
  - 삭제: 저장소에서 자료를 꺼냄. pop
  - 스택이 공백인지 아닌지 확인하는 연산. isEmpty(pop할때 항상 확인)
  - 스택의 top에 있는 item(원소)을 반환하는 연산.peek(뭐가있는지 보는거임)



### 스택구현하기

```python
# C style
def push(item):
    global top
    if top > 100 -1 :
        return
    else:
        top += 1
        stack[top] = item

def pop(): # isEmpty인지 확인중요!
    global top
    if top == -1:
        print("Stack is Empty!!!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

stack = [0] * 100 # 고정
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())

#python style
def push(item):
    s.append(item)
    
def pop():
    if len(s) == 0:
        #underflow
        return
    else:
        return s.pop(-1)


#바로 사용
stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
#pop
if stack:   # len(stack) != 0
    print(stack.pop())
if stack:   # len(stack) != 0
    print(stack.pop())
if stack:   # len(stack) != 0
    print(stack.pop())
if stack:   # len(stack) != 0
    print(stack.pop())
```

## 스택의 응용

### 1. 괄호검사 

- 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
- 괄호 사이에는 포함 관계가 존재

```python
def check(bracket):
    # 인자로 넘어온 괄호들을 순화하면서 검사
    # 여는 괄호라면 무조건 push
    # 닫는 괄호라면 스택에 top위치와 비교하여 재짝이면 pop
    # 제 짝이 아니라면 False
    # 끝까지 순회했을 때 스택의 길이가 0이 아니라면 False
    stack = []

    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[':
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i] == '}' or bracket[i] == ']':
            if len(stack) == 0:
                return False
            tmp = stack.pop()

            if bracket[i] ==')' and tmp == '(':
                continue
            elif bracket[i] == '}' and tmp == '{':
                continue
            elif bracket[i] == ']' and tmp == '[':
                continue
            return False
    if len(stack)>0:
        return False

    return True

for _ in range(int(input())):
    bracket = input()
    print(check(bracket))
```

###  2. Function call

```python
def func2():
    print("함수 2 시작")
    print("함수 2 종료")
    
def func1():
    print("함수 1 시작")
    func2()
    print("함수 1 종료")
    
print("메인시작")
func1()
print("메인끝")

# 리턴값은 없으나 실행할게 없으면 부른 곳으로 돌아가게됨!
```

### 3. factorial

```python
def factorial(n):
    # 종료조건
    if n == 1:
        return 1
    return n * factorial(n-1)
```



### 4. fibo

```python
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

## Memoization

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술. 동적 계획법의 핵심이 되는 기술

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다.
# memo[0]을 0으로 memo[1]는 1로 초기화 한다

def fibo1(n):
    global memo # 참조형이라 안써도됨
    if n >= 2 and len(memo) <=n :
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0, 1]
```

```python
N = int(input)
memo = [-1] * (N+1)
memo[0] = 0
memo[1] = 1

def fibo(N):
    if memo[N] == 1:
        memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]
```





## DP(Dynamic Programming)

- 동적계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제(or 결정문제)를 해결하는 알고리즘

- 피보나치 수 DP적용
  - 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있음

```python
def fibo2(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
```



#### DP의 구현방식

- recursive 방식 : fib1()
- iterative 방식 : fib2()

- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문



## DFS(깊이 우선 탐색)

- 비선형구조인 그래프 구조(tree)는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

  - 표현: 메모리 저장 (방법도 선형과는 다름)
    - 인접행렬 (C나 java는 이걸 많이씀)
    - 인접리스트 (파이썬인 이게 더 수월할 수도)
    - 간선배열
    - 인접행렬과 인접리스트를 많이 쓴다.
  - 순회(빠짐없이) : DFS, BFS(너비우선 탐색)두가지가 있음

  - 선형(쉬움)
    - 표현
    - 순회 : for

- 깊이 우선 탐색(DFS)

  - 시작 정점의 한 방향으로 갈수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정접으로 되돌아 와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
  - ex) fibo의 Call Tree
  - stack이용구현(속도는 stack이용이 빠름), 재귀로 구현(이방법을 많이 씀)
    - 가장 마지막으로 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용



1. 시작 정점 v를 결정하여 방문

2. 정점v에 인접한 정점중에서
   1. 방문하지 않은 정점 w가 있으면, 정접 v를 스택에 push하고 정점 w를 방문 그리고 w를 v로 하여 다시 위의2를 반복
   2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 위의 2를 반복
3.  스택이 공백이 될 때까지 2를 반복

### DFS알고리즘 - 재귀(응용 280p)

```python
# G: 그래프 v: 시작정점
DFS-Recursive(G, v)
	visited[v] <- True // v 방문 설정
    # v에 인접한 모든 정점에 대해서
    For each all w in adjacency(G, v)
    	if visited[w] != True
        	DFS_Recursive(G, w)
```

ex) 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    #방문체크
    visited[v] = 1
    print(v, end=" ")
    # v의 인접한 정점중에서 방문 안한 정점을 재귀 호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

#정점, 간선
N, E = map(int, input().split())
# 간선들
temp = list(map(int, input().split()))
#인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
# 방문체크
visited = [0] * (N+1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)
--------------------------------------------------------------
# 쌤풀이
#input
#정점수, 간선수
# 7 8
----------# 입력값
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

def DFS(v):
    print(v, end= " ")
    visited[v] = 1
    for i in range(1, V+1):
        #현재 내 정점 v와 연결되어 있는지 확인
        if arr[v][i] == 1 and visited[i] ==0:
            DFS(i) #6


# 입력
V, E = map(int, input().split())
# 인접행렬 생성 준비
# 한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해서
# 0번 인덱스따위 버려버리기
arr = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    st, ed = map(int, input().split())
    #무향 그래프이기 때문에 서로 연결되어있음을 표시
    arr[st][ed] = arr[ed][st] = 1

# 방문 배열 선언
visited = [0]*(V+1)
DFS(1)
```



### DFS알고리즘 - 반복

```python
stack s
visited[]
DFS(v)
	push(s,v)
    While not isEmpty(s)
    	v <- pop(s)
        if not visited[v]
        	visit(v)
            for each w in adjacency(v)
            	if not visited[w]
                	push(s,w)
```

ex)

```python
#input
#정점수, 간선수
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

# 입력
V, E = map(int, input().split())
# 인접행렬 생성 준비
# 한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해서
# 0번 인덱스따위 버려버리기
arr = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    st, ed = map(int, input().split())
    #무향 그래프이기 때문에 서로 연결되어있음을 표시
    arr[st][ed] = arr[ed][st] = 1
# 방문배열
visited = []
# 스택
stack = []
#시작 정점을 담는다.
stack.append(1)
1376
# 스택이 빌 때까지 무한히 반복
while len(stack) > 0: #stack =[]
    # 정점을 하나 꺼낸다.
    v = stack.pop() # v = 4 / stack = [2,4]
    # 해당 정점이 방문한 정점이 아니라면
    if v not in visited: # 1이 visited에 없으면/ 현재 visited=[1,3,7,6,5,2]
        print(v, end=" ")
        # 정점을 방문 체크
        visited.append(v) #visited = [1,3,7,6,5,2,4]

        # 현재 정점에서 연결되어 있는 모든 정점을 탐색하기 위한 반복문
        for i in range(1, V+1): # 1에서부터 시작
            #현재 정점과 연결되어 있으면서 방문하지 않은 정점 i가 있다면
            if arr[v][i] == 1 and i not in visited: #arr[4][i]
                # 모두 다 스택에 push
                stack.append(i) # stack = []
```

### DFS에 대해 설명하시오?

- 출발점에서 점점 멀어지는 방향으로 탐색을 하는 방법
- 인접한 노드에서 어디로 갈지 택하고 갈 수 있는 최대한 멀리 가는방식
- stack을 사용하여 반복문을 활용할 수 있구
- 재귀를 이용하여 할 수 있다.



