# 내 풀이
num = ['A', 'B', 'C', 'D', 'E', 'F']
def binary(x):
    tmp = ''
    global ans
    while x > 0:
        tmp += str(x % 2)
        x = x//2
    while len(tmp) < 4:
        tmp += '0'
    for i in range(3, -1, -1):
        ans += tmp[i]
    return

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    ans = ''
    for i in range(len(arr[1])):
        if arr[1][i] in num:
            binary(num.index(arr[1][i]) + 10)
        else:
            binary(int(arr[1][i]))
    print('#{} {}'.format(tc, ans))

# 쌤풀이
# 1. 미리 정의 후 이용
b_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
          'D': 13, 'E': 14, 'F': 15}
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
          '1101', '1110', '1111']

for tc in range(1, int(input()) + 1):
    N, HEX = input().split()
    ans = ''
    # 16진수 한글자씩 읽어서 변경후 저장
    for i in HEX:
        ans += binary[b_dict[i]]
    print("#{} {}".format(tc, ans))
###############################################

# 2. int 내장 함수 이용
for tc in range(1, int(input()) + 1):
    N, HEX = input().split()
    HEX = int(HEX, 16)
    HEX = format(HEX, 'b')
    if len(HEX) != int(N) * 4:
        HEX = '0' * (int(N) * 4 - len(HEX)) + HEX
    print("#{} {}".format(tc, HEX))