T = int(input())
for tc in range(1,T+1):
    string = input()
    str_list = []
    str_reverse = []
    for i in range(len(string)//2):
        str_list.append(string[i])
        str_reverse.append(string[-1-i])
    if str_list == str_reverse:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
