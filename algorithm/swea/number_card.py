T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    number = input()
    number_list = []
    for i in number:
        number_list.append(int(i))
    result = []
    for i in range(0,N):
        cnt = 0
        for j in range(i+1,N):
            if number_list[j] == number_list[i]:
                cnt += 1
        result.extend([cnt])
        Freq = max(result)
        locate = result.index(Freq)
    if sum(result) == 0:
        print(f'#{test_case} {max(number_list)} {max(result) + 1}')
    else:
        print(f'#{test_case} {number_list[locate]} {max(result) + 1}')
        