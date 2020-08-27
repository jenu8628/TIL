import sys
sys.stdin = open("input.txt","r")
#
# def binary(num):
#     bin_list = ''
#     if num // 2 == 0:
#         return str(num % 2) + bin_list
#     bin_list = str(num % 2) + bin_list
#     return binary(num//2) + bin_list
def binary(num):
    bin_list = ''
    if num // 2 == 0:
        return str(num)
    return binary(num//2) + str(num%2)

T = int(input())
for tc in range(1,T+1):
    N = input()
    Base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    result = ''

    for i in N:
        if len(binary(Base64.find(i))) != 6:

            result += ('0' * (6- (len(binary(Base64.find(i)))))) + binary(Base64.find(i))
    print(result)
    total = ''
    for j in range(0,len(result),8):
        tmp = result[j:j+8]
        total += chr(int(tmp,2))
    print(total)
