### 1. 부분집합구하기

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N

def powerset(idx):
    #도착을 했을때
    if idx == N:
        print(sel , " : ", end=" ")
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return
    #해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx+1)
    #해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx+1)

powerset(0)
```

### 2. 부분집합의 합 구하기

```python
# 내풀이
def sum_set(arr):
    total = []
    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        if sum(subset) == 10:
            total.append(subset)
    return total
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
print(sum_set(arr))

# 쌤풀이
N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sel = [0] * N
def powerset(idx):
    # 도착을 했을때
    if idx == N:
        print(sel)
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일때 경우만 출력
        if total == 10:
            print(sel)
        return
    # 해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx + 1)
    # 해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx + 1)
powerset(0)
```

### 3. 부분집합의 합 구하기 백트래킹

```python
N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sel = [0] * N
def powerset(idx, sum_num):
    #지금까지 더한값들을 들고 다니는데
    if sum_num > 10:
        #이미 벗어나면 더이상 수행할 필요가없음
        return
    # 도착을 했을때
    if idx == N:
        print(sel)
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        # #합이 10일때 경우만 출력
        # if total == 10:
        #     print(sel)
        return
    # 해당자리를 뽑고 가고
    sel[idx] = 1
    sum_num += arr[idx]
    powerset(idx + 1 , sum_num)
    # 해당자리를 안뽑고 가고
    sel[idx] = 0
    sum_num -= arr[idx]
    powerset(idx + 1, sum_num)
powerset(0,0)
```

