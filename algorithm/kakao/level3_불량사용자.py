from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    user_p = list(permutations(user_id, len(banned_id)))
    banned_Set = []
    for users in user_p:
        # 하나의 튜플과 비교 시작
        if not check(users, banned_id):
            continue   # 다음 튜플 가져오기
        else:
            # users를 set으로 만들면 순서가 없기 때문에 순서가 달라도 같은지 알 수 있음!
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)
    return len(banned_Set)

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))
a = 'frodo'
b = ['crodo', 'frodoc']