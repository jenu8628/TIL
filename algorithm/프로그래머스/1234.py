def solution(sentence, keyword, skips):
    temp = list(sentence)
    key = list(keyword)
    cnt = 0
    for i in range(len(skips)):
        check = 0
        if cnt >= len(sentence)-1:
            break
        for k in range(cnt, cnt + skips[i] + 1):
            if key[i % len(keyword)] == temp[k]:
                temp.insert(k, key[i % len(keyword)])
                cnt += k + 1
                check = 1
                break
        if check == 1:
            continue
        # cnt : 현재 위치 + 건너뛸 위치
        if i == 0:
            cnt += skips[i]
        else:
            cnt += skips[i] + 1
        temp.insert(cnt, key[i % len(keyword)])
    return "".join(temp)

print(solution("i love coding","mask",[0, 0, 3, 2, 3, 4]))
print(solution("i love coding","mode",[0, 10]))
print(solution("abcde fghi","axyz",[3, 9, 0, 1]))
print(solution("encrypt this sentence","something",[0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]))
print("seoncrmypett thihisng ssenteonmcee")