def hex_to_dec(num16):
    value = 0
    for i in range(len(num16)):
        if '0' <= num16[i] <= '9':
            tmp = ord(num16[i]) - ord('0')
        else:
            tmp = ord(num16[i]) - ord('A') + 10
        value += tmp * (16 ** (L-1-i))
    return value

for tc in range(1, int(input())+1):
    # 숫자의 개수, K번째 크기
    N, K = map(int, input().split())
    # N은 4의 배수이므로 하나의 비밀번호 길이는 L
    L = N // 4
    password = list(input())
    # 중복된 값을 넣지 않게
    ans = set()

    for i in range(L):
        #0번부터 L번 스텝을 뛰면서 사용
        for j in range(0, N, L):
            # L의 길이만큼 잘라서 16진수 형태로 넣는다
            ans.add("".join(password[j:j+L]))
            # ans.add(int("".join(password[j:j + L]), 16))
        # 시계방향과 돈것과 같은 효과
        password.insert(0, password.pop())
    ans = list(ans)
    # 16진수 -> 10진수로 변환하지 않았어도 자동으로 될것임.
    ans.sort(reverse=True)
    print("#{} {}".format(tc, hex_to_dec(ans[K-1])))
    # print("#{} {}".format(tc, ans[K - 1]))

# 다른풀이 --------------------------------------------------

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    L = N // 4
    password = input()
    ans = set()
    password += password[:L-1]
    for i in range(N):
        ans.add(int(password[i:i+L], 16))
    ans = list(ans)
    ans.sort(reverse=True)
    print("#{} {}".format(tc, ans[K-1]))