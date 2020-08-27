import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    cnt = 0
    start = 0
    while True:
        #만약 start가 N-K보다 크면 브레이크/ 다음번에 바로 N까지 가기 때문
        if start >= N-K:
            start = start + K
            break
        #만약 start에서 k만큼 이동한곳에 충전기가 있다면 충전한다.
        # 그리고 start를 k만큼 이동!
        elif start + K in charge:
            cnt += 1
            start += K
        # 만약 start에서 k만큼 이동한 곳에 충전기가 없다면??
        # K만큼 이동하기 전에 있는 충전소중 숫자가 큰곳으로 이동!
        elif not start + K in charge:
            i_list = []
            for i in range(start+1, start+K):
                if i in charge:
                    i_list.append(i)
            if i_list == []:
                print(f'#{test_case} 0')
                break
            start = max(i_list)
            cnt += 1
    if start >= N:
        print(f'#{test_case} {cnt}')