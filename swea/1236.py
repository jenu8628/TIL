
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
def combination(idx, sidx):
    if sidx == R:
        tmp = sel[:]
        total.append(sorted(tmp))
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i+1, sidx+1)

cnt = [0]*30
answer = []
dic = {}
arr = []
for i in orders:
    for j in i:
        cnt[(ord(j)) - 65] += 1
        dic[j] = cnt[(ord(j)) - 65]

for i, j in dic.items():
    if j >= 2:
        arr.append(i)

total = []
N = len(arr)
for j in course:
    R = j
    sel = [0] * R
    combination(0, 0)

toto = []
for i in range(len(total)):
    result = ''
    cnt = 0
    for j in range(len(total[i])):
        result += total[i][j]
    toto.append(result)

dic_menu = {}
for i in range(len(toto)):
    dic_menu[toto[i]] = 0
for i in range(len(toto)):
    for k in range(len(toto[i])):
        for j in range(len(orders)):
            if toto[i][k] in orders[j]:
                dic_menu[toto[i]] += 1
print(dic_menu)

for i in range(len(course)):
    res = []
    for key, value in dic.items():
        if len(key) == course[i]:
            res.append(value)
        print(res)
    for key, value in dic.items():
        if len(key) == course[i]:
            if value == max(res):
                answer.append(key)
sorted(answer)
print(answer)

