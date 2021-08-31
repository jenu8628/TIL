# 내 풀이
T = int(input())
for tc in range(1,T+1):
    arr0 = input().split()
    arr1 = list(map(str, input().split()))
    gns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(arr1)):
        for j in range(10):
            if arr1[i] == gns[j]:
                arr1[i] = int(j)
    arr1.sort()
    for k in range(len(arr1)):
        for n in range(10):
            if arr1[k] == n:
                arr1[k] = gns[n]
    print(arr0[0])
    for i in range(len(arr1)):
        print(arr1[i], end=" ")



# 방법 2 (쌤풀이)
num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

T = int(input())
for tc in range(1,T+1):
    a,b = input().split() # tc와 range받기
    arr = list(input().split()) # 문제 받기
    cnt = [0]*10
    # 딕셔너리로 푸는 방법!
    for key in arr:
        cnt[num_dict[key]] += 1
    print("#{}".format(tc))
    for i in range(10):
        print(num_list[i] * cnt[i], end="")
    print()

# 방법 3 (봉현이 풀이)
t = int(input())
keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
dic = {}
for tc in range(t):
    put1 = []
    put1 = input().split()
    num = put1[0]

    lists = input().split()
    for key in keys:
        count = 0
        for li in lists:
            if key == li:
                count +=1
        dic[key] = count
    print(num)
    for k, v in dic.items():
        for i in range(v):
            print(f'{k}', end=' ')