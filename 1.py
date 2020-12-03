import math

with open('./input1.txt', 'r') as input_file:
    # part 1
    numbers = list(map(int, input_file.read().split()))
    results = []
    for number in numbers:
        number_two = list(filter(lambda x: x + number == 2020,  numbers))
        if len(number_two) > 0:
            results = number, number_two[0]
            break
    print(math.prod(results))

    # part 2
    for number in numbers:
        for another_number in numbers:
            third_number = list(filter(lambda x: x + another_number + number == 2020,  numbers))
            if len(third_number) > 0:
                results = number, another_number, third_number[0]
    print(math.prod(results))
