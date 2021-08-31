N = int(input())
three = [3, 6, 9]
for i in range(1,N+1):
    if '3' in str(i):
        for j in str(i):
            for k in three:
                if str(j) in str(k):
                    print('-', end='')
    elif '6' in str(i):
        for j in str(i):
            for k in three:
                if str(j) in str(k):
                    print('-', end='')
    elif '9' in str(i):
        for j in str(i):
            for k in three:
                if str(j) in str(k):
                    print('-', end='')
    else:
        print( i, end = '')
    print(' ',end='')