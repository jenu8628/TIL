T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

# slice()메소드를 활용하여 리스트를  Y M D로 나눈다.
# M은 1~12
# 1,3,5,7,8,10,12월은 31일까지
# 2월은 28일까지
# 4,6,9,11은 30일까지

for test_case in range(1, T + 1):
    number = input()
    numbers = []
    for i in number:
        numbers.append(int(i)) 
    years = numbers[0:4]
    new_year = ''
    for year in years:
        new_year.add(year)
    month = numbers[4:6]
    new_month = ''
    for j in month:
        new_month.add(j)
    days = numbers[6:]
    new_day = ''
    for day in days:
        new_day.add(day)
    if new_month > 12:
        return False
    else:
        if new_month == 2:
            if day > 28:
                return False
        elif new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11:
            day
    