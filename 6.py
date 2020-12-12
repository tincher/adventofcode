with open('./input6.txt') as input_file:
    groups = input_file.read().split('\n\n')

    result = 0
    for group in groups:
        result += len(set(set(filter(lambda x: x != '\n', group))))
    print(result)

    result = 0
    for group in groups:
        persons = group.split('\n')
        person_count = len(list(filter(lambda x: x != '', group.split('\n'))))
        # person_count = len(group.split('\n'))
        chars = sorted(list(filter(lambda x: x != '\n', group)))
        print('-------')
        print([x for x in chars if chars.count(x) == person_count])
        print(set([x for x in chars if chars.count(x) == person_count]))
        result += len(set([x for x in chars if chars.count(x) == person_count]))

    print(result)
