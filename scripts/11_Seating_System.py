with open("inputs/11.txt", 'r') as file:
    lines = file.read().split("\n")

max_lines = len(lines) - 1
max_seats = len(lines[0]) - 1

def look_deep(y, x, seats, min_i, max_i, min_j, max_j, flag_i, flag_j):
    """
    Look for empty or occupied seats
    """
    num_seats = 0
    while min_j <= x <= max_j and min_i <= y <= max_i:
        if flag_i == '+':
            y += 1
        if flag_i == '-':
            y -= 1
        if flag_j == '+':
            x += 1
        if flag_j == '-':
            x -= 1

        if seats[y][x] == '#':
            num_seats += 1
            break
        if seats[y][x] == 'L':
            break

    return num_seats


def count_seats_deep(y, x, max_i, max_j, seats):
    """
    Counts occupied seats (DEEP)
    """
    num_seats = 0

    # look in each of the 8 directions
    num_seats += look_deep(y, x, seats, 0, max_i, 0, max_j-1, flag_i='', flag_j='+')
    num_seats += look_deep(y, x, seats, 0, max_i, 1, max_j, flag_i='', flag_j='-')
    num_seats += look_deep(y, x, seats, 0, max_i-1, 0, max_j, flag_i='+', flag_j='')
    num_seats += look_deep(y, x, seats, 1, max_i, 0, max_j, flag_i='-', flag_j='')
    num_seats += look_deep(y, x, seats, 0, max_i-1, 0, max_j-1, flag_i='+', flag_j='+')
    num_seats += look_deep(y, x, seats, 1, max_i, 1, max_j, flag_i='-', flag_j='-')
    num_seats += look_deep(y, x, seats, 0, max_i-1, 1, max_j, flag_i='+', flag_j='-')
    num_seats += look_deep(y, x, seats, 1, max_i, 0, max_j-1, flag_i='-', flag_j='+')

    return num_seats


current_state = lines
search = True
while search:
    new_state = []
    for i, line in enumerate(current_state):
        fill = ''
        for j, seat in enumerate(line):
            if current_state[i][j] == '.':
                fill += '.'
            elif current_state[i][j] == 'L':
                if count_seats_deep(i, j, max_lines, max_seats, current_state) == 0:
                    fill += '#'
                else:
                    fill += 'L'
            elif current_state[i][j] == '#':
                if count_seats_deep(i, j, max_lines, max_seats, current_state) >= 5:
                    fill += 'L'
                else:
                    fill += '#'
        new_state.append(fill)
    if current_state == new_state:
        search = False
    current_state = new_state

count = 0
for line in current_state:
    count += line.count('#')

print(count)

# Part 1 solution.

# with open("inputs/11.txt", 'r') as file:
#     lines = file.read().split("\n")

# max_i = len(lines) - 1
# max_j = len(lines[0]) - 1

# def count_seats(i, j, max_i, max_j, seats):
#     """
#     Counts occupied adjacent seats
#     """
#     num_seats = 0
#     x = [i-1, i, i+1]
#     y = [j-1, j, j+1]

#     positions = [el for el in [(a, b) for a in x for b in y] if (el[0] != i or el[1] != j)]
#     for pos in positions:
#         if (0 <= pos[0] <= max_i) and (0 <= pos[1] <= max_j):
#             if seats[pos[0]][pos[1]] == '#':
#                 num_seats += 1
#         else:
#             continue

#     return num_seats


# current_state = lines
# search = True
# while search:
#     new_state = []
#     for i, line in enumerate(current_state):
#         fill = ''
#         for j, seat in enumerate(line):
#             if current_state[i][j] == '.':
#                 fill += '.'
#             elif current_state[i][j] == 'L':
#                 if count_seats(i, j, max_i, max_j, current_state) == 0:
#                     fill += '#'
#                 else:
#                     fill += 'L'
#             elif current_state[i][j] == '#':
#                 if count_seats(i, j, max_i, max_j, current_state) >= 4:
#                     fill += 'L'
#                 else:
#                     fill += '#'
#         new_state.append(fill)
#     if current_state == new_state:
#         search = False
#     current_state = new_state


# count = 0
# for line in current_state:
#     count += line.count('#')

# print(count)
