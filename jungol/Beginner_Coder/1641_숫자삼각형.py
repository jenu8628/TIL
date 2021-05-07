while True:
    n, m = map(int, input().split())
    if 0 < n < 100 and n % 2 == 1 and 1 <= m <= 3:
        if m == 1:
            ans = []
            cnt = 1
            for i in range(n):
                tmp = []
                if i % 2 == 0:
                    for j in range(cnt, cnt+i+1):
                        tmp.append(j)
                        cnt += 1
                    ans.append(tmp)
                else:
                    for j in range(cnt+i+1 - 1, cnt-1, -1):
                        tmp.append(j)
                        cnt += 1
                    ans.append(tmp)
            for i in range(len(ans)):
                for j in ans[i]:
                    print(j, end=" ")
                print()
        elif m == 2:
            for i in range(n):
                print(" " * (((n * 2) - 1) - (((n - i) * 2) - 1)), end="")
                for j in range(((n-i)*2)-1):
                    print(i, end=" ")
                print()
        else:
            for i in range(1, n+1):
                if i <= (n+1)//2:
                    for j in range(1, i+1):
                        print(j, end=" ")
                    print()
                else:
                    for j in range(1, (n-i)+2):
                        print(j, end=" ")
                    print()
    else:
        print("INPUT ERROR!")