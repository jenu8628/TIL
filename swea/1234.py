def combination(idx, sidx):
    if sidx == R:
        tmp = sel[:]
        total.append(tmp)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i+1, sidx+1)

cnt = [0]*30
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
answer = []
dic = {}
arr = [[]*len(orders)]
for i in orders:
    for j in i:
        cnt[(ord(j)) - 65] += 1
        dic[j] = cnt[(ord(j)) - 65]

for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    arr.append(chr(i+65))

for i, j in dic.items():
    if j >= 2:
        arr.append()

N = len(arr)
total = []
for i in course:
    R = i
    sel = [0] * R
    combination(0, 0)
combination(0, 0)
count = 0
