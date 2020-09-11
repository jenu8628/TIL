cal = ['-', '/', '+', '*']

def inorder(v):
    if len(arr[v]) == 3:
        inorder(arr[v][1])

    if len(arr[v]) == 3:
        inorder(arr[v][2])

    if arr[v][0] in cal:
        b = stack.pop()
        a = stack.pop()

        if arr[v][0] == '+':
            stack.append(a + b)
        elif arr[v][0] == '-':
            stack.append(a - b)
        elif arr[v][0] == '*':
            stack.append(a * b)
        elif arr[v][0] == '/':
            stack.append(a / b)
    else:
        stack.append(arr[v][0])

def sort_list(idx):
    if idx == 0:
        return
    for i in range(0, idx-1):
        stack[i], stack[i+1] = stack[i+1], stack[i]
    idx -= 1
    sort_list(idx)


for tc in range(1,11):
    # N : 정점수
    N = int(input())
    arr = [[] for _ in range(N+1)]
    stack = []
    for i in range(N):
        lis = input().split()
        # arr[int(lis[0])].extend(lis[1:])
        if len(lis) == 4:
            arr[int(lis[0])].append(lis[1])
            arr[int(lis[0])].extend((int(lis[2]), int(lis[3])))
        if len(lis) == 2:
            arr[int(lis[0])].append(int(lis[1]))
    inorder(1)
    print("#{} {}".format(tc, round(*stack)))