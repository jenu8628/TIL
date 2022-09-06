import string
import math

def solution(n, k):
    answer = 0
    number = convert(n, k)
    check = ""
    for i in range(len(number)):
        if number[i] != '0':
            check += number[i]
        if (number[i] == '0' or i == len(number) - 1) and check:
            x = int(check)
            check = ""
            if x != 1:
                cnt = True
                for j in range(2, int(math.sqrt(x))+1):
                    if x % j == 0:
                        cnt = False
                        break
                if cnt:
                    answer += 1
    return answer

arr = string.digits+string.ascii_lowercase
def convert(n, k):
    q, r = divmod(n, k)
    if q == 0:
        return arr[r]
    else:
        return convert(q, k) + arr[r]

# n, k = 437674, 3
n, k = 110011, 10
print(solution(n, k))