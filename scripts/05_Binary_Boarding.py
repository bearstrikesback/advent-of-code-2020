with open("inputs/5.txt", 'r') as file:
    lines = [line.split() for line in file.readlines()]

tickets = []
for ticket in lines:
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7

    for elem in str(ticket):
        if elem == "B":
            step = (row_max + 1 - row_min) // 2
            row_min += step
        if elem == "F":
            step = (row_max + 1 - row_min) // 2
            row_max -= step
        if elem == "R":
            step = (col_max + 1 - col_min) // 2
            col_min += step
        if elem == "L":
            step = (col_max + 1 - col_min) // 2
            col_max -= step

    ticket_id = int(row_max * 8 + col_max)
    tickets.append(ticket_id)

boarding_pass = sorted(tickets)
for idx in range(len(boarding_pass) - 1):
    if boarding_pass[idx] + 1 != boarding_pass[idx + 1]:
        print(boarding_pass[idx] + 1)
