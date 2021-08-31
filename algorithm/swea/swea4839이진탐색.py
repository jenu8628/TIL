def half(s, e, key):
    cnt = 0
    while 1 <= e:
        cnt += 1
        mid = int((s+e) / 2)
        if mid == key:
            break
        elif mid > key:
            s = mid + 1
        else:
            e = mid - 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    n_list = range(1, P+1)
    A = half(1, P, Pa)
    B = half(1, P, Pb)
    if A == B:
        print(f'#{tc} 0')
    elif A < B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')