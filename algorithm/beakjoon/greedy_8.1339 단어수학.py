import sys
# N = int(sys.stdin.readline())
# arr = ["" for _ in range(8)]
# result = {}
# ans = 0
# for i in range(N):
#     word = input()
#     for j in range(len(word)):
#         arr[7-j] += word[len(word)-1-i]
# print(arr)
# x = 9
# for i in range(len(arr)):
#     if arr[i]:
#         for alpha in arr[i]:
#             if alpha not in result:
#                 result[alpha] = x
#                 x -= 1
#                 ans += (10**(7-i)*result[alpha])
# print(ans)

N = int(sys.stdin.readline())
# 단어 입력받을 리스트 만들기
words = []
# 단어 입력받기
for i in range(N):
    words.append(input())

# 딕셔너리 초기화하기
dict = {}
# 딕셔너리에 알파벳당 숫자 집어넣기
for word in words:
    k = len(word) - 1
    for s in word:
        if s in dict:
            dict[s] += 10 ** k
        else:
            dict[s] = 10 ** k
        k -= 1
# 숫자리스트 초기화
nums = []

# 사전의 값들만으로 이루어진 리스트 초기화
for value in dict.values():
    nums.append(value)

# 숫자 큰순으로 정렬
nums.sort(reverse=True)

# 출력할 값과 곱해야 하는 수 초기화
ans, t = 0, 9

# 값 구하기
for i in range(len(nums)):
    ans += nums[i] * t
    t -= 1

print(ans)