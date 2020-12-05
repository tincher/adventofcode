from functools import reduce


def get_number(text, char_for_one):
    binary_array = ['1' if x == char_for_one else '0' for x in text]
    binary = reduce(lambda x, y: x + y, binary_array)
    return int(binary, 2)


with open('./input5.txt') as input_file:
    rows = input_file.read().split('\n')[:-1]
    rows = list(map(lambda x: (x[:-3], x[-3:]), rows))
    seat_ids = []
    for (row, seat) in rows:
        row = get_number(row, 'B')
        seat = get_number(seat, 'R')
        seat_ids.append(row * 8 + seat)
    print(max(seat_ids))

    my_seat_id = 0
    seat_ids = sorted(seat_ids)
    for i in range(1, len(seat_ids)):
        if seat_ids[i - 1] == seat_ids[i] - 2:
            my_seat_id = seat_ids[i] - 1
    print(my_seat_id)
