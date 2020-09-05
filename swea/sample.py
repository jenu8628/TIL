import math
a = [0, 0]
b = [3**(1/2), 1]

def sin(a, b):
    # 빗변
    hypo = (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)**(1/2)
    height = abs(b[1]-a[1])
    return height / hypo

def cos(a, b):
    # 빗변
    hypo = (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)**(1/2)
    width = abs(b[0]-a[0])
    return width / hypo

def tan(a, b):
    width = abs(b[0] - a[0])
    height = abs(b[1] - a[1])
    return height / width

def degree(x):
    # 사인 역함수
    y = math.asin(x)
    # 라디안 -> 각도
    z = math.degrees(y)
    return z

print(round(degree(sin(a,b)), 5))