def solution(places):
    answer = []

    for place in places:
        flag = False
        for r in range(len(place)):
            for c in range(len(place[r])):
                if place[r][c] == "P":
                    result = check(r, c, place)
                    if not result:
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        if not flag:
            answer.append(1)
    return answer

def check(r, c, place):
    dist = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dr, dc in dist:
        nr, nc = r + dr, c + dc
        if valid(nr, nc) and place[nr][nc] == "P":
            return False
    dist = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    for dr, dc in dist:
        nr, nc = r + dr, c + dc
        if valid(nr, nc) and place[nr][nc] == "P" and (place[nr][c] != 'X' or place[r][nc] != 'X'):
            return False
    dist = [[2, 0], [-2, 0], [0, 2], [0, -2]]
    for dr, dc in dist:
        nr, nc = r + dr, c + dc
        if valid(nr, nc) and place[nr][nc] == "P" and place[r + dr//2][c + dc//2] != "X":
            return False
    return True

def valid(r,c):
    return -1 < r < 5 and -1 < c < 5



from collections import deque
import numpy as np

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_correct(place):
    place = np.array([list(x) for x in place])
    q = deque([])
    for r, c in zip(*np.where(place == 'P')):
        q.append([r, c, r, c, 0])
    while q:
        cur_r, cur_c, start_r, start_c, dist = q.popleft()
        if dist < 2:
            for nr, nc in moves:
                new_r, new_c = cur_r + nr, cur_c + nc
                if 0 <= new_r < 5 and 0 <= new_c < 5 and (start_r, start_c) != (new_r, new_c):
                    if place[new_r][new_c] == 'P':
                        return 0
                    elif place[new_r][new_c] == 'O':
                        q.append((new_r, new_c, start_r, start_c, dist+1))
    return 1


def solution2(places):
    answer = []
    # P : 응시자, O: 빈 테이블, X: 파티션
    for place in places:
        answer.append(is_correct(place))
    return answer
if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
    print(solution2(places))
    # P : 응시자가 앉아있는 자리
    # O : 빈테이블
    # X : 파티션
    # (r1,c1), (r2, c2) 일 때 맨해튼거리 : |r1-r2| + |c1-c2|