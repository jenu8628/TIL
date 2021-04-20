while True:
    ans = [0]*10
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    ans_num = num1 * num2 * num3
    for i in str(ans_num):
        ans[int(i)] += 1
    for i in ans:
        print(i)
