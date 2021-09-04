arr = ["Enter", "Leave", "Change"]

def solution(record):
    answer = []
    # 나가고 들어온거 아이디 같이 넣기
    lis = []
    # id nickname 같이 넣기
    idName = {}
    for i in record:
        temp = list(map(str, i.split(" ")))
        lis.append([temp[0], temp[1]])
        if temp[0] != arr[1]:
            idName[temp[1]] = temp[2]
    for i in lis:
        if i[0] == arr[0]:
            answer.append("{}님이 들어왔습니다.".format(idName[i[1]]))
        elif i[0] == arr[1]:
            answer.append("{}님이 나갔습니다.".format(idName[i[1]]))
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

a = 1
b = [[1,3], [1,4], [1,5]]

if a in b:
    print('dd')


