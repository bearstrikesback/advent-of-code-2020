from functools import reduce


with open("inputs/13.txt", 'r') as file:
    lines = file.read().split("\n")

buses = [int(x) for x in lines[1].split(',') if x != 'x']
poses = [int(i) for i, elem in enumerate(lines[1].split(',')) if elem != 'x']

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sm = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sm += a_i * mul_inv(p, n_i) * p
    return sm % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

remainders = [a - b for a, b in zip(buses, poses)]
print(chinese_remainder(buses, remainders))

# Part 1 solution.

# with open("inputs/13.txt", 'r') as file:
#     lines = file.read().split("\n")

# timestamp = int(lines[0])
# buses = [int(x) for x in lines[1].split(',') if x != 'x']

# buses = sorted(buses)
# diff = []
# for bus in buses:
#     diff.append(bus - (timestamp % bus))

# wait_time = min(diff)
# first_bus = buses[diff.index(min(diff))]
# print(first_bus * wait_time)
