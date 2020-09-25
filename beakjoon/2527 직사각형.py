for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # 공통부분이 없는 경우
    if p1 < x2 or x1 > p2 or q1 < y2 or y1 > q2:
        print('d')
    elif (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y1) or (p1 == x2 and q1 == y2):
        print('c')
    elif y1 == q2 or q1 == y2 or p1 == x2 or x1 == p2:
        print('b')
    else:
        print('a')
