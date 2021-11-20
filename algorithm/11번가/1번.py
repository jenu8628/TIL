def solution(phone_numbers, phone_owners, number):
    # for i in range(len(phone_numbers)):
    #     if number == phone_numbers[i]:
    #         return phone_owners[i]
    if number in phone_numbers:
        x = phone_numbers.index(number)
        return phone_owners[x]
    return number
