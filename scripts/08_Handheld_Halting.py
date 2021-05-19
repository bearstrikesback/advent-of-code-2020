with open("inputs/8.txt", 'r') as file:
    lines = file.read().split("\n")

candidates = []

for i, line in enumerate(lines):
    cmd, step = line.split()
    if cmd in ['jmp', 'nop']:
        candidates.append(i)

for candidate in candidates:
    steps = dict()
    score = 0
    pos = 0

    while True:
        steps[pos] = 1
        cmd, step = lines[pos].split()
        if candidate == pos:
            if cmd == 'jmp':
                cmd = 'nop'
            else:
                cmd = 'jmp'

        if cmd == 'jmp':
            if step[0] == '+':
                pos += int(step[1:])
            else:
                pos -= int(step[1:])
        if cmd == 'acc':
            if step[0] == '+':
                score += int(step[1:])
                pos += 1
            else:
                score -= int(step[1:])
                pos += 1
        if cmd == 'nop':
            pos += 1
        if pos in steps:
            break
        if pos == 612:
            print(score)
            break
