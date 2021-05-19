with open("inputs/9.txt", 'r') as file:
    lines = file.read().split("\n")

for i, line in enumerate(lines):
    if line == '1504371145':
        pos = int(i)

start = 0
search = True
while search:
    for j in range(2, pos):
        elems = [int(elem) for elem in lines[start:j]]
        if sum(elems) == 1504371145:
            print(max(elems) + min(elems))
            search = False
    start += 1

# Part 1 solution. 1504371145

# from itertools import combinations


# with open("inputs/9.txt", 'r') as file:
#     lines = file.read().split("\n")

# start = 0
# stop = 25

# while True:
#     pairs = combinations(lines[start:stop], 2)
#     test = lines[stop]
#     if any(int(pair[0]) + int(pair[1]) == int(test) for pair in pairs):
#         start += 1
#         stop += 1
#     else:
#         print(test)
#         break
