# def solution(phone_book):
#     book = sorted(phone_book)
#     for i in range(len(book)-1):
#         if book[i] == book[i+1][:len(book[i])]:
#             return False
#     return True


def solution(phone_book):
    book = sorted(phone_book)
    for i in range(len(book)-1):
        if book[i+1].startswith(book[i]):
            return False
    return True