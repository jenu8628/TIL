N = input()
ans = 0
num = N.split('-')

if '+' in num[0]:
    for j in num[0].split('+'):
        ans += int(j)
else:
    ans += int(num[0])

for i in range(1, len(num)):
    if '+' in num[i]:
        x = num[i].split('+')
        for j in x:
            ans -= int(j)
    else:
        ans -= int(num[i])
print(ans)