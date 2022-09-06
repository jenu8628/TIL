def solution(fees, records):
    answer = []
    temp = {}

    end_time = 23*60 + 59
    numbers = []
    for record in records:
        a, number, state = record.split()
        if number not in numbers:
            numbers.append(number)
    numbers.sort()

    for num in numbers:
        temp[num] = temp.get(num, [])
    for record in records:
        a, number, state = record.split()
        h, m = a.split(':')
        time = (int(h) * 60) + int(m)
        temp[number].append([time, state])

    for key, val in temp.items():
        cost = 0
        time = 0
        if val[-1][1] == 'IN':
            time += end_time - val[-1][0]

        for i in range(len(val)):
            if val[i][1] == 'IN':
                in_time = val[i][0]
            if val[i][1] == 'OUT':
                out_time = val[i][0]
                time += out_time - in_time

        if time <= fees[0]:
            cost += fees[1]
        else:
            cost += fees[1]
            x = (time - fees[0]) // fees[2]
            if (time - fees[0]) % fees[2] != 0:
                x = ((time - fees[0]) // fees[2]) + 1
            cost += x * fees[3]
        answer.append(cost)
    return answer
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))