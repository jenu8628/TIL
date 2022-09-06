import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = {}
for i in range(1, N+1):
    a = sys.stdin.readline().rstrip()
    arr[a] = i
    arr[i] = a
for _ in range(M):
    quest = sys.stdin.readline().rstrip()
    if quest.isdigit():
        print(arr[int(quest)])
    else:
        print(arr[quest])