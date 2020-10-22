T = int(input())
for tc in range(1, T + 1):
    # 자석 회전 횟수
    K = int(input())
    # 톱니의 날의 자성정보
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 회전을 시작하는 톱니위치와, 회전방향을 받기
    # ed == 1 : 시계방향, ed == 0 : 반시계방향
    for v in range(K):
        st, ed = map(int, input().split())
        # st를 인덱스로 접근하기 위해 -1해줌!
        n = st - 1
        # 톱니돌려야될 인덱스 담을 tmp
        tmp = [n]
        if n == 0:
            for i in range(1, 4):
                # 옆의 톱니와 다르다면 돌려야 되기 때문에 tmp에 추가
                if arr[n+i-1][2] != arr[n+i][6]:
                    tmp.append(n+i)
                if arr[n+i-1][2] == arr[n+i][6]:
                    break
        elif n == 3:
            for i in range(3):
                # 옆의 톱니와 다르다면 돌려야 되기 때문에 tmp에 추가
                if arr[n - i][6] != arr[n - i - 1][2]:
                    tmp.append(n - i - 1)
                if arr[n - i][6] == arr[n - i - 1][2]:
                    break
        elif n == 2:
            if arr[n+1][6] != arr[n][2]:
                tmp.append(n+1)
            if arr[n-1][2] != arr[n][6]:
                tmp.append(n-1)
                if arr[n-2][2] != arr[n-1][6]:
                    tmp.append(n-2)
        else:
            if arr[n-1][2] != arr[n][6]:
                tmp.append(n-1)
            if arr[n+1][6] != arr[n][2]:
                tmp.append(n+1)
                if arr[n+2][6] != arr[n+1][2]:
                    tmp.append(n+2)
        if ed == 1:
            for i in tmp:
                if (abs(n - i)) % 2 == 0:
                    x = arr[i].pop()
                    arr[i] = [x] + arr[i]
                else:
                    y = arr[i].pop(0)
                    arr[i] = arr[i] + [y]
        if ed == -1:
            for i in tmp:
                if (abs(n - i)) % 2 == 0:
                    x = arr[i].pop(0)
                    arr[i] = arr[i] + [x]
                else:
                    y = arr[i].pop()
                    arr[i] = [y] + arr[i]
    cnt = 0
    for j in range(4):
        if arr[j][0] == 1:
            cnt += 2 ** j
    print('#{} {}'.format(tc, cnt))