with open("inputs/6.txt", 'r') as file:
    lines = file.read().split("\n\n")

result = 0
for line in lines:
    tmp = line.split('\n')
    if len(tmp) == 1:
        result += len(line)
    else:
        result += len(set.intersection(*map(set, tmp)))

print(result)
