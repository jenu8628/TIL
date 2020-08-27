import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    N = input()
    number = [list(map(int,input().split()))for i in range(100)]
    diag_sum = 0
    diag_sum_r = 0
    width = []
    height = []


    for i in range(0,100):
        diag_sum += number[i][i]
        diag_sum_r += number[i][-(i+1)]
        width_sum = 0
        height_sum = 0
        for j in range(0,100):
            width_sum += number[i][j]
            height_sum += number[j][i]
        width.append(width_sum)
        height.append(height_sum)
    max_width = max(width)
    max_height = max(height)

    max_list = [diag_sum, diag_sum_r, max_width, max_height]
    print(f'#{tc} {max(max_list)}')


