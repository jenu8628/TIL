# 큐(Queue)

- 순열(재귀)
- 큐
- 우선순위 큐 -> Tree(Heap)
- BFS(너비우선 탐색) (중요!)
- 큐의 활용: 버퍼

## 큐

### 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조(FIFO: First In Fist Out)
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제 됨



### 큐의 구현

- 공백 큐 생성 : createQueue();
- 원소 삽입 : enQueue(A);
- 원소 반환/삭제 : deQueue();

#### 삽입 : enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
- front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
- 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능 함

```python
def Queue(item):
	global rear
    if isFull() : print("Queue_Full")
    else:
        rear <- rear + 1;
        Q[rear] <- item;
```

#### 삭제 : deQueue()

```
deQueue()
	if(isEmpty()) then Queue_Empty();
	else{
		front <- front + 1;
		return Q[front]
	}
end deQueue()
```



### 실습

- Queue1

```python
# front, rear 이용
Q = [0] * 100
front, rear = -1, -1

def enQueue(item):
    global rear
    if rear == len(Q) -1: 
        print("Queue Full")
    else:
        rear = rear + 1 # rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[front + 1]
    
enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
```



- Queue2 (실제 사용은 이걸로 하면 됨!)

```python
Q = []

Q.append(1)
print(Q)
Q.append(2)
print(Q)
Q.append(3)
print(Q)

print(Q.pop(0))
print(Q)
print(Q.pop(0))
print(Q)
print(Q.pop(0))
print(Q)
```

#### 

#### 원형큐

> 기존에 선형큐의 단점을 보완 / Full이 아니지만 Full로 인식해서 발생하는 문제점을 해결하기 위해

```python
# front, rear 이용
SIZE = 4
Q = [0] * SIZE
front, rear = 0, 0

def enQueue(item):
    global rear
    if (rear+1) % SIZE == front: #full
        print("Queue Full")
    else:
        rear = (rear + 1) % SIZE  # rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front = (front + 1) % SIZE
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[(front + 1) % SIZE]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())

#1
#1
#2
#3
#[4, 1, 2, 3]
```



### 우선순위 큐의 특성

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨



## BFS(Breadth First Search) - 너비 우선 탐색

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용



### BFS알고리즘

- 입력 파라미터: 그래프 G와 탐색 시작점 v(enQ시 방문처리)

```python
def BFS(G, v) :             # 그래스 G, 탐색 시작점 v
    visited = [0] * (n+1)   # n : 정점의 개수
    q = []              # 큐 생성

    q.append(v)         # 시작정점 v를 enQueue
    visited[v] = 1      # 방문한 것으로 표시

    while len(q) != 0:      # 큐가 비어있지 않은 경우
        # t = q.pop[0]
        v = q.pop(0)        # deQueue(왼쪽원소 반환)
        for w in G[v]:           # 정점 v와 인접한 정점 w에 대해
            if not visited[w]:   # 방문하지 않은 곳이라면
                q.append(w)    # enQueue
                # 시작점에서 얼마나 떨어져 있나 알려면
                # visited[w] = visited[t] + 1
                visited[w] = 1 # 방문한 것으로 표시

```

#### BFS예시문제 코드 

1. 인접행렬

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    # 큐, 방문
    Q = []
    visited = [0]*(V+1)
    # enQ(v), visit(v)
    Q.append(v)
    visited[v] = 1
    print(v, end = " ")
    # 큐가 비어있찌 않은 동안
    #while len(Q) != 0:
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문안한 정점이면
            # enQ(v), 방문처리
        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
                print(w, end = " ")


# 입력 -> 인접행렬
V, E = map(int, input().split())
temp = list(map(int, input().split()))
# 인접행렬 초기화
G = [[0] * (V+1) for _ in range(V+1)]
# 인접행렬 저장
for i in range(E):
    s, e = temp[2*i], temp[(2*i)+1]
    G[s][e] = G[e][s] = 1
for i in range(1,V+1):
    print("{} {}".format(i, G[i]))

bfs(1)
# 출력
#1 [0, 0, 1, 1, 0, 0, 0, 0]
#2 [0, 1, 0, 0, 1, 1, 0, 0]
#3 [0, 1, 0, 0, 0, 0, 0, 1]
#4 [0, 0, 1, 0, 0, 0, 1, 0]
#5 [0, 0, 1, 0, 0, 0, 1, 0]
#6 [0, 0, 0, 0, 1, 1, 0, 1]
#7 [0, 0, 0, 1, 0, 0, 1, 0]
#1 2 3 4 5 7 6 
```

2. 인접리스트

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    # 큐, 방문
    Q = []
    # enQ(v), visit(v)
    Q.append(v)
    visited[v] = 1
    print(v, end = " ")
    # 큐가 비어있찌 않은 동안
    #while len(Q) != 0:
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문안한 정점이면
            # enQ(v), 방문처리
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                # visited[w] = 1
                visited[w] = visited[v] + 1
                print(w, end = " ")

# 입력 -> 인접리스트
V, E = map(int, input().split())
temp = list(map(int, input().split()))
# 인접리스트
#G = [[] for _ in range(V+1)]
G = {i : [] for i in range(1, V+1)}
print(G)
visited = [0] * (V + 1)
for i in range(E):
    s, e = temp[2*i], temp[(2*i)+1]
    G[s].append(e)
    G[e].append(s)
print(G)
bfs(1)
print()
# 1에서 가장 멀리 있는 정점의 번호는 얼마이고 몇칸 떨어져 있을까요?
maxI = 0
for i in range(1, V+1):
    if visited[maxI] < visited[i]:
        maxI = i
        # 시작이 1이기 때문
print(maxI, visited[maxI] - 1)
```

