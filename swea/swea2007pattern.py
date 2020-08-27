T = int(input())
for tc in range(1, T+1):
    string = input()
    cnt =1
    pat = ''
    Disc = False

    while True:
        pat = string[:cnt]
        # 마디의 최대 길이가 되면 탈출
        if cnt == 10:
            break
        # string[0:1]과 string[1:2] 비교 다르면
        # string[0:2]와 string[2:4] 비교 ....
        for i in range(cnt, len(string), cnt):
            # pat과 string다음 같은 글자수가 다르면 for문 탈출
            # cnt +1 해서 다시 for문에 들어간다.
            if pat != string[i:i + cnt]:
                break
            # pat와 string 의 정해진 구간의 문자열이 같다면 탈출
            else:
                Disc = True
                break
        # Disc = True가 된다면 탈출
        if Disc == True: # if Disc:라고 써도 됨.
            break

        cnt += 1
    print(f'#{tc} {len(pat)}')
