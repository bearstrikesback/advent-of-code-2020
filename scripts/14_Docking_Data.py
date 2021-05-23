from itertools import combinations


with open("inputs/14.txt", 'r') as file:
    lines = file.read().rstrip().split("\n")

def decimalToBinary(n):
    return bin(n).replace("0b", "")


def floatToAddress(bits):
    vals = []
    vals.append(bits)
    num_float = bits.count('X')
    cmbnations = []

    posX = []
    for j, elem in enumerate(bits):
        if elem == 'X':
            posX.append(j)

    for j in range(1, num_float+1):
        cmbnations.extend(list(combinations(posX, j)))

    list_bits = list(bits)
    for elem in cmbnations:
        if len(elem) == 1:
            list_bits[list(elem)[0]] = '1'
        elif len(elem) > 1:
            for pos in elem:
                list_bits[pos] = '1'
        vals.append(''.join(list_bits))
        list_bits = list(bits)

    addresses = []
    for adr in vals:
        addresses.append(adr.replace('X', '0'))

    return addresses

memory = dict()
buffer = '0' * 36
mask = ''

for line in lines:
    holder = ''
    if str(line).startswith('mask'):
        mask = line.split(' = ')[1]
    elif str(line).startswith('mem'):
        mem, num = line.split(' = ')
        mem = mem.replace('mem[', '').replace(']', '')
        mem = decimalToBinary(int(mem))
        mem = str(buffer + mem)[-36:]
        for i, binary in enumerate(mem):
            if mask[i] == '0':
                holder += mem[i]
            elif mask[i] == '1':
                holder += '1'
            elif mask[i] == 'X':
                holder += 'X'

        list_addresses = floatToAddress(holder)
        for address in list_addresses:
            memory[int(address, 2)] = int(num)

res = 0
for key in memory:
    res += memory[key]

print(res)

# Part 1 solution.

# with open("inputs/14.txt", 'r') as file:
#     lines = file.read().rstrip().split("\n")

# def decimalToBinary(n):
#     return bin(n).replace("0b", "")

# memory = dict()
# buffer = '0' * 36
# mask = ''

# for line in lines:
#     holder = ''
#     if str(line).startswith('mask'):
#         mask = line.split(' = ')[1]
#     elif str(line).startswith('mem'):
#         mem, num = line.split(' = ')
#         mem = mem.replace('mem[', '').replace(']', '')
#         num = decimalToBinary(int(num))
#         num = str(buffer + num)[-36:]
#         for i, binary in enumerate(num):
#             if mask[i] == 'X':
#                 holder += num[i]
#             else:
#                 holder += mask[i]
#         memory[mem] = int(holder, 2)

# res = 0
# for key in memory:
#     res += memory[key]

# print(res)
