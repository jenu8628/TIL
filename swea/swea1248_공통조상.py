import sys
sys.stdin = open('input.txt', 'r')
# def order(x):
#     global cnt
#     if len(arr[x]) == 2:
#         order(arr[x][0])
#         order(arr[x][1])
#     elif len(arr[x]) == 1:
#         order(arr[x][0])
#     cnt += 1
#
# T = int(input())
# for tc in range(1, T+1):
#     # V: 트리의 정점의 총 수, E: 간선의 총 수, N,M: 공통조상을 찾는 두개의 정점번호
#     V, E, N, M = map(int, input().split())
#     arr = [[] for _ in range(V+1)]
#     lis = list(map(int, input().split()))
#     for i in range(E):
#         st, ed = lis[2*i], lis[2*i+1]
#         arr[st].append(ed)
#     i = len(arr)
#     lis_N = []
#     lis_M = []
#     while N != 1 or M != 1:
#         for i in range(len(arr)):
#             if N in arr[i]:
#                 N = i
#                 lis_N.append(N)
#             if M in arr[i]:
#                 M = i
#                 lis_M.append(M)
#     lis_N = lis_N[::-1]
#     lis_M = lis_M[::-1]
#     same = 0
#     cnt = 0
#     for i in range(min(len(lis_N), len(lis_M))):
#         if lis_N[i] == lis_M[i]:
#             same = lis_N[i]
#     order(same)
#     print("#{} {} {}".format(tc, same, cnt))

# 쌤풀이
# 부모찾기 함수
def search_p(v):
    queue = [v]
    while queue:
        curr = queue.pop(0)
        # 부모가 없을때까지 리턴! 즉 루트까지!
        if tree[curr][2] == 0:
            return
        # 부모를 찾아 떠나는 중 이미 부모에 부모요소가 있으면 return
        # 이 가정문은 공통 조상중에 가장 가까운 조상을 찾는 것임!
        if tree[curr][2] in parents:
            return tree[curr][2]
        # 부모요소 계속 넣어줌
        parents.append(tree[curr][2])
        # 부모요소 넣고 빼기 위해서!
        queue.append(tree[curr][2])

# 정점 v를 루트로 하는 서브트리의 크기 만드는 함수
def size_tree(v):
    queue = [v]
    count = 0
    while queue:
        # 자식요로 가기 위해
        curr = queue.pop(0)
        # 서브트리의 크기 확인하는 count
        count += 1
        # 왼쪽자식 있으면 왼쪽자식 추가
        if tree[curr][0]:
            queue.append(tree[curr][0])
        # 오른쪽자식 있으면 오른쪽 자식 추가
        if tree[curr][1]:
            queue.append(tree[curr][1])
    # 서브트리 크기 리턴
    return count

T = int(input())

for tc in range(1,T+1):
    V, E, A, B = map(int,input().split())
    edge = list(map(int, input().split()))
    # tree의 0번인덱스에 왼쪽 자식, 1번인덱스에 오른쪽 자식, 트리의 마지막에 부모요소 넣기
    tree = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        p = edge[i*2]
        c = edge[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    print(tree)
    parents=[]

    search_p(A)
    common = search_p(B)
    ans = size_tree(common)

    print("#{} {} {}".format(tc, common, ans))
