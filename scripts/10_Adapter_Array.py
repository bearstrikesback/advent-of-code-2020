from itertools import groupby


with open("inputs/10.txt", 'r') as file:
    lines = file.read().split("\n")

elems = [int(elem) for elem in lines]

base = 0
diffs = []
for elem in sorted(elems):
    diffs.append(abs(base - elem))
    base = elem

seqs = [list(group) for k, group in groupby(diffs, lambda x: x == 3) if not k]
ways = 1

for seq in seqs:
    if len(seq) == 2:
        ways *= 2
    if len(seq) == 3:
        ways *= 4
    if len(seq) == 4:
        ways *= 7

print(ways)

# Part 1 solution.

# elems = [int(elem) for elem in lines]

# base = 0
# counts = {'1':0, '2':0, '3':1}
# for elem in sorted(elems):
#     res = abs(base - elem)
#     base = elem
#     if res == 1:
#         counts['1'] += 1
#     if res == 3:
#         counts['3'] += 1

# print(counts['1'] * counts['3'])
