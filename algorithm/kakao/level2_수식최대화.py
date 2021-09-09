# 기호
te = ["*", "-", "+"]

# 순열
def per(idx, N):
    if idx == N:
        arr.append(sign[:])
        return
    for i in range(idx, N):
        sign[idx], sign[i] = sign[i], sign[idx]
        per(idx+1, N)
        sign[idx], sign[i] = sign[i], sign[idx]

    return

def cal(num, arr):
    # arr : 계산 순서
    # num 계산할 리스트
    stack = []
    for i in range(len(arr)):
        if i == 0:
            lis = num[:]
        else:
            lis = stack[:]
            stack = []
        while lis:
            x = lis.pop(0)
            if x == arr[i]:
                a = stack.pop()
                b = lis.pop(0)
                if x == "*":
                    stack.append(a * b)
                elif x == "-":
                    stack.append(a - b)
                else:
                    stack.append(a + b)
            else:
                stack.append(x)
    return abs(stack[0])


def solution(expression):
    global arr
    global sign
    answer = 0
    sign = []
    num = []
    mid = 0
    # 리스트화 및 몇개의 연산기호가 있는지 확인 후 담기
    for i in range(len(expression)):
        if i < mid:
            continue
        for j in range(i+1, len(expression)):
            if expression[j] in te:
                if expression[j] not in sign:
                    sign.append(expression[j])
                num.append(int(expression[i:j]))
                num.append(expression[j])
                mid = j+1
                if mid == len(expression) - 1:
                    num.append(int(expression[mid:]))
                break
            if j == len(expression) - 1:
                num.append(int(expression[i:]))

    arr = []
    per(0, len(sign))
    for i in range(len(arr)):
        if cal(num, arr[i]) > answer:
            answer = cal(num, arr[i])
    return answer

expression = "50*6-3*2"
print(solution(expression))
# 음수라면 해당 숫자의 절댓값으로 변환하여 제출!

