while True:
    s, e = map(int, input().split())
    if s < 2 or s > 9 or e < 2 or e > 9:
        print("INPUT ERROR!")
    else:
        idx = 1
        if s >= e:
            while idx < 10:
                t = 0
                while s-t >= e:
                    if (s-t)*idx < 10:
                        print("{} * {} =  {}".format(s-t, idx, (s-t)*idx), end="   ")
                    else:
                        print("{} * {} = {}".format(s-t, idx, (s-t)*idx), end="   ")
                    t += 1
                print()
                idx += 1
        elif s < e:
            while idx < 10:
                t = 0
                while s+t <= e:
                    if (s+t)*idx < 10:
                        print("{} * {} =  {}".format(s+t, idx, (s+t)*idx), end="   ")
                    else:
                        print("{} * {} = {}".format(s+t, idx, (s+t)*idx), end="   ")
                    t += 1
                print()
                idx += 1