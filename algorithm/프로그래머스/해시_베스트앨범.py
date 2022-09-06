def solution(genres, plays):
    answer = []
    # {장르 : 총 재생횟수}
    playsDict = {}
    # {장르: [(플레이 횟수, 고유번호)]}
    count = {}
    for i in range(len(genres)):
        playsDict[genres[i]] = playsDict.get(genres[i], 0) + plays[i]
        count[genres[i]] = count.get(genres[i], []) + [(plays[i], i)]
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    for (genre, totalplay) in genreSort:
        # 플레이 횟수: 내림차순, 고유번호:오름차순 정렬
        count[genre] = sorted(count[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in count[genre][:2]]
    return answer