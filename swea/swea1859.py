# import sys
# from typing import List
#
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    max = number[-1]
    max_profit = 0
    for i in range(len(number)-2,-1,-1):
        if number[i]< max:
            max_profit += max - number[i]
        else:
            max = number[i]
    print(f'#{tc} {max_profit}')
