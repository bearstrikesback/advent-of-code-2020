with open("inputs/2.txt", 'r') as file:
    lines = [line.split() for line in file.readlines()]

valid = 0
for line in lines:
    left = int(line[0].split('-')[0])
    right = int(line[0].split('-')[1])
    match = line[1][0]
    password = line[2]
    cnt = 0
    if password[left-1] == match:
        cnt += 1
    if password[right-1] == match:
        cnt += 1
    if cnt == 1:
        valid += 1

print(valid)
