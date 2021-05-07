x, y = map(int, input().split())
day = ["MON", "TUE", "WED","THU", "FRI", "SAT", "SUN"]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

ans = y-1
for i in range(x):
    ans += month[i]
print(day[ans%7])