T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    total = []
    for i in range(n):
        cnt = 0
        result = 0
        for j in range(n):
            if maze[i][j] == 1 or n- 1 == j:

            elif maze[i][j] ==0:


    print('#{} {}'.format(tc, total))