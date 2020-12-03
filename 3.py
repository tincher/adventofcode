import math


with open('./input3.txt') as input_file:
    text = input_file.read()
    rows = text.split('\n')
    configs = list(zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]))
    tree_counts = []
    for lateral_steps, vertical_steps in configs:
        position = 0
        tree_count = 0
        for r in range(len(rows))[::vertical_steps]:
            if rows[r] == '':
                break
            if position >= len(rows[r]):
                position = position % len(rows[0])
            if rows[r][position] == '#':
                tree_count += 1
            position += lateral_steps
        tree_counts.append(tree_count)
    print(math.prod(tree_counts))
