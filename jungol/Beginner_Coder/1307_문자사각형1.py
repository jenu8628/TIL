# A = 65, Z = 90 ord: 문자->숫자, chr: 숫자-> 문자
while True:
    n = int(input())
    idx = 65
    arr = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if idx > 90:
                idx = 65
            arr[j][i] = chr(idx)
            idx += 1
    for i in range(n):
        print(*arr[i])