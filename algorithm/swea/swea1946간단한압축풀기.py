T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    print('#{}'.format(tc))
    for i in range(N):
        s, total = map(str, input().split())

        for j in range(int(total)):
            print(s, end = '')
            cnt += 1
            if cnt % 10 == 0:
                print()
    print()