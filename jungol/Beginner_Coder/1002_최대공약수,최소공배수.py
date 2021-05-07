def commonnumber(a, b):
    common = 0
    for i in range(1, a+1):
        if a % i == 0:
            if b % i == 0:
                if i > common:
                    common = i
    return common
while True:
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    common = commonnumber(arr[0], arr[1])
    meancommon = (arr[0] * arr[1]) // common
    for i in range(2, len(arr)):
        common = commonnumber(common, arr[i])
        meancommon = (meancommon*arr[i]) // commonnumber(meancommon, arr[i])
    print(common, end=" ")
    print(meancommon)