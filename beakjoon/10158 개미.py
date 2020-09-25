def f(a,b):
    tmp = (a + t) // b
    idx = (a + t) % b
    if tmp % 2 == 0:
        return idx
    else:
        return b-idx

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
print(f(p, w), f(q,h))


# 내 풀이 시간초과
dr = [1, -1]
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
d = 0
c = 0
for i in range(t):
    if 0 < p < w and 0 < q < h:
        p = p + dr[d]
        q = q + dr[c]
    elif p == w or p == 0:
        d = (d + 1) % 2
        p = p + dr[d]
        q = q + dr[c]
    elif q == h or q == 0:
        c = (c + 1) % 2
        p = p + dr[d]
        q = q + dr[c]
    elif (p == 0 or p == w) and (q == 0 or q == h):
        d = (d + 1) % 2
        c = (c + 1) % 2
        p = p + dr[d]
        q = q + dr[c]
print(p, q)