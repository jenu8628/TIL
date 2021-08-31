while True:
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    ans1 = 0
    ans2 = 0
    for i in arr:
        if m % i == 0:
            ans1 += i
        if i % m == 0:
            ans2 += i
    print(ans1)
    print(ans2)