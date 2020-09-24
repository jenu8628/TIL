arr = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(5):
            if arr[i][j] in num[k]:
                arr[i][j] = 0
                