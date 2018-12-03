import re


def main():
    data = parse_data()
    overlaps = calculate_collisions(data)
    part_one(overlaps)
    part_two(data, overlaps)


def parse_data():
    with open('input.txt', 'r') as input_file:
        data = []
        for line in input_file:
            information = [int(n) for n in re.findall(r'\d+', line)]
            data.append({'id': information[0], 'place': [information[1], information[2]],
                         'dim': [information[3], information[4]]})
    return data


def get_coordinates(coordinates, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            yield str(x + coordinates[0]) + "," + str(y + coordinates[1])


def calculate_collisions(data):
    collisions = set()
    filled = set()
    for line in data:
        for coord in get_coordinates(line['place'], line['dim']):
            if coord in filled:
                collisions.add(coord)
            else:
                filled.add(coord)
    return collisions


def has_no_collisions(coordinates, dimensions, overlaps):
    for coord in get_coordinates(coordinates, dimensions):
        if coord in overlaps:
            return False
    return True


def find_no_overlaps(data, overlaps):
    for line in data:
        if has_no_collisions(line['place'], line['dim'], overlaps):
            return line['id']


def part_two(data, overlaps):
    print(find_no_overlaps(data, overlaps))


def part_one(collisions):
    print(len(collisions))


if __name__ == '__main__':
    main()
