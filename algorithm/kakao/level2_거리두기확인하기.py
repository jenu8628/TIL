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

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
# P : 응시자가 앉아있는 자리
# O : 빈테이블
# X : 파티션
# (r1,c1), (r2, c2) 일 때 맨해튼거리 : |r1-r2| + |c1-c2|