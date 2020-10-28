import copy
# def spin(r, c, s, arr):
#     tmp = copy.deepcopy(arr)
#     for i in range(0, 2*s+1): # 0, 4
#         for j in range(0, 2*s+1): # 1, 5
#             tmp[i][j] = arr[-(j+1)][i]
#     return tmp
def spin(r, c, s, arr):
    tmp = copy.deepcopy(arr)
    for i in range(r-s, r+s+1): # 0, 4
        for j in range(c-s, c+s+1): # 1, 5
            tmp[i][j] = arr[-(j-H)][i]
    return tmp

def customcopy(r, c, s, arr):
    tmp = [[] for _ in range((2*s+1))]
    k = -1
    for i in range(r - s, r + s + 1):  # 0, 4
        k += 1
        for j in range(c - s, c + s + 1):  # 1, 5
            tmp[k].append(arr[i][j])
    return tmp

def answer(arr, tmp):


N, M, K = map(int, input().split())
H = abs(N-M)
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(K):
    r, c, s = map(int, input().split())
    r, c = r-1, c-1
    tmp = spin(r, c, s, customcopy(r,c,s,arr))
    arr =
    print(arr)