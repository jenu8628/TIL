from collections import Counter

def solution(s):
    answer = []
    word = s.replace("{","").replace("}", "").split(",")
    count_word = Counter(word).most_common()
    for i in count_word:
        answer.append(int(i[0]))
    return answer

def solution2(s:str):
    word_list = list(map(int, s.replace("}", "").replace("{", "").split(",")))
    count_dict = Counter(word_list).most_common()
    answer = [item[0] for item in count_dict]
    return answer




if __name__ == '__main__':

    print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution2("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution2("{{20,111},{111}}"))
    print(solution2("{{123}}"))
    print(solution2("{{4,2,3},{3},{2,3,4,1},{2,3}}"))




# print(solution(s))