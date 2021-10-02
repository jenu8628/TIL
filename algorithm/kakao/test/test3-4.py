from testFunction import testFunc
from collections import deque

url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'

auth_key = '3449cd08-c1a2-4046-a9ff-5c238c2bc1d6'

x = 0
test = testFunc(auth_key, url)
lose = [277, 855, 845, 566, 154, 136, 303, 798, 747, 89, 261, 318, 291, 579, 400, 504, 776, 129, 755, 6, 80, 341, 509, 580, 681, 606, 41, 348, 538, 627, 292, 774, 415, 635, 860, 189, 869, 888, 145, 201, 330, 369, 388, 631, 58, 78, 101, 121, 178, 213, 244, 262, 285, 406, 407, 446, 590, 618, 636, 647, 700, 705, 712]
while True:
    # 클래스 불러오기
    test = testFunc(auth_key, url)

    # id : 매칭 기다리고 있는 유저 id, from :  매칭 대기를 시작한 시각(턴)
    wating_line = test.watingLine()['waiting_line']     # 매칭 대기열
    # id: 유저 고유 id, grade: 현재 등급
    users = test.userInfo()['user_info']    # 모든 유저들의 현재 등급

    # 2차원 리스트로 만들어서 인덱스로 접근하자.
    # 기다린 시간이 높은 사람을 찾을 때 zip을 이용해서 접근하기 용이함
    # 0: id, 1: 기다린 시간, 2: 등급
    wating = []
    for i in wating_line:
        wating.append([i['id'], i['from'], users[i['id'] - 1]['grade']])
    # 등급우선 정렬, 후에 기다린 시간 순 정렬
    wating.sort(key=lambda x: (-x[2], -x[1]))

    # wating = deque(wating)

    # 유저 매칭
    # 어떻게 매칭 시킬 것인가?
    # 유저 실력은 0 부터 시작
    # 초반엔 누가 잘하는지 모름.
    pair = []
    if len(wating) >= 2:
        i, j = 0, 1
        while i < len(wating) - 1:
            A = wating[i]
            B = wating[j]
            if (A[2] - B[2]) < 30:
                pair.append([A[0], B[0]])
            i = j + 1
            j = i + 1

    # print('wating', wating)
    # print('pair', pair)

    macth = test.match(pair)
    # win : 게임이긴 유저 id, lose: 게임진 유저 아이디, taken: 게임하는데 걸린 시간
    # 오래걸릴수록 비슷한 실력
    # 빨리끝날수록 차이큼!
    result = test.gameResult()['game_result']
    # print('result', result)
    if len(result) >= 1:
        gameresult = []
        for r in result:
            gameresult.append([r['win'], r['lose'], r['taken']])
        commands = []
        for game in gameresult:
            # game[0] : 이긴사람 id
            if game[2] <= 10:
                if game[0] in lose and game[1] not in lose:
                    win_grade = users[game[0] - 1]['grade'] + (40 - game[2])
                    lose_grade = users[game[1] - 1]['grade'] - (40 - game[2])
                elif game[0] not in lose and game[1] not in lose:
                    win_grade = users[game[0] - 1]['grade'] + (40 - game[2])
                    lose_grade = users[game[1] - 1]['grade'] - (40 - game[2])
                else:
                    win_grade = users[game[0] - 1]['grade'] - (40 - game[2])
                    lose_grade = users[game[1] - 1]['grade'] + (40 - game[2])
            else:
                win_grade = users[game[0] - 1]['grade'] + (40 - game[2])
                lose_grade = users[game[1] - 1]['grade'] - (40 - game[2])
            if lose_grade < 0:
                lose_grade = 0
            if win_grade < 0:
                win_grade = 0
            commands.append({'id': game[0], 'grade': win_grade})
            if lose_grade < 0:
                lose_grade = 0
            commands.append({'id': game[1], 'grade': lose_grade})
        # 유저 등급 변경
        # print(commands)
        grade = test.changeGrade(commands)
        # print('grade', grade)
    print(macth)
    if macth['status'] == 'finished':
        break
    if x == 0:
        commands = []
        for i in range(len(users)):
            commands.append({'id': i+1, 'grade': 5000})
        grade = test.changeGrade(commands)
        x += 1