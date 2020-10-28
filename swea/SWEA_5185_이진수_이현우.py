num = ['A', 'B', 'C', 'D', 'E', 'F']

def binary(x):
    tmp = []
    while x > 0:
        tmp.append(x % 2)
        x = x//2
    while len(tmp) < 4:
        tmp.append(0)
    ans.extend(tmp[::-1])
    return

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    ans = []
    for i in range(len(arr[1])):
        if arr[1][i] in num:
            binary(num.index(arr[1][i]) + 10)
        else:
            binary(int(arr[1][i]))
    print('#{} {}'.format(tc, ''.join(list(map(str, ans)))))