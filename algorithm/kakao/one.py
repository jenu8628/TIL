def solution(id_list, report, k):
    user = {}
    answer = []
    ban = {}
    for i in id_list:
        user[i] = user.get(i, [])
        ban[i] = ban.get(i, 0)
    aleady = set()
    for r in report:
        user_id, ban_id = r.split(" ")
        if ban_id not in user[user_id]:
            ban[ban_id] += 1
            user[user_id].append(ban_id)
    for key, val in user.items():
        cnt = 0
        for i in val:
            if ban[i] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))