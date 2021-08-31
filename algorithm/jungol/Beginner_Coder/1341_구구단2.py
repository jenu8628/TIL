while True:
    s, e = map(int, input().split())
    if s < 2 or s > 9 or e < 2 or e > 9:
        print("INPUT ERROR!")
    else:
        t = 0
        if s >= e:
            while s-t >= e:
                idx = 1
                while idx < 10:
                    if idx % 3 == 1 and idx != 1:
                        print()
                    if (s-t)*idx < 10:
                        print("{} * {} =  {}".format(s-t, idx, (s-t)*idx), end="   ")
                    else:
                        print("{} * {} = {}".format(s-t, idx, (s-t)*idx), end="   ")
                    idx += 1
                print()
                print()
                t += 1
        elif s < e:
            while s+t <= e:
                idx = 1
                while idx < 10:
                    if idx % 3 == 1 and idx != 1:
                        print()
                    if (s+t)*idx < 10:
                        print("{} * {} =  {}".format(s+t, idx, (s+t)*idx), end="   ")
                    else:
                        print("{} * {} = {}".format(s+t, idx, (s+t)*idx), end="   ")
                    idx += 1
                print()
                print()
                t += 1
