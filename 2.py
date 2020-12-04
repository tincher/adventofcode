dummy = {'min': 1,
         'max': 3,
         'char': 'f',
         'password': 'afsadf'}

with open('./input2.txt') as input_file:
    # part 1
    lines = input_file.read().split('\n')
    elements = []
    for line in lines:
        if line == '':
            break
        policy, password = line.split(':')
        element = {'password': password.strip()}
        policy_range, policy_char = policy.split(' ')
        element['char'] = policy_char
        policy_min, policy_max = policy_range.split('-')
        element['min'] = int(policy_min)
        element['max'] = int(policy_max)
        elements.append(element)

    valid_passwords = 0
    for elem in elements:
        count = elem['password'].count(elem['char'])
        if elem['min'] <= count <= elem['max']:
            valid_passwords += 1
    print(valid_passwords)

    # part 2
    valid_passwords = 0
    for elem in elements:
        is_in_first_place = elem['password'][elem['min'] - 1] == elem['char']
        is_in_second_place = elem['password'][elem['max'] - 1] == elem['char']
        if (is_in_first_place and not is_in_second_place) or (not is_in_first_place and is_in_second_place):
            valid_passwords += 1
    print(valid_passwords)
