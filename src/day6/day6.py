from collections import defaultdict

from operator import itemgetter


def main():
    coordinates = read_coordinates()
    part_one(coordinates)


def read_coordinates():
    coordinates = []
    with open('input.txt', 'r') as input_file:
        index = 1
        for line in input_file:
            cor_pair = [int(cor) for cor in line.strip().split(',')]
            cor_pair.append(index)
            coordinates.append(cor_pair)
            index += 1
    return coordinates


def part_one(coordinates):
    min_x = min([cor_pair[1] for cor_pair in coordinates])
    max_x = max([cor_pair[1] for cor_pair in coordinates]) + 1
    min_y = min([cor_pair[0] for cor_pair in coordinates])
    max_y = max([cor_pair[0] for cor_pair in coordinates]) + 1

    area_dict = defaultdict(int)

    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            h_distances = [[hamming_distance([i, j], cor_pair), cor_pair[2]] for cor_pair in coordinates]
            min_h_distance = min(h_distances, key=itemgetter(0))
            count_min_h_distance = sum(1 for item in h_distances if item[0] == min_h_distance[0])
            if count_min_h_distance == 1:
                area_dict[min_h_distance[1]] += 1
                if i in (min_y, max_y - 1) or j in (min_x, max_x - 1):
                    area_dict[min_h_distance[1]] = float('-inf')

    print max(area_dict.iteritems(), key=itemgetter(1))


def hamming_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()
