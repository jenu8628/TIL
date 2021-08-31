# numbers = input()

# add_number = 0
# for number in numbers:
#     add_number += int(number)
# print(add_number)

# 숫자를 받아서 정수로 전환
# 1234
# 1234 % 10 => 4를 받고
# number = 1234 // 10 으로 다시 정의합니다.
# 위의 과정을 반복하다가 number ==  0 이 되면 종료합니다.

number = int(input())
add_number = 0
while True:
    add_number += number % 10
    number = number // 10
    if number == 0:
        break
print(add_number)
    
    
