# 방법 1, 2
# 2는 1보다 빠르고 패스는 되지만 그렇게 빠르진 않음.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    # visit = [0] * (sum(score) + 1)  # 마지막에 중복을 제거 최대 100점
    # 이제 시간을 줄여야함!
    # 레벨별로 구분 열은 s
    visit = [[0] * (sum(score) + 1) for _ in range(N+1)]

    def dfs(k, s):   # 인자는 점수
        if visit[k][s]:
            return
        visit[k][s] = 1
        # if k == N:
        #     print(s, end=" ")
        #     visit[k][s] = 1    # 여러번 나와도 1로덮어쓰므로 중복 제거
        if k == N:
            return
        else:
            dfs(k+1, s) # k번 문제를 틀린 경우
            dfs(k+1, s+score[k]) # k번 문제를 맞은 경우

    dfs(0,0)
    print(sum(visit[N]))

# 방법 3 하지만 중복제거를 해줘야 함
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [0] * (sum(score) + 1)
    # 0을 시작점으로
    Q = [[0, 0]]     # k,s 마치 함수의 매개변수 역할
    while Q:
        k, s = Q.pop(0)
        if k == N:
            print(s, end=' ')
            visit[s] = 1
        else:
            Q.append([k + 1, s])
            Q.append([k + 1, s + score[k]])

# 방법 4
# 1번문제 배점 2,3,5
# 매 레벨에 배점 2, 3, 5를 가지고 할 예정
# 0부터 - 2점을 맞은경우 틀린경우 그밑에는 3점을 맞은경우 틀린경우 이런식
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [0] * (sum(score) + 1)
    Q = [0]
    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] + val]:
                continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)
    print("#{} {}".format(tc, len(Q)))