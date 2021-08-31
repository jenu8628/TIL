while True:
    # # 1. 문자열로 구하는 방법
    # num1 = input()
    # num2 = input()
    # ans1 = int(num2[2]) * int(num1)
    # ans2 = int(num2[1]) * int(num1)
    # ans3 = int(num2[0]) * int(num1)
    # # ans4 = int(num1) * int(num2)

    # 2. 숫자로 구하는 방법
    num1 = int(input())
    num2 = int(input())
    ans1 = (num2 % 10) * num1
    ans2 = (num2//10) % 10 * num1
    ans3 = (num2 // 100) * num1
    # ans4 = num1 * num2

    ans4 = ans1 + (ans2 * 10) + (ans3 * 100)
    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)