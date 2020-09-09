# 트리

### 선형구조(1:1)

- 표현방법 : list
- 순회 : for문



### 비선형구조

- 이진트리(1:N)
  - 표현방법 : 1차원배열/ (저장)1차원배열(인접리스트)
  - 순회 : 전위순회 / 중위순회/ 후위순회



- 그래프(N:N)
  - 표현방법 : 인접행렬/ 인접리스트/간선배열
  - 순회 : DFS(stack) / BFS(Queue)



### 트리의 개념

- 비선형 구조
- 1:N의 관계 (부모1, 자식N)를 가지는 자료구조
- 한 개 이상의 노드로 이루어진 유한 집합
  - 노드 중 최상위 노드를 루트라 함



#### 용어 정리

- 형제 노드 - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리 - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들

- 차수
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(리프 노드) : 차수가 0인 노드/ 자식 노드가 없는 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수/ 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값 / 최대 레벨



## 1 이진 트리

> 모든 노드들이 2개의 서브트리를 갖는 형태

### 1-1 특성

- 레벨 i에서의 노드의 최대 개수는 2**i개
- 높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 (h+1)개, 최대 개수는 ((2**(h+1)) - 1) 개

### 

### 1-2 종류

- 포화 이진트리
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리 즉, 높이가 h일 때, ((2**(h+1)) - 1)개의 노드를 가진 이진 트리
- 완전 이진트리
  - 높이가 h이고 노드수가 n개일 때, 포화 이진트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진트리
- 편향 이진트리
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진트리
  - 트리로서의 가치가 없음.



### 1-3 순회

#### 1-3-1. 전위 순회

- 전위 순회 알고리즘

```python
def preorder_traverse(T): #전위 순회
    if T:			#T is not None
        visit(T)	# print(T.item) 방문처리X /이진트리는 방문처리 불필요
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```



#### 1-3-2. 중위 순회

- 중위 순회 알고리즘

```python
def inorder_traverse(T): #중위 순회
    if T:			#T is not None
        preorder_traverse(T.left)
        visit(T)
        preorder_traverse(T.right)
```



#### 1-3-3. 후위 순회

- 후위 순회 알고리즘

```python
def postorder_traverse(T): #후위 순회
    if T:			#T is not None
        preorder_traverse(T.left)
        preorder_traverse(T.right)
        visit(T)
```



### 1-4 표현

#### 1-4-1. 배열을 이용한 이진트리의 표현

- 루트의 번호를 1로하여 내려가면서 왼쪽부터 오른쪽으로 오름차순 순서대로 표현

- 노드 번호의 성질
  - 노드 번호가 i 인 노드의 부모 노드 번호 : i//2
  - 노드 번호가 i 인 노드의 왼쪽 자식 노드 번호 : 2**i
  - 노드 번호가 i 인 노드의 오른쪽 자식 노드 번호 : (2**i) +1
  - 레벨 n의 노드 번호 시작 번호 : 2**n

#### 1-4-2. 연결리스트를 이용한 이진트리의 표현

- 배열이용에 단점을 보완/ 자기참조 구조체

- `왼쪽자식/ 오른쪽자식/ 부모` 의 형태



### 1-5 이진탐색트리

- 효율적인 탐색작업

- key(왼쪽 서브트리)< key(루트노드) < key(오른쪽서브트리)
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음

#### 1-5-1. 탐색연산

- 탐색할 키 값x를 루트노드의 키 값과 비교
- 키값x == 루트노드의 키 값 : 탐색연산 성공
- 키 값x < 루트노드의 키 값 : 루트노드의 왼쪽 서브트리에 대해 탐색연산 수행
- 키 값x > 루트노드의 키 값 : 루트노드의 오른쪽 서브트리에 대해 탐색연산 수행



## 2 힙(heap)

> 완전 이진트리에 있는 노드 중에서 키 값이 가장 큰 노드나 가장 작은 노드를 찾기 위해서 만든 자료구조
>
> 최대 힙 : 키값이 가장 큰 노드를 찾기위한 완전이진트리
>
> 최소 힙 : 키값이 가장 작은 노드를 찾기위한 완전이진트리



- 힙에서는 루트 노드의 원소만을 삭제
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음

```python
def heap_push(item):
    global heap_count
    heap_count += 1
    heap[heap_count] = item

    cur = heap_count
    parent = cur // 2

    # 루트가 아니고, if 부모노드값 > 자식노드값 -> 스왑
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heap_pop():
    global heap_count
    item = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= heap_count:  # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            child = child + 1

    # 자식노드가 존재하고,  부모노드 > 자식노드 -> 스왑
    while child <= heap_count and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1
    return item

# 최소힙
heap_count = 0

temp = [7, 2, 5, 3, 4, 6]
N = len(temp)

heap = [0] * (N + 1)

for i in range(N):
    heap_push(temp[i])

for i in range(N):
    print(heap_pop())
```

