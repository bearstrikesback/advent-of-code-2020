from functools import reduce


paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []
for path in paths:
    with open('inputs/3.txt', 'r') as file:
        input_data = file.read().split("\n")[::path[1]]

    pos = path[0]
    numtrees = 0
    for line in input_data[1:]:
        if len(line) != 0:
            if pos <= len(line) - 1:
                if line[pos] == '#':
                    numtrees += 1
                pos += path[0]
            else:
                pos = pos - len(line)
                if line[pos] == '#':
                    numtrees += 1
                pos += path[0]

    trees.append(numtrees)

res = reduce(lambda x, y: x*y, trees)
print(res)
