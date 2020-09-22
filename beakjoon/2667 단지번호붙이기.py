dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r,c):
    global count
    count += 1
    arr[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1':
            DFS(nr, nc)

N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        count = 0
        if arr[i][j] == '1':
            DFS(i, j)
            cnt += 1
            result.append(count)

print(cnt)
for i in sorted(result):
    print(i)