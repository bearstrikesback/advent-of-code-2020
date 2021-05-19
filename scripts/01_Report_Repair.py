from itertools import combinations


with open('inputs/1.txt', 'r') as file:
    input_data = file.read().split("\n")[::1]

pairs = combinations(input_data, 3)

for pair in pairs:
    if int(pair[0]) + int(pair[1]) + int(pair[2]) == 2020:
        print(int(pair[0]) * int(pair[1]) * int(pair[2]))
