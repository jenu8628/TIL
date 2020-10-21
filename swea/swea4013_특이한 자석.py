T = int(input())
for tc in range(1, T + 1):
    # 자석 회전 횟수
    K = int(input())
    # 톱니의 날의 자성정보
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 회전을 시작하는 톱니위치와, 회전방향을 받기
    # ed == 1 : 시계방향, ed == 0 : 반시계방향
    for i in range(K):
        st, ed = map(int, input().split())
        # st를 인덱스로 접근하기 위해 -1해줌!
        n = st - 1
        tmp = []
        for i in range(4):
            mod_x = n+i % 4
            q = n+i // 4
            if arr[mod_x][2] != arr[mod_x+1][6]:
                if n+i == 4:
                    pass
                tmp.append(mod_x + 1)
