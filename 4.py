import re
import numpy

with open('./input4.txt') as input_file:
    text = input_file.read()
    passports = text.split('\n\n')

    valid_passport_count = 0
    min_reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    all_fields_passports = []
    for passport in passports:
        fields = [i for a in list(map(lambda x: x.split('\n'), passport.split(' '))) for i in a]
        if len(list(filter(lambda x: x.split(':')[0] in min_reqs, fields))) >= 7:
            valid_passport_count += 1
            all_fields_passports.append(sorted(fields))

    valid_passport_count = 0
    for passport in all_fields_passports:
        passport = list(filter(lambda x: not(x == '' or 'cid' in x), passport))
        regexes = [r':(19[2-9]\d|200[0-2])$',
                   r':(amb|blu|brn|gry|grn|hzl|oth)$',
                   r':(202\d|2030)$',
                   r'#(\d|[a-f]){6}$',
                   r':((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$',
                   r':(201\d|2020)$',
                   r':(\d){9}$']
        matches = list(map(lambda i: re.search(regexes[i], passport[i]), range(len(regexes))))
        if matches.count(None) > 0:
            pass
        else:
            valid_passport_count += 1
    print(valid_passport_count)
