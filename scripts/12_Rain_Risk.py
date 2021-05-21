with open("inputs/12.txt", 'r') as file:
    lines = file.read().split("\n")

dirs = ['E', 'S', 'W', 'N']
curr_waypoint = {'E':10, 'S':0, 'W':0, 'N':1}
path = {'E':0, 'S':0, 'W':0, 'N':0}

for line in lines:
    if line[:1] in ['R', 'L']:
        step = (int(line[1:]) % 360) // 90
        if line[:1] == 'L':
            step = -1 * step
        new_keys = list(curr_waypoint.keys())
        new_keys = list(new_keys[step:] + new_keys)[:4]
        new_vals = list(curr_waypoint.values())
        curr_waypoint = dict(zip(new_keys, new_vals))
    elif line[:1] in dirs:
        way = line[:1]
        distance = int(line[1:])
        curr_waypoint[way] += distance
    elif line[:1] == 'F':
        distance = int(line[1:])
        for k, v in curr_waypoint.items():
            path[k] += distance * v

print(abs(path['S'] - path['N']) + abs(path['W'] - path['E']))

# Part 1 solution.

# with open("inputs/12.txt", 'r') as file:
#     lines = file.read().split("\n")

# curr_dir = 'E'
# dirs = ['E', 'S', 'W', 'N']
# path = {'E':0, 'S':0, 'W':0, 'N':0}

# for line in lines:
#     if line[:1] in ['R', 'L']:
#         step = (int(line[1:]) % 360) // 90
#         if line[:1] == 'L':
#             step = -1 * step
#         curr_dir = dirs[step]
#         dirs = list(dirs[step:] + dirs)[:4]
#     elif line[:1] in dirs:
#         way = line[:1]
#         distance = int(line[1:])
#         path[way] += distance
#     elif line[:1] == 'F':
#         distance = int(line[1:])
#         path[curr_dir] += distance

# print(abs(path['S'] - path['N']) + abs(path['W'] - path['E']))
