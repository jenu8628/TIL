from itertools import combinations


def solution(relation):
    col = len(relation[0])
    # 전체 조합
    all_case = []
    for k in range(1, col + 1):
        all_case.extend(combinations(range(col), k))

    # 유일성
    unique = []
    for case in all_case:
        temp = ["".join(relate[int(idx)] for idx in case) for relate in relation]
        if len(set(temp)) == len(relation):
            unique.append(case)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            # if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
    return len(answer)


def is_minimality(unique: list, case: set):
    for have_case in unique:
        # if len(have_case) == len((case & have_case)):
        if len(have_case) == len(case.intersection(have_case)):
            return False
    return True

def solution2(relation):
    col = len(relation[0])
    row = len(relation)
    # 전체 조합
    all_case = []
    for k in range(1, col + 1):
        all_case.extend(map(list, combinations(range(col), k)))

    unique = []
    for case in all_case:
        case = set(case)
        # 최소성
        if not is_minimality(unique, case):
            continue
        # 유일성
        temp = ["|".join(relate[idx] for idx in case) for relate in relation]
        if len(set(temp)) == row:
            unique.append(case)
    return len(unique)


if __name__ == '__main__':
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]

    print(solution(relation=relation))
    # print(solution([['1001','2'], ['100', '12'], ['100', '2']]))
