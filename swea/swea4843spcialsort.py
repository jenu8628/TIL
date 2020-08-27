T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_list = arr[:]
    odd = [1,3,5,7,9]
    even = [0,2,4,6,8]
    for i in range(0,5):
        arr[even[i]] = arr_list[-(i+1)]
        arr[odd[i]] = arr_list[i]
    result = ''
    for j in arr[0:10]:
        result += ' ' + str(j)
    print(f'#{tc}{result}')