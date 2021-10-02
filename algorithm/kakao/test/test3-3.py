from testFunction import testFunc
from collections import deque

url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'

auth_key = '5ce48368-9468-4d80-b44f-a4b66d9498a2'

x = 0
test = testFunc(auth_key, url)
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
            if (A[2] - B[2]) < 20:
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
            if game[2] > 10:
                win_grade = users[game[0] - 1]['grade'] + (40 - game[2])
                lose_grade = users[game[1] - 1]['grade'] - (40 - game[2])
                commands.append({'id': game[0], 'grade': win_grade})
                if lose_grade < 0:
                    lose_grade = 0
                commands.append({'id': game[1], 'grade': lose_grade})
            else:
                win_grade = users[game[0] - 1]['grade'] - (40 - game[2])
                lose_grade = users[game[1] - 1]['grade'] + (40 - game[2])
                commands.append({'id': game[0], 'grade': win_grade})
                if win_grade < 0:
                    win_grade = 0
                commands.append({'id': game[1], 'grade': lose_grade})
        # 유저 등급 변경
        grade = test.changeGrade(commands)
    print(macth)
    if macth['status'] == 'finished':
        break
    if x == 0:
        commands = []
        for i in range(len(users)):
            commands.append({'id': i+1, 'grade': 5000})
        grade = test.changeGrade(commands)
        x += 1
