from collections import Counter
from difflib import SequenceMatcher

from operator import itemgetter


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def main():
    part_one()
    part_two()


def part_one():
    word_twice_count = 0
    word_three_times_count = 0

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            line_counter = Counter(line)
            if 2 in line_counter.values():
                word_twice_count += 1
            if 3 in line_counter.values():
                word_three_times_count += 1

    checksum = word_twice_count * word_three_times_count

    print 'checksum is ' + str(checksum)


def part_two():
    with open('input.txt', 'r') as input_file:
        lines = [line for line in input_file]

    similarity_strings = [(line, comparing_line, similar(line, comparing_line))
                          for line in lines for comparing_line in lines
                          if line is not comparing_line]

    most_similair_strings = max(similarity_strings, key=itemgetter(2))

    result_word = ''.join([char_word_one
                           for char_word_one, char_word_two in zip(most_similair_strings[0], most_similair_strings[1])
                           if char_word_one == char_word_two])

    print result_word


if __name__ == '__main__':
    main()
