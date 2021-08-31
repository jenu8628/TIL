Greetings = [72, 97, 118, 101, '-', 97, '-', 72, 97, 112, 112, 121, '-', 67, 104, 117, 115, 101, 111, 107]
for greeting in Greetings:
    if greeting == '-':
        print(' ', end='')
    else:
        print(chr(greeting), end='')
print()
careful = [66, 101, 119, 97, 114, 101, '-', 111, 102, '-', 67, 111, 114, 111, 110, 97]
for i in range(len(careful)):
    if careful[i] == '-':
        print(' ', end='')
    else:
        print(chr(careful[i]), end='')
print('19')

# 즐거운 추석 되시고, 코로나 조심하세요~~~