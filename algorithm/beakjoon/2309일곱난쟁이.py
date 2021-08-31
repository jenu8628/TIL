# 방법 1
# 조합
def comb(idx, sidx):
    global result
    # 7가지를 다 뽑았는데
    if sidx == 7:
        tmp = sel[:]
        # 그들의 합이 100 이라면
        if sum(tmp) == 100:
            # result에 담고 리턴
            result = tmp
            return
        return
    if idx == 9:
        return
    sel[sidx] = arr[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)

arr = []
for i in range(9):
    arr.append(int(input()))
sel = [0] * 7
result = []
comb(0, 0)
for i in sorted(result):
    print(i)

# 방법 2
arr = []
for i in range(9):
    arr.append(int(input()))
result = []
for i in arr:
    # 리스트 복사를 통해 원소를 두개씩 지우며 조건을 충족할 예정
    tmp = arr
    tmp.remove(i)
    for j in arr:
        # tmp2를 만들어서 반복문이 돌며 원소가 계속 삭제되는 것을 방지
        tmp2 = tmp
        # i 와 j가 같은 경우는 건너뛰기
        if i == j:
            continue
        tmp2.remove(j)
        if sum(tmp2) == 100:
            result = sorted(tmp2)
            # 찾으면 반복문 끝내기
            break
    # result가 만들어 졌다면 반복문 탈출
    if result:
        break
# 답출력을 위한 반복문
for i in result:
    print(i)