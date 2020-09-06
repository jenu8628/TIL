import math
def locx(loc, holl):
    # loc : 목적구, holl : 구멍
    if loc[0] - holl[0] > 0:
        return loc[0] + ((5.72*loc[0])/((loc[0]**2 + loc[1]**2)**(1/2)))
    elif loc[0] - holl[0] < 0:
        return loc[0] - ((5.72*loc[0])/((loc[0]**2 + loc[1]**2)**(1/2)))

def locy(loc, holl):
    if loc[1] - holl[1] > 0:
        return loc[1] + (5.72*loc[1])/((loc[0]**2 + loc[1]**2)**(1/2))
    elif loc[1] - holl[1] < 0:
        return loc[1] - (5.72*loc[1])/((loc[0]**2 + loc[1]**2)**(1/2))

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


c = (127, 0)
a = (6*(3 ** (1/2)), 6)
b = (locx(a, c), locy(a, c))
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