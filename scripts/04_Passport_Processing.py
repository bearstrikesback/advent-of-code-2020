with open("inputs/4.txt", 'r') as file:
    lines = [line.split() for line in file.readlines()]

ch = []

valid = 0
passport = []
for elem in lines:
    if len(elem) != 0:
        passport.extend(elem)
        if len(passport) == 8 or (len(passport) == 7 and ''.join(passport).count('cid') == 0):
            passdict = dict()
            chars = '0123456789abcdef'
            eyes = {"brn", "amb", "blu", "gry", "grn", "hzl", "oth"}
            nums = '0123456789'

            for field in passport:
                passdict[field.split(':')[0]] = field.split(':')[1]
            for key in passdict:

                if key == 'byr':
                    if int(passdict['byr']) > 2002 or int(passdict['byr']) < 1920:
                        passport = []

                if key == 'iyr':
                    if int(passdict['iyr']) > 2020 or int(passdict['iyr']) < 2010:
                        passport = []

                if key == 'eyr':
                    if int(passdict['eyr']) > 2030 or int(passdict['eyr']) < 2020:
                        passport = []

                if key == 'hgt':
                    if (passdict['hgt'][-2:] != 'cm') and (passdict['hgt'][-2:] != 'in'):
                        passport = []
                    if (passdict['hgt'][-2:] == 'cm') and \
                        (int(passdict['hgt'][:-2]) > 193 or int(passdict['hgt'][:-2]) < 150):
                        passport = []
                    if (passdict['hgt'][-2:] == 'in') and \
                        (int(passdict['hgt'][:-2]) > 76 or int(passdict['hgt'][:-2]) < 59):
                        passport = []

                if key == 'hcl':
                    if passdict['hcl'][0] != '#' or len(str(passdict['hcl'])) != 7:
                        passport = []
                    for el in passdict['hcl'][1:]:
                        if el not in chars:
                            passport = []

                if key == 'ecl':
                    if passdict['ecl'] not in eyes:
                        passport = []

                if key == 'pid':
                    if len(str(passdict['pid'])) != 9:
                        passport = []
                    for el in passdict['pid']:
                        if el not in nums:
                            passport = []

        if len(passport) == 8 or (len(passport) == 7 and ''.join(passport).count('cid') == 0):
            valid += 1
            ch.append(passdict['hgt'])
            passport = []
    else:
        passport = []

print(valid)
