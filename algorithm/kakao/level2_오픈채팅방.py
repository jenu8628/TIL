def solution1(record):
    answer = []
    # 나가고 들어온거 아이디 같이 넣기
    lis = []
    # id nickname 같이 넣기
    idName = {}
    for i in record:
        temp = list(map(str, i.split(" ")))
        lis.append([temp[0], temp[1]])
        if temp[0] != "Leave":
            idName[temp[1]] = temp[2]
    for i in lis:
        if i[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(idName[i[1]]))
        elif i[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(idName[i[1]]))
    return answer

def solution2(record):
    answer = []
    id_name_dict = {}
    result_list = []
    for sentence in record:
        splited = sentence.split(' ')
        if len(splited) == 3:
            status, user_id, user_name = splited
            id_name_dict[user_id] = user_name
            if status == 'Enter':
                result_list.append([user_id, '님이 들어왔습니다.'])
        else:
            status, user_id = splited
            result_list.append([user_id, '님이 나갔습니다.'])
    for result in result_list:
        user_id, status = result
        answer.append(id_name_dict[user_id] + status)

    return answer


if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    # print(solution1(record))
    print(solution2(record))



a = 1
b = [[1,3], [1,4], [1,5]]

if a in b:
    print('dd')


