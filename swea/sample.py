import math
# 목적구를 치기위한 위치를 구하는 함수
def locx(loc, hole):
    # loc : 목적구, hole : 구멍
    if loc[0] - hole[0] > 0:
        return loc[0] + abs(((5.72*(loc[0]-hole[0]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
    elif loc[0] - hole[0] < 0:
        return loc[0] - abs(((5.72*(loc[0]-hole[0]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))

def locy(loc, hole):
    if loc[1] - hole[1] > 0:
        return loc[1] + abs(((5.72*(loc[1]-hole[1]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
    elif loc[1] - hole[1] < 0:
        return loc[1] - abs(((5.72*(loc[1]-hole[1]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))

# 좌표로 각도구하는 법
def degree(white, obj):
    # white : 흰공, obj : 목적구를 치기위한 위치
    # 사인함수
    # 빗변
    hypo = ((obj[0] - white[0]) ** 2 + (obj[1] - white[1]) ** 2) ** (1 / 2)
    # 높이
    height = abs(obj[1] - white[1])

    # 오른쪽 위
    if obj[0] - white[0] > 0 and obj[1] - white[1] < 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 90 - math.degrees(y)
    # 왼쪽 위
    elif obj[0] - white[0] < 0 and obj[1] - white[1] < 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 270 + math.degrees(y)
    # 왼쪽 아래
    elif obj[0] - white[0] < 0 and obj[1] - white[1] > 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 270 - math.degrees(y)
    # 오른쪽 아래
    elif obj[0] - white[0] > 0 and obj[1] - white[1] > 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 90 + math.degrees(y)
    elif obj[0] - white[0] == 0 and obj[1] - white[1] < 0:
        return 0
    elif obj[0] - white[0] > 0 and obj[1] - white[1] == 0:
        return 90
    elif obj[0] - white[0] == 0 and obj[1] - white[1] > 0:
        return 180
    elif obj[0] - white[0] < 0 and obj[1] - white[1] == 0:
        return 270


# 쿠션칠때 어디 쳐야할지 고르기
def top_middle(white, obj):
    z = (obj[0] - white[0]) * ((white[1]) / (white[1]+obj[1]))
    return (white[0]+abs(z), 0)

def bottom_middle(white, obj):
    z = (obj[0] - white[0]) * ((white[1]) / (white[1]+obj[1]))
    return (white[0]+abs(z), 127)

c = (258, 127) # hole
a = (100*(3 ** (1/2)), 100) # 목적구
b = (locx(a, c), locy(a, c)) # 흰공이 쳐서 와야될 위치
print(a)
print(b)

# def cos(a, b):
#     # 빗변
#     hypo = (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)**(1/2)
#     width = abs(b[0]-a[0])
#     return width / hypo
#
# def tan(a, b):
#     width = abs(b[0] - a[0])
#     height = abs(b[1] - a[1])
#     return height / width

def play(conn, gameData):
    angle = 10
    power = 10
    print(gameData.balls)
    if gameData.balls[1] == [125, 120]:
        angle = 50
        power = 50

    elif gameData.balls[1] == [250, 10]:
        angle = 105
        power = 100
    elif gameData.balls[2] == [15, 10]:
        angle = 267
        power = 100

    elif gameData.balls[2] == [240, 124]:
        angle = 86.5
        power = 75

    elif gameData.balls[3] == [250, 10]:
        angle = 182.7
        power = 70

    elif gameData.balls[3] == [254, 6]:
        angle = 90
        power = 30
    elif gameData.balls[1] == [195, 65]:
        angle = 89
        power = 180
    elif gameData.balls[1] == [254, 58]:
        angle = 180
        power = 80


