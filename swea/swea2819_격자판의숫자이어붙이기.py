import sys
sys.stdin = open('sample_input(1).txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def f(x, y, number):
    if len(number) == 7:
        total.add(number)
        return

    for k in range(4):
        nr = x + dr[k]
        nc = y + dc[k]
        if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
            continue
        f(nr, nc, number + arr[nr][nc])

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    total = set()
    for i in range(4):
        for j in range(4):
            number = arr[i][j]
            f(i, j, number)
    print('#{} {}'.format(tc, len(total)))