for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    st = 1
    bt = arr[st]
    cnt = 0
    while st + bt < N:
        cnt += 1
        max_bt = 0
        for i in range(st+1, st+bt+1):
            if max_bt < arr[i]+i:
                max_bt = arr[i]+i
                x = i
        st = x
        bt = arr[x]
    print('#{} {}'.format(tc, cnt))

# 쌤풀이
def check(my, cnt):
    global ans
    #가지치기
    if cnt > ans:
        return

    if my >= bus_stop[0]:
        ans = min(ans, cnt)
        return

    for i in range(my + bus_stop[my], my, -1):
        check(i, cnt+1)


for tc in range(1, int(input())+1):
    bus_stop = list(map(int, input().split()))
    ans = 987654321

    check(1, -1)

    print("#{} {}".format(tc, ans))