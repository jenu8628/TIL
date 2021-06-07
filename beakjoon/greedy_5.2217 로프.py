import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    x = int(sys.stdin.readline())
    arr.append(x)
arr.sort()
max_num = 0
for i in arr:
    max_num = max(max_num, i*N)
    N -= 1
print(max_num)
