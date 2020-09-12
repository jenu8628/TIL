i = "java backend junior pizza 150"
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
answer = []
info_lis = []
query_lis = []
for i in info:
    result = i.split()
    info_lis.append(result)

for i in query:
    result = i.split()
    total = []
    for j in result:
        if j != 'and':
            total.append(j)
            pass
    query_lis.append(total)

for i in query_lis:
    cnt_max = 0
    cnt = [0] * len(info_lis)
    cnt_answer = 0
    for j in range(len(i)-1):
        if i[j] == '-':
            continue
        else:
            cnt_max += 1
            for k in range(len(info_lis)):
                if i[j] in info_lis[k]:
                    cnt[k] += 1

    for m in range(len(cnt)):
        if int(info_lis[m][-1]) >= int(i[-1]) and cnt[m] == cnt_max:
            cnt_answer += 1
    answer.append(cnt_answer)


