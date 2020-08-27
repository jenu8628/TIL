T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    grade = [list(map(int, input().split()))for i in range(N)]
    total = []
    # 학생들의 시험점수를 모아서 리스트로 만듬
    for i in range(N):
        total_grade = ((grade[i][0]*35)+(grade[i][1]*45)+(grade[i][2]*20))/100
        total.append(total_grade)
    # 순위별로 성적을 나눠서
    # 그 성적에 해당하는 부분에 K번째 성적이 들어간다면
    # 성적을 print한다.
    grade_rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for j in range(0, 10):
        if total[K-1] in sorted(total)[(j*N)//10:((j+1)*N)//10]:
            print('#{} {}'.format(tc, grade_rank[-(j+1)]))
            break
